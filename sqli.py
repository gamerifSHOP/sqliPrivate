#!/usr/bin/env python3
import sys
import argparse
from core.engine import Engine
from utils.logger import Logger

BANNER = r"""
  ___  ___  _    ___      _    _
 / __|/ _ \| |  | _ \_ _(_)__| |_  ___
 \__ \ (_) | |__|  _/ '_| / _| | || -_)
 |___/\__\_\____|_| |_| |_\__|_|\_,_\___|
            sqlPrivate Tools 2026
            Developer: gamerif404
            t.me /@bellImupss
"""

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="sqlPrivate - Auto SQLi + Vuln Scanner")
    parser.add_argument("-u", "--url", help="Target URL")
    parser.add_argument("-l", "--list", help="File berisi daftar target")
    parser.add_argument("--method", default="GET", choices=["GET", "POST"])
    parser.add_argument("--data", help="POST data")
    parser.add_argument("--cookie", help="Cookie")
    parser.add_argument("--headers", help="Custom headers")
    parser.add_argument("--proxy", help="Proxy")

    parser.add_argument("--profile", default="normal",
                        choices=["slow", "normal", "fast", "insane", "stealth"],
                        help="Preset kecepatan")
    parser.add_argument("--delay", type=float, help="Jeda per request (detik)")
    parser.add_argument("--threads", type=int, help="Jumlah thread paralel")
    parser.add_argument("--timeout", type=int, help="Timeout request (detik)")
    parser.add_argument("--rate", type=float, help="Request per detik (0=tanpa limit)")
    parser.add_argument("--burst", type=int, help="Jumlah request sebelum jeda")

    parser.add_argument("--random-agent", action="store_true")
    parser.add_argument("--waf-bypass", action="store_true")
    parser.add_argument("--tamper", help="Tamper script")
    parser.add_argument("--crawl", action="store_true")
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--dbs", action="store_true")
    parser.add_argument("--tables", action="store_true")
    parser.add_argument("--columns", help="Columns of table")
    parser.add_argument("--dump", help="Dump table")
    parser.add_argument("--os-shell", action="store_true")
    parser.add_argument("--crack", help="Crack hash (md5/sha1/sha256)")
    parser.add_argument("--output", default="output/")
    parser.add_argument("--report", default="txt", choices=["txt", "json", "html"])
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    if not args.url and not args.list and not args.crack:
        print("[!] Butuh -u URL, -l list.txt, atau --crack HASH")
        sys.exit(1)

    logger = Logger(verbose=args.verbose, output_dir=args.output)
    engine = Engine(args, logger)
    engine.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Dihentikan user")
        sys.exit(0)
