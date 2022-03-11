import requests, re, threading
from os import system

#Coded By yusiqo
#Şifresiz Tool
#Çalmayin Ule

system("title " + f"TeleView By @ZetTekno / @yusiqo")
print('''
   _____     _            _               
  /__   \___| | ___/\   /(_) _____      __
    / /\/ _ \ |/ _ \ \ / / |/ _ \ \ /\ / /
   / / |  __/ |  __/\ V /| |  __/\ V  V / 
   \/   \___|_|\___| \_/ |_|\___| \_/\_/  
         By: [  @yusiqo / @yu5uy ]                         

''')
_proxy_file = input(' [/] Proxy Dosya ismi Gir Örnek: [ proxy.txt ]: ')
link = input(' [/] Post Linkini Gir: ').strip().replace('https://', '').replace('http://', '')
_threads = int(input(' [/] Kaç Botla Çalıştırılsın: '))
#Galiba bişeyleri kurcalion
print(' [?] Fazla Bot Seçtiniz, Eminmisiniz?  ' if _threads > 400 else '')
if _threads > 400: '' if input(' - Are you sure you want to skip [y/N]: ').strip().lower() == 'y' else exit()

main_url = f'https://{link}?embed=1'
views_url = 'https://t.me/v/?views='

proxies_file = open(str(_proxy_file), 'r').read()
proxies = proxies_file.splitlines()
count_proxies = len(proxies)
sent, bad_proxy, done, next_proxy = 0, 0, 0, 0

_headers = {
  'accept-language': 'en-US,en;q=0.9',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}


def tit(): system("title " + f"TeleView By @ZetTekno / @yusiqo -- Statika: ({done}/{count_proxies}) -- Gönderildi: {sent} -- Hatalı proxy: {bad_proxy}")

#lan ne bakion ne :D
def send_views():
    global sent, bad_proxy, done, next_proxy
    while True:
        try:
            proxy = proxies[next_proxy]
            next_proxy += 1
        except IndexError:
            break
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update(_headers)
            main_res = session.get(main_url).text
            _token = re.search('izlenme Datası="([^"]+)', main_res).group(1)
            views_req = session.get(views_url + _token)
            print(' [+] izlenme Gönderildi ' + 'Statistik Kodu: '+str(views_req.status_code))
            sent += 1
            done += 1
            tit()
#Fazla inion .d
        except requests.exceptions.ConnectionError:
            print(' [x] Hatalı Proxy: ' + proxy)
            bad_proxy += 1
            done += 1
            tit()

#şuna bak ya zzzzzz
Threads = []
for t in range(_threads):
    x = threading.Thread(target=send_views)
    x.start()
    Threads.append(x)

for Th in Threads:
    Th.join()
#Nasıl sistem ama
