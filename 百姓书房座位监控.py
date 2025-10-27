

import requests
import notify
import re
#每天的sign不一样，且要一一对应。
combine = [{'sign':'9F8D054C5CA8CC18C485842603F83177','date':'2025-10-28'},{'sign':'83D2F2B9C439700ADBF6331D5FB30B01','date':'2025-10-29'},{'sign':'044214497EBE5BC71A7CCE31E458B2A6','date':'2025-10-30'}]
for c in combine:
    headers = {
        'Host': 'api.yuxiusz.com',
        'Connection': 'keep-alive',
        # 'Content-Length': '46',
        'Token': 'TC1myo0TW6eEM4vA21sNuxb5XTGgz2edcKKsrZRfdp8/XuKpUVcfn942aDgaesA/bwVO34UP/CuqilVXCKI84wmfazW+DTAbO4s02zRKbB//R6ifvwPMdr1pGbOlxE11Zc/pY4m3zCQ78N7BtSuFH+ZFBCoijYbevsrZtr7/8qONEVWlnsgxS0k47CMBVK8jmyu0XQt4KnqXwfXkdS9l27kD0PZ+3l+PcyBYaFEbsdlvESetKUtn8TbXXsqzNSZ0sqQWZjV33ef1NNk5nQ/kLHCfRFDF9PJ3ph8m4CCAaDHVsTqKnJ+5RVSJhpQGY6PldHdy98gEKjsLOtN8gJ6uiA==',
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
            name = item['name']
            pattern = r'[^\w\s\u4e00-\u9fa5]'   
            seat = re.sub(pattern,'',name)
            for detail in item['details']:
                reservable_details = [
            {    
                'time_slot': f"{detail['start_time']} - {detail['end_time']}",
                'is_reservable': detail['is_reservable'],
                'date': detail['date']
            }]
                if detail['is_reservable']:
                    notify.send(f"{reservable_details[0]['date']}的{seat}有座位了！！", "时间段"+str(reservable_details[0]['time_slot']))
                    print(reservable_details)
                else:
                    print(reservable_details[0]['date']+'暂时没座位。')
    except:
        print('token有问题，请重新获取')
        notify.send('百姓书房座位监控失败~','请检查Token和sign是否正确和有效。')
