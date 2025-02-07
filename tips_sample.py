import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

response = http.request("GET", "https://www.expedia.com/", headers={"User-Agent": "Mozilla/5.0"})

prin = response.headers.get("Set-Cookie")
print(prin)



