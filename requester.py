import requests
import random
import time
from utils.throttle import Throttle

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
]

ACCEPT_LANGS = ["en-US,en;q=0.9", "en-GB,en;q=0.9", "id-ID,id;q=0.9,en;q=0.8"]
REFERERS = ["https://www.google.com/", "https://www.bing.com/", "https://duckduckgo.com/"]

class Requester:
    def __init__(self, args, logger):
        self.args = args
        self.logger = logger
        self.session = requests.Session()
        self.session.verify = False
        requests.packages.urllib3.disable_warnings()
        self.throttle = Throttle(args, logger)
        self._setup_static_headers()

    def _setup_static_headers(self):
        if self.args.cookie:
            self.session.headers.update({"Cookie": self.args.cookie})
        if self.args.headers:
            for h in self.args.headers.split(";"):
                if ":" in h:
                    k, v = h.split(":", 1)
                    self.session.headers.update({k.strip(): v.strip()})

    def _random_headers(self):
        if not self.args.random_agent:
            return {}
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": random.choice(ACCEPT_LANGS),
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": random.choice(["keep-alive", "close"]),
            "Referer": random.choice(REFERERS),
            "DNT": random.choice(["1", "0"]),
        }

    def send(self, payload=None):
        self.throttle.wait()
        url = self.args.url
        if payload:
            url = url + payload if "?" in url else url + "?" + payload
        proxies = {"http": self.args.proxy, "https": self.args.proxy} if self.args.proxy else None
        headers = self._random_headers()
        try:
            if self.args.method == "POST":
                data = (self.args.data or "") + (payload or "")
                return self.session.post(url, data=data, headers=headers, proxies=proxies,
                                         timeout=self.throttle.timeout, allow_redirects=False)
            return self.session.get(url, headers=headers, proxies=proxies,
                                    timeout=self.throttle.timeout, allow_redirects=False)
        except requests.exceptions.Timeout:
            self.logger.warn("Timeout")
            return None
        except requests.exceptions.ConnectionError:
            self.logger.warn("Koneksi error")
            return None
        except Exception as e:
            self.logger.error(f"Request error: {e}")
            return None

    def get_text(self, payload=None):
        r = self.send(payload)
        return r.text if r else ""

    def get_text_url(self, url):
        self.throttle.wait()
        try:
            r = self.session.get(url, headers=self._random_headers(),
                                 timeout=self.throttle.timeout, allow_redirects=False)
            return r.text
        except Exception:
            return ""

    def get_status(self, payload=None):
        r = self.send(payload)
        return r.status_code if r else 0

    def get_time(self, payload=None):
        start = time.time()
        self.send(payload)
        return time.time() - start
