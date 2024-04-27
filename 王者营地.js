/*
cron: 59 15 8 * * *
王者营地每日签到
自己抓包找到msdkEncodeParam参数并设置到变量WZYD_TOKEN里
*/
const axios = require('axios')
const notify = require('./sendNotify')
function version(){
    return new Promise(function(resolve,reject){
    resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))})
}

async function main(){
    await version().then(data=>{console.log(data.data)})
	const header =  {
		"appid": "1105200115",
		"openid": "A83B54FFF9932164D7E39DB3B88D7087",
		"msdkEncodeParam": process.env.WZYD_TOKEN,
		"sig": "eb4fa36c0605e1c177f22d07a63ba780",
		"userId": "407825320",
		"roleId": "634229831",
		"gameId": "20001",
		"gameOpenid": "54BB3BCAA8E14D025D8CBA0C37230351",
		"msdkToken": "pudhlNwI",
		"source": "smoba_zhushou",
		"Origin": "https://camp.qq.com",
		"encode": 2,
		"noencrypt": 1,
		"timestamp": "1665531674282",
		"cClientVersionName": "6.74.401",
		"algorithm": "v2",
		"version": "3.1.96i"
	    }
	const payload = {"cSystem":"ios","h5Get":1,"roleId":"1685189495"}
	
	axios.post('https://kohcamp.qq.com/operation/action/signin',payload,{headers:header} )
	.then((res) => {
	  notify.sendNotify('王者营地签到结果',JSON.stringify(res.data))
	  console.log(`statusCode: ${res.data.returnMsg}`)
	  console.log(res)
	})
	.catch((error) => {
	  console.error(error)
	})
}
main()
