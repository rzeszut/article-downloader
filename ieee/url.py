from urllib import quote

DEFAULT_VALUES = {
    'query': '',
    'pages': 1,
    'start-page': 1,
    'from': 1995,
    'to': 2014
}

def prepare_urls(values):
    vals = DEFAULT_VALUES.copy()
    vals.update(values)
    vals['query'] = quote('(' + vals['query'] + ')')
    return [prepare_page_url(vals, p) for p in range(vals['pages'])]

def prepare_page_url(values, page):
    vals = values.copy()
    vals['page'] = page + vals['start-page']
    return ('http://ieeexplore.ieee.org/search/searchresult.jsp?action=search' +\
        '&sortType=' +\
        '&rowsPerPage=100' +\
        '&pageNumber=%(page)d' +\
        '&searchField=Search_All' +\
        '&matchBoolean=true' +\
        '&queryText=%(query)s' +\
        '&addRange=%(from)d_%(to)d_Publication_Year') % vals

