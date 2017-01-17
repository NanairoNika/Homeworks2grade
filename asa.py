def textcleaner(cleanedtxt):
    f = open ('Trump.txt','r', encoding = 'utf-8')
    text = f.read()
    text = text.lower()
    text = text.split()
    for word in text:
        word = word.strip('!.,?’:"()•]')
        cleanedtxt.append(word)
    for word in cleanedtxt:
        if word == '':
            cleanedtxt.remove(word)
    f.close()
    return cleanedtxt


def dicti(text, chastota):
    for word in text:
        if word not in chastota:
            chastota[word] = 1
        else:
            chastota[word] +=1
    for word in sorted(chastota):
        if chastota[word] > 10:
            print (word, chastota[word])
def main():
    cleanedtxt = []       
    cleanedtxt = textcleaner(cleanedtxt)
    chastota = {}
    dicti(cleanedtxt, chastota)
main()
    
    

