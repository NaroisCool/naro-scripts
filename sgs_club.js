/*
cron: 0 * * *
三国社区签到
*/
const notify = require('./sendNotify')
const axios = require('axios')
const header= {
        'Host': 'club.sanguosha.com',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'IwdU_2132_lastact=1701358194%09plugin.php%09; IwdU_2132_st_p=289159%7C1701358173%7C055ada9ed4519c678b55f7b565fdc131; IwdU_2132_viewid=tid_1287953; IwdU_2132_forum_lastvisit=D_60_1701358068; IwdU_2132_st_t=289159%7C1701358068%7C306364b378138d5073d11977e054aef6; IwdU_2132_creditbase=0D892D0D131D0D20D0D0D0; IwdU_2132_creditnotice=0D5D0D0D0D0D0D0D0D289159; IwdU_2132_atarget=1; IwdU_2132_auth=c18bmoSxLuQgk9ilN3ZlhSBMlxDUPU%2B%2Fqb6vZS8PAje1nKPBTJtHPNsHNV1yaKAEZlhbEgZP7FWEBiS4puvocNN3jJA; IwdU_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; IwdU_2132_lastcheckfeed=289159%7C1701358055; IwdU_2132_nofavfid=1; IwdU_2132_ulastactivity=1701358055%7C0; IwdU_2132_lastvisit=1701354326; IwdU_2132_saltkey=jZ8dgMM1; acw_tc=0b32821217013578439803420e1c8c95d4e9a4a359f967ed624f9d263b6011; SGS_DEVICEID=WEB-EBBA55B9-A6AF-4700-98DB-1718E74E2F8A; SGS_DEVICEID_SPARE=WEB-EBBA55B9-A6AF-4700-98DB-1718E74E2F8A',
        'Connection': 'keep-alive',
        'Sec-Fetch-Mode': 'navigate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'Referer': 'https://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=0&inajax=0&mobile=yes',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
    }

axios.post('https://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=0&inajax=0&mobile=yes',new URLSearchParams({
        'formhash': 'a5da46ff'
    }),{headers:header})
.then((res) => { 
      notify.sendNotify('签到结果',res.data);
}).catch((error) => {
  console.error(error)
})
