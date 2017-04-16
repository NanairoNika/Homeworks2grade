import re
import os


def Seeker():
    files = os.listdir()
    nofold = []
    for file in files:
        if os.path.isfile(file):
            nofold.append(file)
    return nofold


def numbseek(nofold):
    numb = []
    for name in nofold:
        if re.match('.*[0-9]+.*', name):
            numb.append(name)
    return numb


def copyquit(numb):
    copied = []
    uncopied = []
    for name in numb:
        diviz = re.split('\.', name)
        copied.append(diviz[0])
    for name1 in copied:
        i=0
        for name2 in copied:
            if name1==name2:
                i+=1
        if i==1:
            uncopied.append(name1)
    return uncopied
            
            
def main():    
    nofold = Seeker()
    numb = numbseek(nofold)
    uncopied = copyquit(numb)
    print (uncopied, len(numb))


main()
