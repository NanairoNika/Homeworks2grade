def textcleaner():
    f = open ('Trumpy.txt','r', encoding = 'utf-8')
    text = f.read()
    text = text.lower()
    text = text.replace(",","")
    text = text.replace(".","")
    text = text.replace("!","")
    text = text.replace("?","")
    text = text.replace("»","")
    text = text.replace("«","")
    text = text.replace(":","")
    text = text.split()
    f.close()
    return text
    
    
def nessseek(text, lst):
    p = 0
    for i in text:
        if i[-4:] == 'ness':
            lst.append(i)
    return lst
    
    
def nesscomp(lst):
    d = 0
    k = 0
    themu = []
    for i in lst:
        numb = 0
        numb = lst.count(i)
        if numb == d:
            for z in themu:
                k = 0
                if z == i:
                    k += 1
            if k == 0:
                themu.append(i)
        if numb > d:
            d = numb
            themu = [i]
    return themu


def countness(lst):
    unique = []
    for i in lst:
        k = 0
        for z in unique:
            if i == z:
                k += 1
        if k == 0:
            unique.append(i)
    h = len(unique)
    return h
	
	
def main():
    trump = textcleaner()
    nesswords = []
    freq = []
    nesswords = nessseek(trump, nesswords)
    count = countness(nesswords)
    freq = nesscomp(nesswords)
    print ('Tne number of unique words with ness: ', count)
    print ('The most frequent word/s with ness: ', freq)


main()
