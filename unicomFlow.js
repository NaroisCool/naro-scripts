/*
cron: 59 36 9-19/2 * * 1-5
*/
const notify = require('./sendNotify')
const request = require('axios')
const payload = "duanlianjieabc=&channelCode=&serviceType=&saleChannel=&externalSources=&contactCode=&ticket=&ticketPhone=&ticketChannel=&userNumber=&language=chinese"
const header = {
    "Cookie":process.env.UNICOM_TOKEN,
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 unicom{version:iphone_c@9.0500}"
} 
request.post("https://m.client.10010.com/servicequerybusiness/operationservice/queryOcsPackageFlowLeftContentRevisedInJune", payload, {headers:header}).then((res)=>{
    var res = res.data
    var report = '今日使用流量:'+res.rzbAllUse+'MB, 通话☎️超出'+res.voiceExceed+'分钟,短信🆕超出'+res.smsHeadUsed+'条'
    console.log(report)
    notify.sendNotify('实时流量统计',report)
})
