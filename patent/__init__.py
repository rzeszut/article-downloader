import models

import url
import pages
import convert

def download_patents(parameters):
    session = models.Session()
    urls = url.prepare_urls(parameters)
    i = 1

    for u in urls:
        print "Getting %s ..." % u
        search_page = pages.SearchPage(u)

        for l in search_page.links:
            print "%d: Getting %s ..." % (i, l)
            patent_page = pages.PatentPage(l)
            db_patent = convert.convert_patent(patent_page)
            session.add(db_patent)

            if i % 100 == 0:
                session.commit()
                print "Saved %d records." % i
            i = i + 1

    session.commit()
    print "Saved."

