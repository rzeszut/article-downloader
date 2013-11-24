import requesocks as r
import lxml.html as html

import config

session = r.session()
if config.USE_PROXY:
    session.proxies = {
        'http': config.PROXY_ADDRESS,
        'https': config.PROXY_ADDRESS
    }

def get_page(url):
    global session
    resp = session.get(url)
    dom = html.fromstring(resp.text)
    dom.make_links_absolute(url)
    return dom

