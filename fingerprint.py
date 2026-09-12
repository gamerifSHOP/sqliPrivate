class Fingerprint:
    def __init__(self, req, parser, logger):
        self.req = req
        self.parser = parser
        self.logger = logger

    def detect(self):
        tests = {
            "mysql": ["'", "\"", "')", "';", " AND 1=1", " AND 1=2"],
            "postgresql": ["'", "\"", "')", "';", " AND 1=1"],
            "mssql": ["'", "\"", "')", "';", " AND 1=1"],
            "oracle": ["'", "\"", "')", "';", " AND 1=1"],
        }
        for dbms, payloads in tests.items():
            for p in payloads:
                resp = self.req.get_text(p)
                if self._match(dbms, resp):
                    return dbms
        return "unknown"

    def _match(self, dbms, text):
        if not text:
            return False
        sigs = {
            "mysql": ["You have an error in your SQL syntax", "MySQL", "MariaDB"],
            "postgresql": ["PostgreSQL", "pg_query", "PG::SyntaxError"],
            "mssql": ["Microsoft SQL Server", "ODBC SQL Server", "Unclosed quotation mark"],
            "oracle": ["ORA-", "Oracle", "quoted string not properly terminated"],
        }
        return any(s.lower() in text.lower() for s in sigs.get(dbms, []))
