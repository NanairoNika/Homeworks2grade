import re
def textcleaner():
    cleanedtxt = []
    f = open ('chin.txt','r', encoding = 'utf-8')
    text = f.read()
    text = text.split()
    for word in text:
        word = word.strip('!;.,?’:"…()•]')
        word = word.strip('\n')
        cleanedtxt.append(word)
    for word in cleanedtxt:
        if word == '':
            cleanedtxt.remove(word)
    cltxt = ' '.join(cleanedtxt)
    f.close()
    return cltxt
def main():
    satt = []
    text = []
    text = textcleaner()
    satt = re.findall('«.+»', text)
    print(satt)
main()
