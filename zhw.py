#租号玩自动上线下线擦亮卖家出租号
import requests
import os
import time

def offRent():
    url = 'https://www.zuhaowan.com/Account/offRent.html'
    cookie = os.environ['ZuHaoWan']
    headers = {
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': cookie
    }
    res = requests.post(url=url, headers=headers, data='id=10284948&accountsign=')
    print(res.json().get('message'))

def onRent():
    url = 'https://www.zuhaowan.com/Account/onRent.html'
    cookie = os.environ['ZuHaoWan']
    headers = {
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': cookie
    }
    res = requests.post(url=url, headers=headers, data='id=10284948&accountsign=')
    print(res.json().get('message'))


if __name__ == '__main__':
    offRent()
    time.sleep(2)
    onRent()
    #sold_out()
