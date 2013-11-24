from urllib import quote_plus

DEFAULT_VALUES = {
# any string
    'query': '',
# Any, Title, Abstract, Author, issn, PII, Keyword, JournalTitle
    'query-fields': 'Any',
# AND, OR, NOT
    'query-join': 'AND',
# any string
    'query2': '',
# Any, Title, Abstract, Author, issn, PII, Keyword, JournalTitle
    'query2-fields': 'Any',
# min 1990
    'from': 1995,
# max 2014
    'to': 2014,
# min 1
    'num': 100,
# min 1
    'start': 1
}

def prepare_url(values):
    vals = DEFAULT_VALUES.copy()
    vals.update(values)
    vals['query'] = quote_plus(vals['query'])
    vals['query2'] = quote_plus(vals['query2'])
    return ('http://vls2.icm.edu.pl/cgi-bin/search.pl?SearchTemplate=search_form.advanced' +
            '&search_field=%(query)s' +
            '&fields=%(query-fields)s' +
            '&AdvBooleanJoiner=%(query-join)s' +
            '&search_field2=%(query2)s' +
            '&fields2=%(query2-fields)s' +
            '&Database=elsevier_1990' +
            '&Database=springer_1990' +
            '&Category=all_categories' +
            '&ArticleType=All+Types...' +
            '&Language=' +
            '&daterange=yearrange' +
            '&fromyear=%(from)d' +
            '&toyear=%(to)d' +
            '&Max=%(num)d' +
            '&Start=%(start)d' +
            '&Order=' +
            '&GetSearchResults=Submit+Query') % vals

