#! venv/bin/python

import pages
import models
import convert
import url

models.setup_db()
session = models.Session()

u = url.prepare_url({
    'query': 'big data',
    'num': 1500,
    'start': 501
})
print "Getting %s ..." % u
search_page = pages.SearchPage(u)

i = 1
for l in search_page.links:
    print "%d: Getting %s ..." % (i, l)
    article_page = pages.BibliographicPage(l)
    db_page = convert.convert_article(article_page)
    session.add(db_page)
    i = i + 1
    if i % 100 == 0:
        session.commit()
        print "Saved %d records." % i

session.commit()
print "Saved."

