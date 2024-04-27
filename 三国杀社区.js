/*
cron: 9 * * *
三国社区签到
*/
const notify = require('./sendNotify')
const axios = require('axios')
function version(){
        return new Promise(function(resolve,reject){
        resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))})
}

async function main(){
        await version().then(data=>{console.log(data.data)})
        const header= {
                'Host': 'club.sanguosha.com',
                'Sec-Fetch-Site': 'same-origin',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cookie': 'IwdU_2132_lastact=1713015996%09plugin.php%09; IwdU_2132_mobile=no; IwdU_2132_noticeTitle=1; IwdU_2132_sendmail=1; IwdU_2132_atarget=1; IwdU_2132_forum_lastvisit=D_61_1713015856; IwdU_2132_st_t=289159%7C1713015856%7C5796c1595b853aa2fb63b9228f30a939; IwdU_2132_auth=0107w0ZY%2B%2Fl8IHM7qs5PqiWU5FOZ0dqvEaLSIM2%2BqYyjSbnZ1b4g%2B1itSRuIF94KEK%2F3oKYfV21rF0etaX17Ue3NG7g; IwdU_2132_lastcheckfeed=289159%7C1713015853; IwdU_2132_nofavfid=1; IwdU_2132_ulastactivity=1713015853%7C0; IwdU_2132_lastvisit=1713012246; IwdU_2132_saltkey=dUS80AA8; acw_tc=0b32807617130158468018374e3e0c9607e954935bbdeca12f4175ef3ec282; SGS_DEVICEID=WEB-12255F68-CEC7-4000-9DFF-F4E756C74A66; SGS_DEVICEID_SPARE=WEB-12255F68-CEC7-4000-9DFF-F4E756C74A66; Hm_lvt_741c1946c0ae40c84a3db0b843e0b944=1712107450,1712109092,1712126920,1712882997; Hm_lvt_fb3e47332f1c41f3e8dd1961d001377f=1712107450,1712109092,1712126920,1712882997',
                'Connection': 'keep-alive',
                'Sec-Fetch-Mode': 'navigate',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                'Referer': 'https://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign',
                'Sec-Fetch-Dest': 'document',
                'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
            }
        
        axios.post('https://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1','7110f1c2',{headers:header})
        .then((res) => { 
            console.log(res.data)
              notify.sendNotify('签到结果',res.data);
        }).catch((error) => {
          console.error(error)
        })
}
main()
