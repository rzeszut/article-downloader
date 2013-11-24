import models

import url
import pages
import convert

def download_articles(parameters):
    session = models.Session()
    u = url.prepare_url(parameters)

    print "Getting %s ..." % u
    search_page = pages.SearchPage(u)

    i = 1
    for l in search_page.links:
        print "%d: Getting %s ..." % (i, l)
        article_page = pages.BibliographicPage(l)
        db_article = convert.convert_article(article_page)
        session.add(db_article)

        if i % 100 == 0:
            session.commit()
            print "Saved %d records." % i
        i = i + 1

    session.commit()
    print "Saved."

