class WAFDetect:
    def __init__(self, req, logger):
        self.req = req
        self.logger = logger

    def detect(self):
        r = self.req.send("' AND 1=1-- -")
        if not r:
            return "unknown"
        headers = {k.lower(): v for k, v in r.headers.items()}
        wafs = {
            "cloudflare": ["cf-ray", "cf-cache-status"],
            "sucuri": ["x-sucuri-id", "x-sucuri-cache"],
            "wordfence": ["wordfence"],
            "akamai": ["x-akamai-transformed"],
            "incapsula": ["x-iinfo", "incap_ses"],
            "f5": ["x-wa-info", "bigip"],
            "barracuda": ["barra_counter_session"],
            "modsecurity": ["mod_security", "modsecurity"],
        }
        found = []
        for name, sigs in wafs.items():
            for sig in sigs:
                if sig in str(headers) or sig in r.text.lower():
                    found.append(name)
        if found:
            self.logger.warn(f"WAF terdeteksi: {set(found)}")
            return list(set(found))
        self.logger.info("Tidak ada WAF terdeteksi")
        return []
