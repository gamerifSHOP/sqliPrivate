class OOB:
    def __init__(self, req, parser, logger, args):
        self.req = req
        self.parser = parser
        self.logger = logger
        self.args = args

    def run(self):
        self.logger.info("OOB butuh server listener. Lewati dulu.")
