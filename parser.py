from urllib.parse import urlparse, parse_qs, urlencode

class Parser:
    def __init__(self, url):
        self.url = url
        self.parsed = urlparse(url)
        self.params = parse_qs(self.parsed.query)

    def get_params(self):
        return list(self.params.keys())

    def build(self, param, value):
        new_params = self.params.copy()
        new_params[param] = [value]
        return f"{self.parsed.scheme}://{self.parsed.netloc}{self.parsed.path}?{urlencode(new_params, doseq=True)}"
