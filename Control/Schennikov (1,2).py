arr=[]
with open ('freq.txt','r', encoding = 'utf-8') as f:
    arr = f.readlines()
for i in arr:
    if 'союз' in i:
        if 'прл' not in i:
            if 'сущ' not in i:
                print (i)
line = []
ipm = 0
for p in arr:
    if 'жен ' in p:
        if 'ед ' in p:
            line = p.split()
            ipm += float(line[-1])
            print (line[0])
print (ipm)

    
