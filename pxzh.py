#螃蟹租号爬虫
import requests
import notify

# 定义基础URL
base_url = 'https://api.pxb7.com/api/product/daily/details?game_id=61&date=1712419200&page={}'
header ={
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "ApiToken":"dfb00eb839abe281c499e141686f3247",
    "token":"feb93033a7ab04ea442b08103ec019a4",
    "loginstatus": "false",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"}

ol = 0
ten = 0
mobile = 0
start_page = 1
while True:
    # 构造完整的URL
    url = base_url.format(start_page)

    # 发送HTTP GET请求并获取响应
    response = requests.get(url=url,headers=header).json()
    code = response.get('code')
    # 检查响应的状态码
    if code == 200:
        data = response.get('data')
        #print(data)
        #昨日卖出总数
        total = data.get('total')
        start_page = data.get('page')
        #租号数据
        data2 = data.get('list')
        #总共的页码
        pages = (total + 10 -1) // 10
        print('总共页数'+str(pages))
        print('总数'+str(total))
        print('第'+str(start_page)+'页')
        if start_page <= pages:
            for l in data2:
                try:
                    if 'OL' in l.get('category')[0].get('value'):
                        gj = l.get('category')[3].get('value')
                        name = l.get('name')
                        date = l.get('pay_date')
                        pop = str(l.get('collect'))
                        price = str(l.get('price'))
                        #print('官阶：'+gj+'\n描述：'+name+'\n价格：'+price+'\n成交时间'+date+'\n欢迎度'+pop)
                        notify.send('爬取结果','官阶：'+gj+'\n描述：'+name+'\n价格：'+price+'\n成交时间'+date+'\n欢迎度'+pop)
                        ol = ol +1
                    if '十周年' in l.get('category')[0].get('value'):
                        ten = ten +1
                    if '移动' in l.get('category')[0].get('value'):
                        mobile = mobile +1
                except:
                    print('出错')
            if start_page == pages:
                print('遍历完成！')
                notify.send('遍历完成！','ol/十周年/移动'+str(ol)+'/'+str(ten)+'/'+str(mobile))
                break
            else:
                start_page = start_page +1
        else:
            break
