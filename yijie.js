/*
cron 59 15 8 * * * sign.js
易捷加油签到
*/
const axios = require('axios')
const notify = require('./sendNotify')
const header =  {
    "Accept":"application/json, text/plain, */*",
    "X-Date":"Tue, 22 Aug 2023 07:24:23 GMT",
    "Authorization":'hmac accesskey="16ec6d2769024c95", algorithm="hmac-sha1", headers="x-date content-md5", signature="JHs7NVNJPmgnU3D5HbiKcSpovoI="',
    "Content-md5":"1B2M2Y8AsgTpgAmY7PhCfg==",
    "Sec-Fetch-Site":"same-origin",
    "Accept-Language":"zh-CN,zh-Hans;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Sec-Fetch-Mode":"cors",
    "Content-Type":"application/json;charset=utf-8",
    "Origin":"https://egw.ejoy.sinopec.com",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x1800282f) NetType/4G Language/zh_CN miniProgram/wxbfe24664b9cf5b3b",
    "Referer":"https://egw.ejoy.sinopec.com/activityh5/app/getgifts/13cfe340b2cb475aa4b3990e76120635?token=3b7f5f3615f04870b13404dedc99f496&syssource=QBXCX",
    "Content-Length":"112",
    "Connection":"keep-alive",
    "Sec-Fetch-Dest":"empty",
    "Cookie":"acw_tc=0a6fd24b16926963785792100ee26e4259ce6f8147f73fd05dccf0d2b43531; aliyungf_tc=f9747271ad70aa92d70b4c0c1184b41da8033409bacb47dc0e3bf65c6ec42541"
    }
const payload = {"swtid":"13cfe340b2cb475aa4b3990e76120635","token":process.env.yijie,"datetime":1692689063764}

axios.post('https://egw.ejoy.sinopec.com/surveyWeb/api/inside/saveSignGift',payload,{headers:header} )
.then((res) => {
  notify.sendNotify('易捷加油签到结果',JSON.stringify(res.data))
  console.log(`statusCode: ${JSON.stringify(res.data)}`)
  console.log(res)
})
.catch((error) => {
  console.error(error)
})
