/*
cron: 9 * * *
京东读书签到
*/
const notify = require('./sendNotify')
const axios = require('axios')
function version() {
    return new Promise(function (resolve, reject) {
        resolve(axios.get("https://gitee.com/naro_li/statement/raw/main/naro-scripts"))
    })
}

async function main() {
    await version().then(data => { console.log(data.data) })
    axios.post(
        'https://jdread-api.jd.com/jdread/api/activity/sign',
        {
            'effective_date': '2024-06-09',
            'sign_type': 0
        },
        {
            params: {
                'eventFrom': '1',
                'build': '202312240',
                'client': 'ipad',
                'cv': '4.29.1',
                'dv': 'ffvf6oqbikAzvP1oFTE9Wcskf94TZbLc4RJWmgN5rXspHxWAXBiY6lGe8A83mfSC',
                'ec': 'i6VU0uAIat/S8saW0LcoI1wOZ+m+h88jeDOai8DdRE7e2JBTj/xgPLC1+6CYjZtXYhLE3ApH1f7aqc9KG5ARlQV46o3knP8RuuFsyYnqnVdZ67egGxTgUwR/rVr3TTjY33Wj4Yzl5Pchwv52NXfYSGT2QashcMiyWkHbX0RcI91PFNGlJ+iSbZINb/chLjok2BBC+b9PJQmTOdMcZkelqA',
                'os': 'ios',
                'statusHeight': '20',
                'suid': 'ipad',
                'tm': '1717810183106',
                'uid': 'ipad',
                'app': 'jdread-m',
                'encdv': '1',
                'sign': 'f3b6df5d34eacf7c823fb5c8a2c36ab2'
            },
            headers: {
                'Host': 'jdread-api.jd.com',
                'reqtime': '1717810183106',
                'Accept': 'application/json',
                'isencrypt': 'false',
                'Sgm-Context': '455447510437088100;455447510437088100',
                'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'Origin': 'https://jdread-api.jd.com',
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 JDRead 4.29.1 rv:202312240 (iPad; iPadOS 15.7; zh_CN; jdread-app) darkMode=false',
                'Referer': 'https://jdread-api.jd.com/h5/p_sign_in?eventFrom=1&app=jdread-app&build=202312240&client=ipad&cv=4.29.1&dv=uiqGNC-k5SVGlAvMftFVunR5jdOGsOrlh4zwoU_QI6pchLRbPk2CBGBoOQw4Gz2j&ec=Sa1BljLc7N3CYv4VU%2FZhtXLksSyBC6BXceMIsaB0X0N4F2%2BDXadDpCGVOZoNnUAZua8MOgSEBPo7VNoDwKOXdQ6RJQvMwhEwG3oF8CA86aFrUOEPlt%2B1YrVQk66A9L%2F2UYX%2BpdiBxjcR241RzaNbCgib5z7%2B1ndiogv2d%2FwmU30L8Nb3uezFVlxoqq%2Fy6usTt0KrGXuUDRJaODPLElewqw%3D%3D&os=ios&statusHeight=20&suid=ipad&tm=1717810178124&uid=ipad',
                'Content-Length': '45',
                'Connection': 'keep-alive',
                'Cookie': process.env.JDREAD
            }
        }
    ).then((res) => {
        console.log(res.data)
        notify.sendNotify('签到结果', JSON.stringify(res.data));
    }).catch((error) => {
        console.error(error)
    })
}
main()
