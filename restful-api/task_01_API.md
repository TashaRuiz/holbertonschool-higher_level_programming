>curl -I https://jsonplaceholder.typicode.com/posts

HTTP/2 200 
date: Fri, 13 Nov 2026 17:37:44 GMT
content-type: application/json; charset=utf-8
access-control-allow-credentials: true
cache-control: max-age=43200
report-to: {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=9le32cFRUny%2Fm4L5RAvwS1Qyyf%2BQgHPlogkyNXZsi5utDucGHgPNDYTJ5HrI7Qer87Gmv1WY0O9tyU5w1%2BTth5VdRKduF8p%2BfApPIAKa2mTlPhJvadZ%2FRmJVIoV7z4ingdMK2TKQeDyYTlpQAizI2uktimitTDg%2FaaQy"}]}
etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
expires: -1
pragma: no-cache
vary: Origin, Accept-Encoding
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 3600000
x-ratelimit-remaining: 3599998
x-ratelimit-reset: 1793985019
nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
cf-cache-status: HIT
server: cloudflare
cf-ray: a59f8bcabfedcbd1-SJU
alt-svc: h3=":443"; ma=86400

>curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```