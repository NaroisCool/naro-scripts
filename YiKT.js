/*
cron: 0 0 9 * * *
江西文旅一卡通余票监控
修改参数
bookingDate
X-WECHAT-HOSTSIGN
*/
const notify = require('./sendNotify')
const axios = require('axios')
function version() {
    return new Promise(function (resolve, reject) {
        resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))
    })
}
const formattedDate = new Date().toISOString().slice(0, 10);
async function main() {
    await version().then(data => { console.log(data.data) })

  axios.get('https://card.ly3618.com/jxcard/api/booking/v1/storeBooking/listShowConfig', {
  params: {
    'uuid': '4f016263126d49958e9bbbf3689aee59',
    'bookingDate': '2025-08-16'
  },
  headers: {
    'Host': 'card.ly3618.com',
    'Connection': 'keep-alive',
    'burialDataEvId': 'D45602D582F15150',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Authorization': 'bearer eb0050c4-ea3c-4cc7-bf11-eff6eebc1ab0',
    'X-WECHAT-HOSTSIGN': '{"noncestr":"51db2d7efcdac705ab268fc88e07a094","timestamp":1753454277,"signature":"1540823a8626fd579ae04a4b9149852e144cea86"}',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.60(0x18003c32) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx37242ffaf5e753a0/97/page-frame.html'
  }
}).then((res) => {
        (res.data.data)[0].surplusNum > 0 ? notify.sendNotify('有票了！',(res.data.data)[0].surplusNum+'张' ): console.log((res.data.data)[0].surplusNum+'张')
    }).catch((error) => {
        console.error(error)
    })
}
main()
