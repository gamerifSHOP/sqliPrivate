class Tamper:
    def __init__(self, logger):
        self.logger = logger

    def space2comment(self, payload):
        return payload.replace(" ", "/**/")

    def randomcase(self, payload):
        import random
        return "".join(c.upper() if random.random() > 0.5 else c.lower() for c in payload)

    def charencode(self, payload):
        return "".join(f"%{ord(c):02x}" for c in payload)
