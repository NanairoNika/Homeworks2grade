import urllib.request
import json

lengthall = []
lengthcommall = []
idall = []

def posts(requestlink):
   req = urllib.request.Request(requestlink)
   response = urllib.request.urlopen(req)
   result = response.read().decode('utf-8')
   data = json.loads(result)
   return data
def lengthandid(lengthall,idall, data):
    for p in range(100):
        try:
            text = data["response"]["items"][p]["text"].split()
            lengthall.append(len(text))
            idall.append(data["response"]["items"][p]["id"])
        except:
            pass
    return lengthall,idall
def getcomments(requestlink):
    req = urllib.request.Request(requestlink)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    data = json.loads(result)
    return(data)
data1 = posts('https://api.vk.com/method/wall.get?domain=baneks&offset=0&count=100&v=5.73&access_token=7422af727422af727422af721b744083d2774227422af722ee34a6cd72ebf36222c09ec')
data2 = posts('https://api.vk.com/method/wall.get?domain=baneks&offset=99&count=100&v=5.73&access_token=7422af727422af727422af721b744083d2774227422af722ee34a6cd72ebf36222c09ec')
lengthall, idall = lengthandid(lengthall, idall, data1)
lengthall, idall = lengthandid(lengthall, idall, data2)
for i in idall:
    data = getcomments('https://api.vk.com/method/wall.getComments?domain=baneks&post_id'+str(i)+'offset=0&count=100&v=5.73&access_token=7422af727422af727422af721b744083d2774227422af722ee34a6cd72ebf36222c09ec')
    for p in range(100):
        try:
            text = data["response"]["items"][p]["text"].split()
            lengthcommall.append(len(text))
        except:
            pass
print(lengthcommall)
