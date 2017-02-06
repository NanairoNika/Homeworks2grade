import re
f = open ('cons.html' , 'r', encoding = 'utf-8')
text = f.read()
UTC = re.findall('UTC\+[1234567890]', text)


