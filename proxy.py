
import requests
import os
import requests

from support import supply
from selenium.webdriver.common.by import By
import random,time
supply = supply()
db,connect = supply.connectSQL(10, 'faretrack') 
proxyid = '28'
connect.execute(f"Select proxy from proxy_live where status in ({proxyid})")
resultset = connect.fetchall()
proxy = supply.proxy_refreshed(resultset[random.randrange(0, len(resultset))][0])

proxis  = {'http':'socks5h://'+str(proxy)} if proxy else None

print(proxis)

proxis  = {'https':'socks5h://'+str(proxy)} if proxy else None

ses = requests.Session()
ses.proxies =proxis


response = ses.get('http://api4.ipify.org/?format=json')
print(response.text)

#============================================== NEXT ===================================

os.environ["http_proxy"] = f"http://{proxy}"
os.environ["https_proxy"] = f"https://{proxy}"

response = requests.get("http://api4.ipify.org/?format=json")
print(response.text)

#============================================== NEXT ===================================


os.environ["http_proxy"] = f"socks5://{proxy}"
os.environ["https_proxy"] = f"socks5://{proxy}"

response = requests.get("http://api4.ipify.org/?format=json")
print(response.text)