import re
f = open ('cons.html' , 'r', encoding = 'utf-8')
text = f.read()
UTC = re.findall('UTC\+[1234567890]+', text)
consttime = [UTC[0]]
counter = 0
def WintSummTime
    for time in UTC:
        for swtime in consttime:
            if time == swtime:
                counter += 1
        if counter == 0:
            consttime.append(time)
        counter = 0
print ('Зимнее время >', consttime[0])
print ('Летнее время >', consttime[1])
