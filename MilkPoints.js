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
const _0x39b8=['奶粉积分明细','https://sfa-prod.jlbry.cn/cp/points/recruit/credit/record/findPointsDetails','length','sendNotify','总分：','data','then','log','error','credit'];const _0x4536=function(_0x39b893,_0x45368f){_0x39b893=_0x39b893-0x0;let _0x262ad6=_0x39b8[_0x39b893];return _0x262ad6;};const url=_0x4536('0x1');axios['post'](url,payload,{'headers':header})[_0x4536('0x6')](_0x4c56e2=>{let _0x430264=_0x4c56e2['data'][_0x4536('0x5')]['creditRecord']['records'];let _0x482056='';let _0x58f3cb=_0x4c56e2[_0x4536('0x5')]['data']['allCredit'];console[_0x4536('0x7')](_0x58f3cb);for(let _0x2b9f4e=0x0;_0x2b9f4e<_0x430264[_0x4536('0x2')];_0x2b9f4e++){_0x482056=_0x482056+'\x0a'+_0x430264[_0x2b9f4e]['creditSource']+':'+_0x430264[_0x2b9f4e][_0x4536('0x9')];}console[_0x4536('0x7')](_0x482056);notify[_0x4536('0x3')](_0x4536('0x0'),_0x4536('0x4')+_0x58f3cb+'\x0a'+_0x482056);})['catch'](_0xb6f01d=>{console[_0x4536('0x8')](_0xb6f01d);});
