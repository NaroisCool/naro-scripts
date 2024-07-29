/*
cron: 59 15 8 * * *
王者营地每日签到
自己抓包找到如下参数并设置到变量WZYD_TOKEN和WZYY_BODY里,多个账号用分号隔开
{"appid": "","openid": "","msdkEncodeParam": "","sig": "","userId": "","source": "","encode": 2,"timestamp": "","algorithm": "v2","version": "3.1.96i"};{"appid": "","openid": "","msdkEncodeParam": "","sig": "","userId": "","source": "","encode": 2,"timestamp": "","algorithm": "v2","version": "3.1.96i"}
{"cSystem":"ios","h5Get":1,"roleId":"1685189495"};{"cSystem":"ios","h5Get":1,"roleId":"520128481"}
*/
const axios = require('axios')
const notify = require('./sendNotify')
function version(){
	return new Promise(function(resolve,reject){
	resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))})
}

async function main(){
    	await version().then(data=>{console.log(data.data)})
		// 从环境变量中获取Cookie
		const cookieHeaderValue = process.env.WZYD_TOKEN;
        const bodyValue = process.env.WZYD_BODY;
		// 将Cookie值拆分为单独的Cookie
		const cookies = cookieHeaderValue.split(';');
        const body = bodyValue.split(';');
        let count = 0 
		for (cookie of cookies){
			const header = JSON.parse(cookie)
            const payload = JSON.parse(body[count])
            axios.post('https://kohcamp.qq.com/operation/action/signin',payload,{headers:header} )
            .then((res) => {
                console.log(payload.roleId+'的王者营地签到结果'+JSON.stringify(res.data))
                notify.sendNotify(payload.roleId+'的王者营地签到结果',JSON.stringify(res.data))
            }).catch((error) => {
                console.error(error)
            })
                count = count +1
            }
			
}
main()
