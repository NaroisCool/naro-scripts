import json
import os
from urllib.parse import quote
import httpx
import requests
from bs4 import BeautifulSoup
import notify

"""
    百变小樱机场自动签到领流量
    机场注册地址☞ https://dash.bbxy.buzz/auth/register?code=G9we
    脚本执行要求安装python依赖bs4和httpx;填入变量BBXY_EMAIL（邮箱账号）和BBXY_PASSWORD（登录密码）
    感谢原作者Admsec，
    经NaroisCool改进，将从百变小樱官方永久地址发布网站（http://bbxy88.com/）上爬取最新的国内访问地址，以及其他方法内的逻辑改动。
"""


class BBXYSign:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                      "like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
        self.session = httpx.Client()
        self.originUrl = ""
        self.loginUrl = ""
        self.email = os.environ.get("BBXY_EMAIL")
        self.password = os.environ.get("BBXY_PASSWORD")
        self.params = {"email": self.email, "passwd": self.password, "remember-me": '0'}
        self.signSuccessOrNot = False
        self.signSuccessMsg = ""
      
    def check_websites_sync(self, websites):
        with httpx.Client(headers=self.headers) as client:
            print(f"总共{len(websites)}个网站")
            count = 1
            for site in websites:
                try:
                    response = client.get(site)
                    if response.status_code == 200 :
                        print(f"这个链接可以访问，暂定:{site}")
                        self.loginUrl = site + "auth/login"
                        self.originUrl = site
                        #进行登录测试
                        flag = self.login()
                        if flag:
                            print(f"这个链接可以登录，锁定:{site}")
                            count = count +1
                            if count>len(websites):
                                notify.send('BBXY签到结果！','所有网站登录测试失败，请重新运行一遍！') 
                            return site
                        else :
                            print(f'登录失败，尝试下一个链接')
                            print('-----------------')
                            count = count +1
                            if count>len(websites):
                                notify.send('BBXY签到结果！','所有网站登录测试失败，请重新运行一遍！')                           
                            continue
                except httpx.RequestError as e:
                    print(f"这个链接不能用，避一避: {site} - {e}")
                    print('-----------------')
                    count = count +1
                    if count>len(websites):
                                notify.send('BBXY签到结果！','所有网站登录测试失败，请重新运行一遍！')                   
                    continue

    '''
    登录
    '''

    def login(self):
        print('开始登录测试...')        
        try:
            r = self.session.post(url=self.loginUrl, params=self.params, headers=self.headers)
            response = json.loads(r.text)
            if response['ret'] != 1:
                print(f"登录失败, 原因：{response['msg']}")
                return False
            else:
                print("登录成功")   
                return True
        except Exception as e:          
            print(e)
            return False

    """
    签到
    """

    def sign(self):
        try:
            client = self.session.post(url=self.originUrl + "user/checkin", params=self.params, headers=self.headers)
            response = json.loads(client.text)
            if response['ret'] != 1:
                print(f"签到失败了，原因是{response['msg']}")
                notify.send('BBXY签到结果：',response['msg'])
                return False
            self.signSuccessMsg = response
            self.signSuccessOrNot = True
            #result = self.signSuccessMsg['msg'].decode('unicode_escape')
            msg = (f"签到成功:{self.signSuccessMsg['msg']}\n总流量{self.signSuccessMsg['traffic']}\n"
                       f"今日已用{self.signSuccessMsg['trafficInfo'].get('todayUsedTraffic')}\n"
                       f"总共已用{self.signSuccessMsg['trafficInfo'].get('lastUsedTraffic')}\n"
                       f"剩余流量{self.signSuccessMsg['trafficInfo'].get('unUsedTraffic')}\n")
            if self.signSuccessOrNot:
                notify.send('BBXY签到结果！',msg)
                return True
            else:
                notify.send('BBXY签到结果！',msg)
                return False
            return True
        except Exception as e:
            print(e)
            return False
    
    """
    消息模板，顺便发送消息到微信公众号
    """
        


if __name__ == '__main__':
    """
    主程序
    从http://bbxy88.com/上爬取最新国内的入口地址
    """
    print("*****\n"
    "百变小樱机场自动签到领流量\n"
    "机场注册地址☞ https://bbxy.life/auth/register?code=G9we\n"
    "脚本执行要求填入变量BBXY_EMAIL（邮箱账号）和BBXY_PASSWORD（登录密码）\n"
    "感谢原作者Admsec，\n"
    "经NaroisCool改进，将从百变小樱官方永久地址发布网站（http://bbxy88.com/）上爬取最新的国内访问地址，以及其他方法内的逻辑改动。\n"
    "*****")
    url = 'http://bbxy88.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    additional_links = ['https://dash.bbxy.buzz/','https://baibianxiaoying.top/']
    websites = links+additional_links
    a = BBXYSign()
    a.check_websites_sync(websites)
    a.sign()
