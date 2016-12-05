tekst=[]
f = open('text.txt','r', encoding = 'utf-8')
for line in f:
        tekst = f.readlines()
m=len(tekst[0])
b=len(tekst[0])
print(tekst)
print(m,b)
for i in tekst:
    print (i)
    print (len(i))
    if len(i)-1 > b:
        b = len(i)-1
    if len(i)-1 < m:
        m = len(i)-1
print (b,m)
a = b/m
print (a)
