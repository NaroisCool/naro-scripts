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
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJQWEI3LUZST05ULkFQSSIsImV4cCI6MTcxMzA1MTQwMSwiYXVkIjoiYWRtaW4iLCJuYmYiOjE3MTMwMDgyMDEsImlhdCI6MTcxMzAwODIwMSwidXNlciI6eyJ1c2VyX2lkIjo1NjI4NjU3LCJ1c2VyX3NuIjoiVFUyTlpDIiwiZW1haWwiOiIiLCJxcSI6IiIsInVzZWRfcXEiOiIxMjAzMTQxNjA5IiwidXNlZF93eCI6IjE3NTAzMDYxMTE5IiwidXNlZF9waG9uZSI6IjE3NTAzMDYxMTE5IiwicGFzc3dvcmQiOiJlOTk0YjFkNzIyNjYzNTkyZmJhYzExY2FkMjg5MzdmYSIsImNvbnRhY3QiOiIiLCJhdmF0YXIiOiIiLCJyZWFsbmFtZSI6IiIsInRlbHBob25lIjoiMTc1MDMwNjExMTkiLCJjb3VudHJ5X2NvZGUiOiI4NiIsImFkZHJlc3MiOiIiLCJwb3N0Y29kZSI6IiIsInNleCI6MSwibmlja25hbWUiOiJcdTc1MjhcdTYyMzdfMTcxMjQ5MjI5MTE5IiwiZGVmaW5lZCI6bnVsbCwiY2VydF9uYW1lIjoiXHU2NzRlXHU1MDY1IiwiY2VydF9pZCI6IjM2MjIwMTE5OTQxMTE5MzQxWCIsImNlcnRfdGVscGhvbmUiOm51bGwsImF1dGhfc3RhdGUiOjEsImF1dGhfaWQiOm51bGwsImxhc3RfbG9naW4iOiIxNzEzMDA4MjAwIiwibGFzdF9pcCI6IjExNy4xNjYuNTIuNzgiLCJsb2dpbl9jb3VudCI6NiwiYWRkX3RpbWUiOjE3MTI0OTIyOTEsImFkZF9zb3VyY2UiOjEsImxhc3RfY2hlY2tfYmxhY2siOjAsInRvdXhpYW5nIjoiaHR0cHM6XC9cL20xLnB4YjcuY29tXC9pbWFnZVwvbXlcL2F2YXRhclwvYXZhdGFyMS5wbmciLCJhbGlwYXkiOiIiLCJhbGlwYXlfcXJjb2RlIjoiIiwid2VjaGF0IjpudWxsLCJ3ZWNoYXRfcXJjb2RlIjoiIiwiYmFua2NhcmQiOiIiLCJiYW5rX3JlYWxuYW1lIjoiIiwiYmFua19hZGRyZXNzIjoiIiwicGF5cHdkIjoiIiwibm93X21vbmV5IjoiMC4wMCIsInVzZXJfbm90ZSI6IiIsImxvZ291dF90aW1lIjowLCJjYW5jZWxlZCI6MCwiY2FuY2VsZWRfc291cmNlIjowLCJmZGRfdWlkIjpudWxsLCJmZGRfdHJhbnNhY3Rpb25fbm8iOm51bGwsImxvY2tpbmciOjAsInB1c2hfY29udHJvbGwiOjEsInd4YV9vcGVuaWQiOiIiLCJweF9jaGFubmVsX3VzZXJfaWQiOjAsImRvd25sb2FkX2NoYW5uZWxfaWQiOjAsIm1lbWJlcnNoaXAiOjEsImRldmljZV9maW5nZXJwcmludCI6IjcyNzMwMmIxMTgzNDlkOTkzNGQwOGYwMDNjZDA0YjZhIiwiaW1fY29udHJvbGwiOjEsImludml0YXRpb25fY29kZSI6IiIsInVuaW9uX2lkIjoibzBlRnI1b21kVXRtYzdHQ0ZIZGF3UTQ5X3F0cyIsIm9mZmljaWFsX29wZW5pZCI6Im9odzZRNTc5WWFjYndwYTBsUmJXMkJkN0x4MHMiLCJhcHBfb3BlbmlkIjoiIiwid3hfbmlja25hbWUiOiJUZWNoTGVlIiwiaXNfc3Vic2NyaWJlIjowLCJpc19iaW5kX3dlY2hhdCI6MSwiYWxpcGF5X29wZW5pZCI6IiJ9fQ.W2Moxo7x2uz-xeoAlAJt2rhtOixTUJgwvglR-gA033g",
        "LoginStatus": "true",
        "x-fronend-tcpport": "5628657",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
const payload = "{\"game_id\":61,\"product_id\":113576}"

axios.post('https://api.pxb7.com/api/product/gore',payload,{headers:header} )
.then((res) => {
  console.log(res.data)
})
.catch((error) => {
  console.error(error)
})
