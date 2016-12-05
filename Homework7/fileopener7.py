tekst=[]
with open('text.txt','r', encoding = 'utf-8') as f:
    smth = f.read()
    smth = smth.replace('\n',' ')
    tekst = smth.split(' ') 
m=len(tekst[0])
b=len(tekst[0])
for i in tekst:
    if len(i) > b:
        b = len(i)
    if len(i) < m:
        m = len(i)
a = b/m
print (a)
