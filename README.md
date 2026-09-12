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
