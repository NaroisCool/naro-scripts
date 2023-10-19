/*
cron: 59 15 11 * * *
clashnode订阅地址自动获取
*/
const notify = require('./sendNotify')
const axios = require('axios')
const currentDate = new Date();
const year = currentDate.getFullYear();
const month = String(currentDate.getMonth() + 1).padStart(2, '0');
const day = String(currentDate.getDate()).padStart(2, '0');
const NOW = `${month}月${day}日`;

const header =  {
        "Host": "clashnode.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://clashnode.com/",
        "Connection": "keep-alive",
        "Cookie": "_ga_PXMC8VNYDZ=GS1.1.1696866895.1.1.1696868508.0.0.0; _ga=GA1.2.800438358.1696866895; _pk_ref.1.122d=%5B%22%22%2C%22%22%2C1696866895%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.122d=3892d1df181000b9.1696866895.; _pk_ses.1.122d=1; _gid=GA1.2.2029919306.1696866896",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    }

axios.get('https://clashnode.com/',{headers:header})
.then((res) => {
  var regex = new RegExp(`.*${NOW}.*`, "g");
  var lines = res.data.split('\n');
  var matchedLines = lines.filter(line => regex.test(line));
  if (Array.isArray(matchedLines) && matchedLines.length === 0){
    console.log('今天还没有更新节点')
  } else{
    console.log(matchedLines[0])
    var regex = /href="([^"]+)"/;
    var match = matchedLines[0].match(regex);
    //匹配今天更新的文章地址
    if (match) {
      var href = match[1];
      axios.get(href,{headers:header} )
      .then((res) => {
        var regex = /.*txt.*/g;
        var lines = res.data.split('\n');
        var matchedLines = lines.filter(line => regex.test(line));
        console.log(matchedLines);
        notify.sendNotify('有新节点啦！',matchedLines)
      })
      .catch((error) => {
        console.error(error)
      })
    } else {
      console.log('未找到匹配的 href 地址');
    }    
  }
}).catch((error) => {
  console.error(error)
})
