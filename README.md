# sqlPrivate

Tools SQL injection overpowered untuk Termux.
Developer: **gamerif404**

## Fitur

- Auto detect DBMS (MySQL, PostgreSQL, MSSQL, Oracle)
- Auto detect parameter (URL + HTML)
- Auto pilih modul berdasarkan fingerprint
- Crawl website cari parameter
- Modul: error-based, union, boolean, time, stacked, OOB
- Auto upload shell (kalau FILE privilege)
- WAF detect + bypass
- Crack hash (MD5, SHA1, SHA256, bcrypt)
- Report (txt, json, html)
- Kontrol kecepatan: profile, delay, threads, rate, burst
- Random User-Agent + header rotasi

## Install

```bash
chmod +x setup.sh
./setup.sh

# scan single target auto
python sqli.py -u "https://target.com/page.php?id=1" --auto

# crawl + auto
python sqli.py -u "https://target.com" --crawl --auto

# scan massal dari file
python sqli.py -l targets.txt --auto --threads 20

# dump database
python sqli.py -u "URL" --dbs
python sqli.py -u "URL" --tables
python sqli.py -u "URL" --dump users

# os shell
python sqli.py -u "URL" --os-shell

# crack hash
python sqli.py --crack 5f4dcc3b5aa765d61d8327deb882cf99
