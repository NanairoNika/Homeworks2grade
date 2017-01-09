import random
with open('nouns.txt') as f:
    n1 = f.read()
with open('verbs.txt') as f:
    v1 = f.read()
with open('adj.txt') as f:
    a1 = f.read()
n = n1.split()
v = v1.split()
a = a1.split()
def Verbpast1():
    rverb1 = random.choice(v)
    rverb1 = rverb1[:-2]
    rverb1 = rverb1 + "л"
    return rverb1

def Verbpast2():
    rverb2 = random.choice(v)
    rverb2 = rverb2[:-2]
    rverb2 = rverb2 + "ли"
    return rverb2

def Adj():
    radj = random.choice(a)
    return radj

def Noun1():
    rnoun1 = random.choice(n)
    return rnoun1

def Noun2():
    rnoun2 = random.choice(n)
    rnoun2 = rnoun2 + "е"                    
    return rnoun2

def FirThi():
    Lane13 = Noun1()+" "+Verbpast1()+" "+"на"+" "+Noun2()
    print (Lane13)

def SecFou():
    Lane24 = Adj()+" "+Noun1()+" "+Verbpast2()
    print (Lane24)

FirThi()
SecFou()
FirThi()
SecFou()


