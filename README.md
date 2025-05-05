# 🔐 SQL Injection Exploit — Smart Settlements 360 Demo

## 📌 Description
A simulated SQL injection attack on a login form in a Flask app used in a smart settlements dashboard.

## 🚀 Exploit Steps
1. Sent malicious input via form POST:
   - Username: `' OR '1'='1`
   - Password: `' OR '1'='1`
2. Server interprets query as always true
3. Attacker bypasses authentication

## 💣 Impact
Unauthorized access to admin dashboard or sensitive data.

## 🧰 Tools Used
- Flask
- Python Requests

## ✅ Fix
Update vulnerable query:
```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
