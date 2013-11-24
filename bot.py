#! venv/bin/python

import models
import vls2
import patent

models.setup_db()

# vls2.download_articles({
#     'query': 'mapreduce',
#     'num': 300
# })

patent.download_patents({
    'query-abstract-or-title': 'big data',
    'pages': 20
})

