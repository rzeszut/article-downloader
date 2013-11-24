import re
import datetime

import connection as con

class SearchPage:
    def __init__(self, url):
        self.url = url
        self.page = con.get_page(url)
        self.initialize()

    def initialize(self):
        link_elems = self.page.cssselect('a.publicationLinkClass')
        self.links = map(lambda l: l.attrib['href'], link_elems)

class PatentPage:
    DATE_PATTERN = re.compile('(\d{4})-(\d{2})-(\d{2})')

    def __init__(self, url):
        self.url = url
        self.page = con.get_page(url)
        self.initialize()

    @staticmethod
    def strip_string(s):
        return s.strip()

    def initialize(self):
        rows = self.page.cssselect('table.tableType3 > tbody > tr')[2:]
        self.set_name()
        self.set_date()
        self.set_inventors(rows[0][1])
        self.set_applicants(rows[1][1])
        self.set_classification(rows[2][1])
        self.set_application_number(rows[3][1])
        self.set_priority_number(rows[4][1])
        self.set_abstract()

    def set_name(self):
        self.name = self.page.cssselect('#pagebody > h3')[0].text_content().strip()

    def set_date(self):
        date_text = self.page.cssselect('#pagebody > h1')[0].text
        date_match = re.search(self.DATE_PATTERN, date_text)
        y, m, d = date_match.groups()
        self.date = datetime.date(int(y), int(m), int(d))

    def set_inventors(self, td):
        self.inventors = map(self.strip_string, td.text.split(';'))

    def set_applicants(self, td):
        self.applicants = map(self.strip_string, td.text.split(';'))

    def set_classification(self, td):
        cls_rows = td[0][0].getchildren()
        self.international_classification = map(self.strip_string,
                                                cls_rows[0][1].text_content().split(';'))
        self.cooperative_classification = map(self.strip_string,
                                              cls_rows[1][1].text_content().split(';'))

    def set_application_number(self, td):
        self.application_number = td.text_content().strip()

    def set_priority_number(self, td):
        self.priority_number = td.text_content().strip()

    def set_abstract(self):
        self.abstract = self.page.cssselect('p.printAbstract')[0].text_content().strip()

