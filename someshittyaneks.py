import urllib.request
import json
req = urllib.request.Request('https://api.vk.com/method/wall.get?domain=baneks&offset=1&count=50&v=5.73&access_token=7422af727422af727422af721b744083d2774227422af722ee34a6cd72ebf36222c09ec') 
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
data = json.loads(result)
print (data["response"]["count"])
for i in range (50):
    try:
        print(data["response"]["items"][i]["text"])
    except:
        pass
