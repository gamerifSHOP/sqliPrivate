import re
from urllib.parse import urlparse, parse_qs

class AutoParam:
    def __init__(self, url, req, logger):
        self.url = url
        self.req = req
        self.logger = logger

    def from_url(self):
        p = urlparse(self.url)
        return list(parse_qs(p.query).keys())

    def from_html(self):
        html = self.req.get_text()
        params = set()
        for m in re.finditer(r'<input[^>]+name=["\']([^"\']+)["\']', html, re.I):
            params.add(m.group(1))
        for m in re.finditer(r'href=["\']([^"\']+\?[^"\']+)["\']', html, re.I):
            q = urlparse(m.group(1)).query
            for k in parse_qs(q).keys():
                params.add(k)
        return list(params)

    def all(self):
        p = set(self.from_url()) | set(self.from_html())
        self.logger.info(f"Parameter: {list(p)}")
        return list(p)
