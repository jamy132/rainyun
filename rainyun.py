import http.client
import json

conn = http.client.HTTPSConnection("api.v2.rainyun.com")
payload = json.dumps({
   "task_name": "每日签到"
})
headers = {
   'x-api-key': '{m8YSSEQLKsbl2BHAOqNEB5VL1CddvupP}',
   'User-Agent': 'Mozilla/5.0',
   'Content-Type': 'application/json'
}
conn.request("POST", "/user/reward/tasks", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
