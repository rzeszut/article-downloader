from os.path import join, abspath, dirname

USE_PROXY = True
PROXY_ADDRESS = 'socks5://127.0.0.1:12345'

basedir = abspath(dirname(__file__))
DATABASE_URL = 'sqlite:///' + join(basedir, 'articles.db')

