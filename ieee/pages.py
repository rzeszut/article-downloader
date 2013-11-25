import re

import connection as con

def uniq(lst):
    return list(set(lst))

class SearchPage:
    def __init__(self, url):
        self.url = url
        self.page = con.get_page(url)
        self.initialize()

    def initialize(self):
        link_elems = self.page.cssselect('.noAbstract h3 a')
        self.links = map(lambda l: l.attrib['href'], link_elems)

class ArticlePage:
    YEAR_PATTERN = re.compile('(\d{4})')

    def __init__(self, url):
        self.url = url
        self.page = con.get_page(url)
        self.publisher = None
        self.issn = None
        self.title = None
        self.abstract = None
        self.journal = None
        self.year = None
        self.source = 'ieeexplore.ieee.org'
        self.initialize()

    def initialize(self):
        self.set_title()
        self.set_abstract()
        self.set_journal_and_year()
        self.set_authors()
        self.set_keywords()

    def set_title(self):
        title_info = self.page.cssselect('div.title h1')
        if len(title_info) > 0:
            self.title = title_info[0].text_content().strip()

    def set_abstract(self):
        abstract_info = self.page.cssselect('div#articleDetails div.article p')
        if len(abstract_info) > 0:
            self.abstract = abstract_info[0].text_content().strip()

    def set_journal_and_year(self):
        paragraphs = self.page.cssselect('div#articleDetails div.article-ftr > p')
        if len(paragraphs) > 0:
            self.journal = paragraphs[0].cssselect('a')[0].text.strip()

            year_group = re.search(self.YEAR_PATTERN, paragraphs[1].text_content())
            if year_group is None:
                article_info = self.page.cssselect('div#articleDetails div.article-ftr .article-info dl')
                year_info = article_info[1][1].text_content()
                year_group = re.search(self.YEAR_PATTERN, year_info)

        else:
            article_info = self.page.cssselect('div#articleDetails div.article-ftr .article-info dl')
            year_info = article_info[0][-1].text_content()
            year_group = re.search(self.YEAR_PATTERN, year_info)

        if year_group is None:
            print "Year absent for article %s" % self.url
        else:
            y = int(year_group.group(1))
            if y >= 1970 and y <= 2014:
                self.year = y

    def set_authors(self):
        authors_elems = self.page.cssselect('div#abstractAuthors a')
        self.authors = map(lambda el: el.text_content().strip(), authors_elems)

    def set_keywords(self):
        keywords_elems = self.page.cssselect('div#abstractKeywords a')
        self.keywords = uniq(map(lambda el: el.text_content().strip().lower(),
                                 keywords_elems))

