/*
cron 20 * * *
*/
const notify = require('./sendNotify')
const request = require('axios')
const payload = "duanlianjieabc=&channelCode=&serviceType=&saleChannel=&externalSources=&contactCode=&ticket=&ticketPhone=&ticketChannel=&userNumber=&language=chinese"
const header = {
    "Cookie":process.env.UNICOM_TOKEN,
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 unicom{version:iphone_c@9.0500}"
} 

request.post("https://m.client.10010.com/servicequerybusiness/balancenew/accountBalancenew.htm",payload,{headers:header}).then((res)=>{
    var res = res.data
    var report = '剩余话费：'+res.curntbalancecust+'，当月支出：'+res.allbillfee+'，（其中上网费：'+res.realTimeFeeSpecialFlagThree[0].bill.billfee+'，月固定费：'+res.realTimeFeeSpecialFlagThree[1].bill.billfee+'，语音通话：'+res.realTimeFeeSpecialFlagThree[2].bill.billfee+'，）当月存入：'+res.monthlyRechargeBill+'，上月余额：'+res.carryForwardFromLastMonth
    console.log(report)
    notify.sendNotify('联通账单简报',report)
})
