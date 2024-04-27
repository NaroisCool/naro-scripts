/*
cron: 59 15 8 * * *
三国杀OL小程序-三国桃园刷任务
找到自己的token填到Authenticate即可
*/
const notify = require('./sendNotify')
const axios = require('axios')

//每日签到

// 从环境变量中获取Cookie
const cookieHeaderValue = process.env.sanguosha;

// 将Cookie值拆分为单独的Cookie
const cookies = cookieHeaderValue.split(';');

function version(){
        return new Promise(function(resolve,reject){
        resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))})
}

async function main(){
        await version().then(data=>{console.log(data.data)})
        // 遍历每个Cookie值
        for(cookie of cookies){
            let header =  {
                    "Host": "preolforum.sanguosha.com",
                    "Connection": "keep-alive",
                    "Authenticate": cookie,
                    "content-type": "application/json",
                    "Accept-Encoding": "gzip,compress,br,deflate",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x18002930) NetType/WIFI Language/zh_CN",
                    "Referer": "https://servicewechat.com/wx88a45073e0660980/59/page-frame.html"
        
                }

            
            await axios.get('https://preolforum.sanguosha.com//wx/user/info',{headers:header} )
                .then((res) => {console.log('账号：'+res.data.data.name+'...')})
            .catch((error) => {
                console.error(error)
            })

            axios.get('https://preolforum.sanguosha.com//wx/forum/clock?type=1',{headers:header} )
                .then((res) => {console.log(res.data.msg)})
            .catch((error) => {
            console.error(error.response.data)
            })
        
            axios.get('https://preolforum.sanguosha.com//v2/forum/list?fid=77&page=1',{headers:header} )
            .then((res) => {
            //console.log(res.data.data.list)
            let count = 0;
        
            for (const item of res.data.data.list) {
                //console.log(item'isLike'])
                if (item.isLike === false) {
        
                //浏览帖子
                axios.get('https://preolforum.sanguosha.com//wx/first/post?tid='+item.tid,{headers:header} )
                .then((res) => {
                    console.log('浏览帖子任务'+res.data.msg)
                }).catch((error) => {
                    console.error(cookie+error.response.data)
                })
                //点赞
                axios.get('https://preolforum.sanguosha.com//wx/thread/like?tid='+item.tid,{headers:header} )
                .then((res) => {
                    console.log('点赞任务'+res.data.msg)
                }).catch((error) => {
                    console.error(cookie+error.response.data)
                })
                count = count+1
                }
                //每日五次
                if (count >= 5) {
                break;
                }
            }
            })
            .catch((error) => {
            console.error(error.response.data)
            })
        }
}
main()
