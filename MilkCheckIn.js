/*
cron: 59 15 8 * * 1-5
旗帜奶粉小程序签到
*/
const notify = require('./sendNotify')
const axios = require('axios')
const header =  {
    "Token-Cloud-WchatCp": process.env.naifen
    }
const url=`https://sfa-prod.jlbry.cn/cp/points/recruit/sign/doSign?unionId=oPYap5391KOQPEwlpxfwWOGLJCtc`
axios.post(url,{headers:header} )
.then((res) => {
  notify.sendNotify('免费领奶粉签到',res.data['msg'])
  console.log(`statusCode: ${res.statusCode}`)
  console.log(res)
})
.catch((error) => {
  console.error(error)
})
