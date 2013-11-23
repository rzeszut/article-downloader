import requesocks as r
import re
import lxml.html as html

import config

session = r.session()
session.proxies = {
    'http': config.PROXY_ADDRESS,
    'https': config.PROXY_ADDRESS
}

def get_page(url):
    global session
    resp = session.get(url)
    dom = html.fromstring(resp.text)
    dom.make_links_absolute(url)
    return dom

class SearchPage:
    BIBL_PAGE_PATTERN = re.compile("^.*Bibliographic Page.*$")

    def __init__(self, url):
        self.url = url
        self.page = get_page(url)
        self.initialize()

    def initialize(self):
        link_elems = filter(self.is_page_link, self.page.cssselect('a'))
        self.links = map(lambda l: l.attrib['href'], link_elems)

    @staticmethod
    def is_page_link(link):
        m = re.match(SearchPage.BIBL_PAGE_PATTERN, link.text_content())
        return (m is not None)

class BibliographicPage:
    TITLE_PATTERN = re.compile("^.*Title.*$")
    AUTHORS_PATTERN = re.compile("^.*Authors.*$")
    KEYWORDS_PATTERN = re.compile("^.*Keywords.*$")
    ABSTRACT_PATTERN = re.compile("^.*Abstract.*$")
    PUBLISHER_PATTERN = re.compile("^.*Publisher.*$")
    ISSN_PATTERN = re.compile("^.*ISSN.*$")
    YEAR_PATTERN = re.compile("(\d{4})")

    def __init__(self, url):
        self.url = url
        self.page = get_page(url)
        self.journal = None
        self.title = None
        self.authors = None
        self.keywords = None
        self.abstract = None
        self.publisher = None
        self.issn = None
        self.year = None
        self.initialize()

    def initialize(self):
        rows = self.page.cssselect('table tr td table tr td table tr')
        for r in rows:
            tds = r.cssselect('td')
            if len(tds) == 1:
                self.set_journal(tds[0])
            elif len(tds) == 2:
                field = tds[0].text_content().strip()
                value = tds[1].text_content().strip()

                self.set_title(field, value)
                self.set_authors(field, value)
                self.set_keywords(field, value)
                self.set_abstract(field, value)
                self.set_publisher(field, value)
                self.set_issn(field, value)
                self.set_year(field, value)

    def set_journal(self, td):
        if self.journal is None:
            links = td.cssselect('a')
            if len(links) > 0:
                value = links[0].text_content().strip()
                self.journal = value

    def set_title(self, field, value):
        if self.title is None:
            if re.match(self.TITLE_PATTERN, field) is not None:
                self.title = value

    def set_authors(self, field, value):
        if self.authors is None:
            if re.match(self.AUTHORS_PATTERN, field) is not None:
                self.authors = map(lambda s: s.strip()[:-1], value.split(';'))

    def set_keywords(self, field, value):
        if self.keywords is None:
            if re.match(self.KEYWORDS_PATTERN, field) is not None:
                self.keywords = map(lambda s: s.strip().lower(), value.split(';'))

    def set_abstract(self, field, value):
        if self.abstract is None:
            if re.match(self.ABSTRACT_PATTERN, field) is not None:
                self.abstract = value

    def set_publisher(self, field, value):
        if self.publisher is None:
            if re.match(self.PUBLISHER_PATTERN, field) is not None:
                self.publisher = value

    def set_issn(self, field, value):
        if self.issn is None:
            if re.match(self.ISSN_PATTERN, field) is not None:
                self.issn = value

    def set_year(self, field, value):
        if self.year is None:
            y = re.search(self.YEAR_PATTERN, field)
            if y is not None:
                self.year = int(y.group(0))

