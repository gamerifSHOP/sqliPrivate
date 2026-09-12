import re
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, base, req, logger, max_pages=30):
        self.base = base
        self.req = req
        self.logger = logger
        self.max_pages = max_p
