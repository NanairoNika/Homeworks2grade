s=input()
i = len(s) - 1
p=0
while p <= i:
    if s[p]=='о' or s[p]=='п' or s[p]=='е':
        print (s[p])
        p+=2
    else:
        p+=2
