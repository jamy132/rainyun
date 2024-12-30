import http.client

conn = http.client.HTTPSConnection("api.v2.rainyun.com")
payload = ''
headers = {
   'x-api-key': '{{m8YSSEQLKsbl2BHAOqNEB5VL1CddvupP}}',
}
conn.request("POST", "/user/reward/tasks", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
