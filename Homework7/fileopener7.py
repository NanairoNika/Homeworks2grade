tekst=[]
with open('text.txt','r', encoding = 'utf-8') as f:
    for line in f:
        tekst = f.readlines()
m=len(tekst[0]-1)
b=len(tekst[0]-1)
for i in tekst:
    if len(i)-1 > b:
        b = len(i)-1
    if len(i)-1 < m:
        m = len(i)-1
print (b,m)
a = b/m
print (a)
