/*
cron: 59 15 8 * * *
云闪付签到
*/
const notify = require('./sendNotify')
const axios = require('axios')


function version(){
    return new Promise(function(resolve,reject){
    resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))})
}

async function main(){
    await version().then(data=>{console.log(data.data)})
    const header =  {
            "Host": "youhui.95516.com",
            "Accept": "application/json, text/plain, /",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJQVlZKUkoxRzYiLCJ0IjoiMDIxNzI1MzIiLCJpYXQiOjE2OTY2NDA0NzAsImV4cCI6MTk1NTg0MDQ3MH0.AJaDlMGyJsuaQcbE-W6tAd-LCZ_zBCPPg7M0iODu8ls",
            "Sec-Fetch-Site": "same-origin",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "x-city": "360900",
            "Sec-Fetch-Mode": "cors",
            "Accept-Encoding": "gzip, deflate, br",
            "Origin": "https://youhui.95516.com",
            "Content-Length": "2",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/sa-sdk-ios (com.unionpay.chsp) (cordova 4.5.4) (updebug 0) (version 938) (UnionPay/1.0 CloudPay) (clientVersion 198) (language zh_CN) (upHtml) (walletMode 00)",
            "Referer": "https://youhui.95516.com/newsign/public/app/index.html",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Sec-Fetch-Dest": "empty",
            "Cookie": process.env.YSF
    
        }
    const payload = {}
    axios.post('https://youhui.95516.com/newsign/api/daily_sign_in',payload,{headers:header} )
    .then((res) => {
      notify.sendNotify('云闪付签到结果',res.data.signedIn+res.data.days)
      console.log(res.data)
    })
    .catch((error) => {
      console.error(error)
    })
}
main()
