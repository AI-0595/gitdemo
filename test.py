

from support import supply
import random,time
supply = supply()
db,connect = supply.connectSQL(11, 'faretrack') 
proxyid = '28'
connect.execute(f"Select proxy from proxy_live where status in ({proxyid})")
resultset = connect.fetchall()
proxy = supply.proxy_refreshed(resultset[random.randrange(0, len(resultset))][0])

from undetected_chromedriver import Chrome, ChromeOptions
import requests,pyautogui,tempfile,shutil,socket

def create_new_profile():
    temp_dir = tempfile.mkdtemp(prefix='chrome_profile_')
    return temp_dir

def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 0))
        return s.getsockname()[1]

# proxy_split = proxy.split('@')

if '@' in str(proxy):
    credentials, host_port = proxy.split('@')
    proxy_user, proxy_pass = credentials.split(':')
    proxy_host_port = f'http://{host_port}'
else:
    proxy_host_port = proxy
    proxy_user = proxy_pass = ''

options = ChromeOptions()
options.add_argument(f'--proxy-server={proxy_host_port}')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
if random.choice([True,False]):
    options.add_argument('--incognito')
new_profile_dir = create_new_profile()
new_port = find_available_port()
options.add_argument(f'--user-data-dir={new_profile_dir}')
options.add_argument(f'--remote-debugging-port={new_port}')

try:
    driver = Chrome(options=options,version_main= 114)
    domain_url='https://www.goindigo.in/'
    driver.get(domain_url)
    time.sleep(3)
    if proxy_user:
        time.sleep(3)
        print(proxy_user)
        print(proxy_pass)
        pyautogui.click()
        pyautogui.click()
        pyautogui.typewrite(proxy_user)
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(proxy_pass)
        pyautogui.typewrite(['enter'])
    time.sleep(10)
    cok=driver.get_cookies()
    print(cok)

except Exception as e:
    print("Error:", e)
finally:
    if 'driver' in locals():
        driver.quit()
    if new_profile_dir:
        shutil.rmtree(new_profile_dir, ignore_errors=True)


