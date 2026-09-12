import os
from datetime import datetime

class Logger:
    def __init__(self, verbose=False, output_dir="output/"):
        self.verbose = verbose
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.logfile = os.path.join(output_dir, f"sqlPrivate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    def _write(self, level, msg):
        line = f"[{datetime.now().strftime('%H:%M:%S')}] [{level}] {msg}"
        print(line)
        with open(self.logfile, "a") as f:
            f.write(line + "\n")

    def info(self, msg):
        self._write("INFO", msg)

    def success(self, msg):
        self._write("OK", msg)

    def warn(self, msg):
        self._write("WARN", msg)

    def error(self, msg):
        self._write("ERR", msg)
