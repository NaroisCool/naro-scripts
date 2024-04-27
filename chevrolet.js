/*
雪佛兰app签到
将抓包里的cpctoken放到xflCookie
*/

const axios = require('axios')
const notify = require('./sendNotify')

function version(){
    return new Promise(function(resolve,reject){
    resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))})
}

async function main(){
  await version().then(data=>{console.log(data.data)})
  axios.post(
    'https://ctwx.sgmlink.com/api/check/submit',
    {},
    {
      headers: {
        'Host': 'ctwx.sgmlink.com',
        'X-Tingyun': 'c=B|xoQp58Chn_A;x=1ef0e146bdd74a59',
        'Accept': 'application/json, text/plain, */*',
        'cpctoken': process.env.xflCookie,
        'userType': '1',
        'Sec-Fetch-Site': 'same-origin',
        'source': '0',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'cors',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://ctwx.sgmlink.com',
        'User-Agent': 'Optional(Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MyChevy/7.20.0) MyChevy/7.20.0',
        'Referer': 'https://ctwx.sgmlink.com/portal/',
        'Content-Length': '2',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty'}
    }
  ).then((res) => {console.log(res);notify.sendNotify('签到结果：',JSON.stringify(res.data))})
      .catch((error) => {
      console.error(error)
      })
}
main()
