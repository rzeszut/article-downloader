#! venv/bin/python

import models
import vls2
import ieee
import patent

models.setup_db()

# vls2.download_articles({
#     'query': 'mapreduce',
#     'num': 300
# })

ieee.download_articles({
    'query': 'big data',
    'pages': 7,
    'start-page': 14
})

#patent.download_patents({
#    'query-abstract-or-title': 'hadoop',
#    'pages': 5
#})

