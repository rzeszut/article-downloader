import models

import url
import pages
import article_convert as convert

def download_articles(parameters):
    session = models.Session()
    urls = url.prepare_urls(parameters)
    i = 1
    if 'start-page' in parameters:
        page = parameters['start-page']
    else:
        page = 1

    for u in urls:
        print "Getting page %d: %s ..." % (page, u)
        search_page = pages.SearchPage(u)

        for l in search_page.links:
            print "%d: Getting %s ..." % (i, l)
            article_page = pages.ArticlePage(l)
            db_article = convert.convert_article(article_page)
            session.add(db_article)
            i = i + 1

        session.commit()
        print "Saved %d records; page %d finished." % (i, page)
        page = page + 1

    session.commit()
    print "Saved."

