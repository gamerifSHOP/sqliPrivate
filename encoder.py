import base64
import urllib.parse

class Encoder:
    @staticmethod
    def url(s):
        return urllib.parse.quote(s)

    @staticmethod
    def double_url(s):
        return urllib.parse.quote(urllib.parse.quote(s))

    @staticmethod
    def hex(s):
        return "0x" + s.encode().hex()

    @staticmethod
    def base64(s):
        return base64.b64encode(s.encode()).decode()
