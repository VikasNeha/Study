import requests

r = requests.get("http://fiverr.com/login")
print r.text
print r.headers
print r.history