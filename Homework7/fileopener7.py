tekst=[]
b=0
m=0
f = open('text.txt','r', encoding = 'utf-8')
for line in f:
    if len(line)-1 > b or b==0:
        b = len(line)-1
    if len(line)-1 < m or m==0:
        m = len(line)-1
a = b/m
print (a)
