import re
def textcleaner(cleanedtxt):
    f = open ('dost1.txt','r', encoding = 'utf-8')
    text = f.read()
    text = text.lower()
    text = text.split()
    for word in text:
        word = word.strip('—!;.,?’:"…()•]«»-')
        cleanedtxt.append(word)
    for word in cleanedtxt:
        if word == '':
            cleanedtxt.remove(word)
    cleanedtxt = ' '.join(cleanedtxt)
    f.close()
    return cleanedtxt
text = []
text = textcleaner(text)
print (text)
