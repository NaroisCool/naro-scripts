import requests

def offRent():
    url = 'https://www.zuhaowan.com/Account/offRent.html'
    cookie = 'Hm_lpvt_e4e4ed899c525f81b649490c283bbca7=1655471087;Hm_lvt_e4e4ed899c525f81b649490c283bbca7=1653706733,1655367866,1655447640;Hm_lpvt_bed4c82ceb65d9a6cb7032125195648c=1655471087;Hm_lvt_bed4c82ceb65d9a6cb7032125195648c=1653706734,1655367866,1655447641;dofun_stamp=608064Y0AZQnEmhaesmE6qdXfBE2u6zcZ-oaKIPeG5WAMeF0wjDRFC_Ha4BEOmMA2upShThqtONAmOpPFglrqaMEc7GygvyGMlIhav1R8OKB7e-PZYwNDQ5lXBRIE4mMx2dGe_TuL7yryixLR_0Gj9PymKwlc6yki28h9WsP2v;guide_newer=1;registerForm=1;stamp=b35db85184e587543903888a762a029f;stampu=C1361CD74DBB639781B0C06C519DFBE594BCEE1A4E9328931A8BC9E470EFCC8B3FDD46E5FBD569499E96109D7F5EC03938AA566243FF15041E34A904142E49021A4B9BDF8638D031EECDB6FA9AA65127CDAC9B8EAC533537277B354C0B980FD88C5FC64C5490F56D4690ECA1E45DD22B481B5612D173B6ACBFC1CB0C522B03F0F59016993A9D11AB8C7E589CE88A3C7DB0674FF27698DF30605FC76C2A49333376A23ED04C785D43F6459C190BE1E9F48B4A71A0B40729C238C28FA9197035CF2DE9C6B7A41AF3FB630B0E82C0;zhwun=ACFAE3288C312D0D2912EC;__pu__=10983FFC85A04A9A58E2A0;PHPSESSID=jqs25ut7v8stesnm6upv40v081;nouid=62aae92f778192429;__puno__=54C164A2D5FC11F454ECA5B91EEBEDF6'
    headers = {
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/102.0.5005.87 Mobile/15E148 Safari/604.1',
        'Connection': 'keep-alive',
        'Cookie': cookie
    }
    res = requests.post(url=url, headers=headers, data='id=10284948&accountsign=')
    print(res.json().get('message'))


if __name__ == '__main__':
    offRent()
    #sold_out()