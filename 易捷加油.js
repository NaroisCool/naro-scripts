/*
cron 59 15 8 * * * sign.js
易捷加油签到
*/
const axios = require('axios')
const notify = require('./sendNotify')
var currentDate = new Date();
var options = { month: 'short', year: 'numeric', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit', timeZone: 'GMT' };
var options3 = {day: '2-digit'}
var options2 = { weekday: 'short' };
var dayOfWeek = currentDate.toLocaleString('en-US', options2);
var day = currentDate.toLocaleString('en-US', options3);
var formattedDate =dayOfWeek+', '+day+' '+currentDate.toLocaleString('en-US', options).replace(/,/g, '')+' GMT';
console.log(formattedDate);
const header =  {
    "Accept":"application/json, text/plain, */*",
    "X-Date":formattedDate,
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
    "Cookie":"aliyungf_tc=a91508a137977b952f00b54060e71499aeb91f1a7fc5f6aff6872617ad25de26; acw_tc=ac11000117140312485898067e4b825cb89c6bf532acecaf1cb97eade190e6"
    }
const payload = {"swtid":"bbfc100c8e4c41ad90be696bfb139809","token":'764f0da59a8b4954a04d3220f02e14a4',"datetime":Date.now()}

axios.post('https://egw.ejoy.sinopec.com/surveyWeb/api/inside/saveSignGift',payload,{headers:header} )
.then((res) => {
  notify.sendNotify('易捷加油签到结果',JSON.stringify(res.data))
  console.log(`statusCode: ${JSON.stringify(res.data)}`)
  console.log(res)
})
.catch((error) => {
  console.error(error)
})
