from os.path import join, abspath, dirname

basedir = abspath(dirname(__file__))

PROXY_ADDRESS = 'socks5://127.0.0.1:12345'
DATABASE_URL = 'sqlite:///' + join(basedir, 'articles.db')
