arr = []
with open ('freq.txt','r', encoding = 'utf-8') as f:
    arr = f.readlines()
smth = []
while True:
    k = input()
    if k == '':
        break
    else:
        smth.append(k)
for i in smth:
    for line in arr:
        idk = line.split()
        if idk[0] == i:
            print (line)
