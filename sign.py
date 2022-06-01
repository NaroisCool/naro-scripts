import requests
from notify import send 
from notify import NOW

if __name__ == '__main__':
    urls = 'http://ehr.thinvent.com:16666/Web.HR//Mobile/AppSign/userSignData?r=0.9782261866256824'
    # m = MultipartEncoder(fields={'upload': open('test.txt', 'rb')},
    #                      boundary='----WebKitFormBoundaryaSp5ER0SytDjXKd1')

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        "Content-type": "multipart/form-data, boundary=----WebKitFormBoundaryaSp5ER0SytDjXKd1",
        'Origin': 'http://ehr.thinvent.com:16666',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)  Mobile/15E148 wxwork/4.0.3 MicroMessenger/7.0.1 Language/zh ColorScheme/Dark',
        'Connection': 'keep-alive',
        'Referer': 'http://ehr.thinvent.com:16666/Web.HR/Mobile/sign/signgaode.html?r=0.6025903886577239',
        'Content-Length': '1101',
        'Cookie': 'ASP.NET_SessionId=ot3g0030okenzk4wu4omkddk; .ASPXAUTH=C80CE50968C1A77DADC4E005858583F01F969973B0FA949CC11DE86A818D0CB8AD1B7FBAE4441E9C6346EBDA06760D307719F239D691FA9A999767DEECF8B80DFDDEA8AEE823FEBBEB7A02E9412ADD1E43F1773A5DBA95391AEFC9E2ACDBACEC'

    }
    payload = '------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="a0188"\r\n\r\n6248\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="CARD_TIME"\r\n\r\n2022-05-12 08:25:47\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="CARD_MEMO"\r\n\r\n\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="CARDTYPE"\r\n\r\n\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="OUTFLAG"\r\n\r\n1\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="LAT"\r\n\r\n27.81673\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="LNG"\r\n\r\n114.420\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="MADDRESS"\r\n\r\n\xe6\xb1\x9f\xe8\xa5\xbf\xe7\x9c\x81\xe5\xae\x9c\xe6\x98\xa5\xe5\xb8\x82\xe8\xa2\x81\xe5\xb7\x9e\xe5\x8c\xba\xe5\xae\x9c\xe6\x98\xa5\xe5\xb8\x82\xe5\xae\x9c\xe9\x98\xb3\xe6\x96\xb0\xe5\x8c\xba\xe5\xae\x9c\xe6\x98\xa5\xe5\x9b\xbe\xe4\xb9\xa6\xe9\xa6\x86\xe5\xae\x9c\xe6\x98\xa5\xe5\xb8\x82\xe5\x8d\x9a\xe7\x89\xa9\xe9\xa6\x86\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="MACHINEALIAS"\r\n\r\n\xe5\xbe\xae\xe4\xbf\xa1\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1\r\nContent-Disposition: form-data; name="PHOTO"\r\n\r\nnull\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1--\r\n------WebKitFormBoundaryaSp5ER0SytDjXKd1--\r\n'
    payload2 = ''
    resp = requests.post(url=urls, headers=headers, data=payload).text
    send(NOW+'签到结果',resp)
