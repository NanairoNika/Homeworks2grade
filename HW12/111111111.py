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
    f.close()
    return cleanedtxt
def main():
    text = []
    findfind = []
    text = textcleaner(text)
    for word in text:
        iigood = re.search('на((й(т|д)(и|у|ё)(т?|шь|м)?е?)|(хо(жу|д(и|я)(м|шь|те|т)?))|(шё?л(и|а)?))', word)
        if iigood:
            findfind.append(word)
    print(findfind)
main()
