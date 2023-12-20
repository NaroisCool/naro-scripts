/*
cron: 59 15 8 * * *
三国杀OL小程序-三国桃园刷任务
找到自己的token填到Authenticate即可
*/
const notify = require('./sendNotify')
const axios = require('axios')

//每日签到

// 从环境变量中获取Cookie
const cookieHeaderValue = process.env.sanguosha;

// 将Cookie值拆分为单独的Cookie
const cookies = cookieHeaderValue.split(';');

// 遍历每个Cookie值
const _0x60d3=['error','https://preolforum.sanguosha.com//wx/thread/like?tid=','https://preolforum.sanguosha.com//wx/first/post?tid=','get','isLike','application/json','tid','then','catch','data','log','Mozilla/5.0\x20(iPhone;\x20CPU\x20iPhone\x20OS\x2016_6\x20like\x20Mac\x20OS\x20X)\x20AppleWebKit/605.1.15\x20(KHTML,\x20like\x20Gecko)\x20Mobile/15E148\x20MicroMessenger/8.0.41(0x18002930)\x20NetType/WIFI\x20Language/zh_CN','forEach'];const _0x32f2=function(_0x60d3fa,_0x32f289){_0x60d3fa=_0x60d3fa-0x0;let _0x283c13=_0x60d3[_0x60d3fa];return _0x283c13;};cookies[_0x32f2('0xc')](_0x11a408=>{let _0x5ea68e={'Host':'preolforum.sanguosha.com','Connection':'keep-alive','Authenticate':_0x11a408,'content-type':_0x32f2('0x5'),'Accept-Encoding':'gzip,compress,br,deflate','User-Agent':_0x32f2('0xb'),'Referer':'https://servicewechat.com/wx88a45073e0660980/59/page-frame.html'};axios[_0x32f2('0x3')]('https://preolforum.sanguosha.com//wx/forum/clock?type=1',{'headers':_0x5ea68e})[_0x32f2('0x7')](_0x54093e=>{console['log'](_0x54093e);})[_0x32f2('0x8')](_0x16842f=>{console[_0x32f2('0x0')](_0x16842f);});axios[_0x32f2('0x3')]('https://preolforum.sanguosha.com//v2/forum/list?fid=77&page=1',{'headers':_0x5ea68e})['then'](_0x3465cd=>{let _0x1ce993=0x0;for(const _0x486e9b of _0x3465cd[_0x32f2('0x9')]['data']['list']){if(_0x486e9b[_0x32f2('0x4')]===![]){axios[_0x32f2('0x3')](_0x32f2('0x2')+_0x486e9b['tid'],{'headers':_0x5ea68e})[_0x32f2('0x7')](_0x46f51e=>{console['log'](_0x46f51e);})[_0x32f2('0x8')](_0xd3dd09=>{console['error'](_0xd3dd09);});axios[_0x32f2('0x3')](_0x32f2('0x1')+_0x486e9b[_0x32f2('0x6')],{'headers':_0x5ea68e})['then'](_0x4f4c28=>{console[_0x32f2('0xa')](_0x4f4c28);})[_0x32f2('0x8')](_0x8dd6bf=>{console[_0x32f2('0x0')](_0x8dd6bf);});_0x1ce993=_0x1ce993+0x1;}if(_0x1ce993>=0x5){break;}}})[_0x32f2('0x8')](_0x5aaf75=>{console['error'](_0x5aaf75);});});
