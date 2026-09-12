from concurrent.futures import ThreadPoolExecutor, as_completed
from core.requester import Requester
from core.fingerprint import Fingerprint
from core.auto_exploit import AutoExploit
from modules.error_based import ErrorBased
from modules.union_based import UnionBased
from modules.boolean_based import BooleanBased
from modules.time_based import TimeBased
from modules.stacked import Stacked
from modules.oob import OOB
from modules.os_shell import OSShell
from utils.parser import Parser
from utils.crawler import Crawler
from utils.reporter import Reporter
from config.settings import TOOLS_NAME, DEVELOPER, VERSION

class Engine:
    def __init__(self, args, logger):
        self.args = args
        self.logger = logger
        self.req = Requester(args, logger)
        self.parser = Parser(args.url) if args.url else None
        self.reporter = Reporter(args.output, args.report)

    def scan_one(self, target):
        self.logger.info(f"=== Target: {target} ===")
        self.parser = Parser(target)

        if self.args.crawl:
            c = Crawler(target, self.req, self.logger)
            params = c.crawl()
            self.logger.info(f"Parameter: {params}")

        self.fp = Fingerprint(self.req, self.parser, self.logger)
        dbms = self.fp.detect()
        self.logger.info(f"DBMS: {dbms}")

        if self.args.auto:
            ae = AutoExploit(self.req, self.parser, self.logger, self.args)
            results = ae.detect()
            mods = ae.pick(results)
            self.logger.success(f"Modul work: {mods}")
            self.reporter.add(target, "modules", mods)

        if dbms == "mysql":
            mods = [ErrorBased, UnionBased, BooleanBased, TimeBased, Stacked, OOB, OSShell]
        elif dbms == "postgresql":
            mods = [ErrorBased, UnionBased, BooleanBased, TimeBased, Stacked, OSShell]
        elif dbms == "mssql":
            mods = [ErrorBased, UnionBased, BooleanBased, TimeBased, Stacked, OSShell]
        elif dbms == "oracle":
            mods = [ErrorBased, UnionBased, BooleanBased, TimeBased, OOB]
        else:
            mods = [ErrorBased, UnionBased, BooleanBased, TimeBased]

        for mod in mods:
            try:
                self.logger.info(f"Menjalankan {mod.__name__}")
                m = mod(self.req, self.parser, self.logger, self.args)
                m.run()
            except Exception as e:
                self.logger.error(f"{mod.__name__} gagal: {e}")

    def run(self):
        self.logger.info(f"{TOOLS_NAME} v{VERSION} by {DEVELOPER}")

        if self.args.crack:
            from db.cracker import Cracker
            Cracker(self.logger).crack(self.args.crack)
            return

        targets = []
        if self.args.list:
            with open(self.args.list) as f:
                targets = [l.strip() for l in f if l.strip()]
        else:
            targets = [self.args.url]

        threads = self.req.throttle.threads
        self.logger.info(f"Threads: {threads}")

        if threads > 1:
            with ThreadPoolExecutor(max_workers=threads) as ex:
                futures = {ex.submit(self.scan_one, t): t for t in targets}
                for fut in as_completed(futures):
                    try:
                        fut.result()
                    except Exception as e:
                        self.logger.error(f"Target gagal: {e}")
        else:
            for t in targets:
                self.scan_one(t)

        self.reporter.save()
        self.logger.info("Selesai")
