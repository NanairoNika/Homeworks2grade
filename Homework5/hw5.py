s = input()
B = s.split()
A = []
while B != []:
    if len(s) > 5:
        A += B
    s = input()
    B = s.split()
for x in A: 
    print(x)
