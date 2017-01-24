import re
def textcleaner(cleanedtxt):
    f = open ('1.txt','r')
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

def find3vow(text):
    for word in text:
        result = re.search('.*[еуэыаоюиёея].*[еуэыаоюиёея].*[еуэыаоюиёея].*', word)
        if result == word:
            print (word)

    
def main():
    text = []
    text = textcleaner(text)
    find3vow(text)

    
main()
