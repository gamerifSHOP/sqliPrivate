#!/data/data/com.termux/files/usr/bin/bash
# sqlPrivate installer
# Developer: gamerif404

echo "[*] Install sqlPrivate..."
pkg update -y
pkg install -y python git
pip install --upgrade pip
pip install -r requirements.txt
chmod +x sqli.py
echo "[+] Selesai."
echo "[+] Jalankan: python sqli.py -u TARGET --auto"
