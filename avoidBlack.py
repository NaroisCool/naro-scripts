from requests import get, post, put, packages
import requests
from re import findall
from os.path import exists
import json
import os
import sys,re
import random,time
import base64
import hashlib
import urllib.parse
import uuid

packages.urllib3.disable_warnings()
from urllib.parse import unquote
"""
防黑代理脚本工具，改编自lonesomexz大神
"""
hadsend=True
UserAgent=""
Proxy=""

def printf(text):
    print(text)
    sys.stdout.flush()

def randomuserAgent():
    global struuid,addressid,iosVer,iosV,clientVersion,iPhone,area,ADID,lng,lat
    global UserAgent
    struuid=''.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','a','b','c','z'], 40))
    addressid = ''.join(random.sample('1234567898647', 10))
    iosVer = ''.join(random.sample(["15.1.1","14.5.1", "14.4", "14.3", "14.2", "14.1", "14.0.1"], 1))
    iosV = iosVer.replace('.', '_')
    clientVersion=''.join(random.sample(["10.3.0", "10.2.7", "10.2.4"], 1))
    iPhone = ''.join(random.sample(["8", "9", "10", "11", "12", "13"], 1))
    area=''.join(random.sample('0123456789', 2)) + '_' + ''.join(random.sample('0123456789', 4)) + '_' + ''.join(random.sample('0123456789', 5)) + '_' + ''.join(random.sample('0123456789', 5))
    ADID = ''.join(random.sample('0987654321ABCDEF', 8)) + '-' + ''.join(random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 4)) + '-' + ''.join(random.sample('0987654321ABCDEF', 12))
    lng='119.31991256596'+str(random.randint(100,999))
    lat='26.1187118976'+str(random.randint(100,999))
    UserAgent=f'jdapp;iPhone;10.0.4;{iosVer};{uuid};network/wifi;ADID/{ADID};model/iPhone{iPhone},1;addressid/{addressid};appBuild/167707;jdSupportDarkMode/0;Mozilla/5.0 (iPhone; CPU iPhone OS {iosV} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/null;supportJDSHWK/1'


def get_proxy_api(proxy_url, max_retries=5, timeout=60, retry_delay=1):
    for retry in range(max_retries):
        res = get(url=proxy_url)
        printf(f"本次获取到的代理：{res.text}")
        proxy_ip_port = res.text.strip()
        proxy_address = f"http://{proxy_ip_port}"

        try:
            response = get("https://jd.com", proxies={"http": proxy_address, "https": proxy_address}, timeout=timeout)
            if response.status_code == 200:
                print(proxy_address+"  此代理可用")
                return proxy_address
        except Exception as e:
            printf(f"代理检测失败，错误信息：{e}")

        printf("代理检测失败，重新获取...")
        time.sleep(retry_delay)
    
    printf("无法获取可用的代理IP，尝试次数已达上限。")
    return None

def main():
    printf("版本: 20240102")
    printf("隧道型代理池接口:export WSKEY_PROXY_TUNNRL='http://127.0.0.1:123456'")
    printf("拉取型代理API接口(数据格式:txt;提取数量:每次一个):export WSKEY_PROXY_URL='http://xxx.com/apiUrl'")
    printf("没有代理可以自行注册，比如携趣，巨量，每日免费1000IP，完全够用")
    printf("====================================")
    global proxy_url
    proxy_url=os.environ.get("WSKEY_PROXY_URL") or os.environ.get("WSKEY_PROXY_TUNNRL") or None
    print(proxy_url)
    global Proxy 
    Proxy = get_proxy_api(proxy_url)
    print("请用这个代理>> "+Proxy)

if __name__ == '__main__':    
    main()
