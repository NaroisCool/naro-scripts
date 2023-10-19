/*
cron: 59 15 8 * * 1-5
旗帜小程序奶粉积分明细
*/
const notify = require('./sendNotify')
const axios = require('axios')
const header =  {
    "Token-Cloud-WchatCp": process.env.naifen
    }
const payload={"unionId":"oPYap5391KOQPEwlpxfwWOGLJCtc","status":0,"memberId":"1630917159031545857","current":1,"pageSize":10}
const url=`https://sfa-prod.jlbry.cn/cp/points/recruit/credit/record/findPointsDetails`
axios.post(url,payload,{headers:header} )
.then((res) => {
  let arr = res.data['data']['creditRecord']['records']
  let credits = ''
  let total = res.data['data']['allCredit']
  console.log(total)
  for (let i = 0; i < arr.length; i++) {
    credits = credits+"\n"+arr[i]['creditSource']+":"+arr[i]['credit']
    }
  console.log(credits)
  notify.sendNotify("奶粉积分明细","总分："+total+"\n"+credits)
})
.catch((error) => {
  console.error(error)
})
