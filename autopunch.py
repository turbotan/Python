import urllib.request
import socket
import json
import hashlib

baseurl = 'http://api.xbwq.com.cn/wq'

api = "/attendance/clockin"

url = baseurl + api

params = {"acc":"1932.922176838596",
          "com_id":"15",
          "data_open": "0",
          "device":"ios",
          "deviceuuid": "5390201B-5D72-4806-851C-0CF5AEA97C06-1459996023",
          "is_rang":"0",
          "is_wifi_clockin":"0",
          "lat":"30.63325082210554",
          "lng": "103.9776239674156",
          "location":"四川省成都市武侯区簇锦街道武兴四路166-7号西部智谷D区附近",
          "location_type":"4",
          "loc_time":"1511319770",
          "phonemodel":"iPhone 6s iOS11.1.2",
          "power":"63.99999856948853",
          "timesign":"1511319785",
          "type":"2",
          "user":"339183",
          "ver":"2.50",
          "wifi_connect":"1"}

params['key'] = '12345678901234567890'

keys = params.keys()

keys = sorted(keys)

signdata = ''

for key in keys :
    value = urllib.parse.quote(params[key])
    signdata = signdata + key + "=" +value + "&"

signdata = signdata[:len(signdata)-1]

print(signdata)

sign = hashlib.md5(signdata.encode(encoding="utf-8"))
del params['key']
params['sign'] = sign.hexdigest()
print(params['sign'])

postdata = urllib.parse.urlencode(params).encode('utf-8')

requestHeader = {'User-Agent':'Fieldworks/1.1 (iPhone; iOS 11.1.2; Scale/2.00)'}

req = urllib.request.Request(url=url, data=postdata, headers=requestHeader)
result = urllib.request.urlopen(req)
print(result.read())