#! venv/bin/python

import pages
import models
import convert
import url

models.setup_db()
session = models.Session()

u = url.prepare_url({
    'query': 'big data',
    'num': 500
})
print "Getting %s ..." % u
search_page = pages.SearchPage(u)

for l in search_page.links:
    print "Getting %s ..." % l
    article_page = pages.BibliographicPage(l)
    db_page = convert.convert_article(article_page)
    session.add(db_page)

session.commit()
print "Saved."

