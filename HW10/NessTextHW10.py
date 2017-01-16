def textcleaner():
    f = open ('Trump.txt','r', encoding = 'utf-8')
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
            p = p + 1
            lst.append(i)
    return p, lst
    
    
def nesscomp(lst):
    d = 0
    k = 0
    themu = []
    for i in lst:
        numb = 0
        for p in lst:
            if i == p:
                numb = numb + 1
        if numb == d:
            for z in themu:
                if z == i:
                    k = k + 1
                if k == 0:
                    themu.append(i)
        if numb > d:
            d = numb
            themu = [i]
    return themu
	
	
def main():
    trump = textcleaner()
    nesswords = []
    freq = []
    count, nesswords = nessseek(trump, nesswords)
    print ('Tne number of words with ness: ', count)
    freq = nesscomp(nesswords)
    print ('The most frequent word/s with ness: ', freq)


main()
    

