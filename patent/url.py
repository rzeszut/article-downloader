from urllib import quote_plus

DEFAULT_VALUES = {
# Search only in patent title
    'query-title': '',
# Search in title and abstract
    'query-abstract-or-title': '',
# Number of pages to load, min 1 (page has 25 patents)
    'pages': 1,
    'from': 1995,
    'to': 2014
}

def prepare_urls(values):
    vals = DEFAULT_VALUES.copy()
    vals.update(values)
    vals['query-title'] = quote_plus(vals['query-title'])
    vals['query-abstract-or-title'] = quote_plus(vals['query-abstract-or-title'])
    return [prepare_page_url(vals, p) for p in range(vals['pages'])]

def prepare_page_url(values, page):
    vals = values.copy()
    vals['page'] = page
    return ('http://worldwide.espacenet.com/searchResults?compact=false' +
            '&page=%(page)d' +
            '&AB=%(query-abstract-or-title)s' +
            '&TI=%(query-title)s' +
            '&PD=%(from)d:%(to)d' +
            '&ST=advanced' +
            '&locale=en_EP' +
            '&DB=EPODOC') % vals

