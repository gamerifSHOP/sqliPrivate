class WAFBypass:
    def __init__(self, logger):
        self.logger = logger

    def bypass(self, payload):
        p = payload.replace(" ", "/**/")
        p = p.replace("UNION", "UnIoN").replace("SELECT", "SeLeCt")
        p = p.replace("'", "%27")
        return p
