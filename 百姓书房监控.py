

import requests
import notify
#每天的sign不一样，且要一一对应。
combine = [{'sign':'A864C49958A6F098546B20334124A4E0','date':'2025-10-26'},{'sign':'BA828EACB93C71EA2BAC9F03F9FB475E','date':'2025-10-27'}]
for c in combine:
    headers = {
        'Host': 'api.yuxiusz.com',
        'Connection': 'keep-alive',
        # 'Content-Length': '46',
        'Token': 'TC1myo0TW6eEM4vA21sNuxb5XTGgz2edcKKsrZRfdp8/XuKpUVcfn942aDgaesA/bwVO34UP/CuqilVXCKI84wmfazW+DTAbO4s02zRKbB//R6ifvwPMdr1pGbOlxE11cyWhSiqdGJc1NpfkwXFkdSHGZAFfvO8UtrJuE0s2VFh5bcDDI2iZo49QwN3nWdLbmyu0XQt4KnqXwfXkdS9l27kD0PZ+3l+PcyBYaFEbsdlvESetKUtn8TbXXsqzNSZ0+NmNrnbsijP1q8IDkh3GcMZfxJrajo+ZUB7/t+O51D4qoodwsYcP589ZPZrhQze6ErqFDpLjbzDdp0kRgYzZlw==',
        'content-type': 'application/x-www-form-urlencoded',
        'instid': '2001',
        'Sign': c['sign'],
        # 'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.64(0x1800402b) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxf634f3b3f235aa75/9/page-frame.html',
    }

    data = {
        'org_id': '704',
        'area_id': '6075',
        'choose_date': c['date'],
    }

    response = requests.post('https://api.yuxiusz.com/appapi/reservation/Seats', headers=headers, data=data)

    data = response.json()
    try:
        for item in data['data']:
            name = item['name'],   
            for detail in item['details']:
                reservable_details = [
            {    
                'time_slot': f"{detail['start_time']} - {detail['end_time']}",
                'is_reservable': detail['is_reservable'],
                'date': detail['date']
            }]
                if detail['is_reservable']:
                    notify.send(f"{name}有座位了！！", str(reservable_details[0]))
                    print(reservable_details)
                else:
                    print(reservable_details[0]['date']+'暂时没座位。')
    except:
        print('token有问题，请重新获取')
