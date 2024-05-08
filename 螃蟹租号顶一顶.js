/*
cron: 0 0 9 * * *
螃蟹租号顶一顶
*/
const axios = require('axios')
const notify = require('./sendNotify')
const header =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": process.env.pxtoken,
        "LoginStatus": "true",
        "x-fronend-tcpport": "5628657",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
const pids = [29217,113576]
const game_ids = [79,61]
for (pid of pids){
    for (game_id of game_ids){
        const payload = `{\"game_id\":${game_id},\"product_id\":${pid}}`
        axios.post('https://api.pxb7.com/api/product/gore',payload,{headers:header} )
        .then((res) => {
        notify.sendNotify('螃蟹租号顶一顶',JSON.stringify(res.data))
        console.log(res.data)
        })
        .catch((error) => {
        console.error(error)
    })
    }
    
}




