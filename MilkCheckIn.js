/*
cron: 59 15 8 * * *
旗帜奶粉小程序签到
https://sfa-prod.jlbry.cn/cp/points/recruit/sign/doSign
*/
const notify = require('./sendNotify')
const axios = require('axios')
const header =  {
    "Token-Cloud-WchatCp": process.env.naifen
    }
const _0x5f31=['post','error','data','then','statusCode','msg','log'];const _0x2155=function(_0x5f3127,_0x215521){_0x5f3127=_0x5f3127-0x0;let _0x3a6ac4=_0x5f31[_0x5f3127];return _0x3a6ac4;};const url='https://sfa-prod.jlbry.cn/cp/points/recruit/sign/doSign?unionId=oPYap5391KOQPEwlpxfwWOGLJCtc';axios[_0x2155('0x0')](url,{'headers':header})[_0x2155('0x3')](_0x4472f8=>{notify['sendNotify']('免费领奶粉签到',_0x4472f8[_0x2155('0x2')][_0x2155('0x5')]);console['log']('statusCode:\x20'+_0x4472f8[_0x2155('0x4')]);console[_0x2155('0x6')](_0x4472f8);})['catch'](_0x542619=>{console[_0x2155('0x1')](_0x542619);});
