import http.client

conn = http.client.HTTPSConnection("services.chanel.com")

payload = ""

headers = {
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'x-requested-with': "XMLHttpRequest"
    }

conn.request("POST", "/en_US/storelocator/getStoreList", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
