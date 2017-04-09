import re
def textcleaner():
    f = open ('lat.txt','r', encoding = 'utf-8')
    text = ()
    text = f.read()
    text = text.replace("!",".")
    text = text.replace("?",".")
    text = text.split('.')
    f.close()
    return text


def sentmas(text):
    divsent = []
    clsent = []
    for sent in text:
        sent = sent.split()
        divsent.append(sent)
    return divsent


def sentfinder(divsent):
    tensent = []
    for sent in divsent:
        l = 0
        for word in sent:
            l+=1
        if l > 10:
            tensent.append(sent)
    return tensent


def wordfinder(tensent):
    bwords = []
    for sent in tensent:
        for word in sent:
            bw = re.search('\s*[А-Я].*', word)
            if bw:
                bwords.append(word)
    return bwords


def main():
    text = textcleaner()
    divsent = sentmas(text)
    tensent = sentfinder(divsent)
    bwords = wordfinder(tensent)
    print (bwords)
main()
