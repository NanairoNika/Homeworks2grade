import html.parser #или просто html если версия после 3.3
import os
import re
import fnmatch
f = open ('205.58.html','r', encoding = 'utf-8')
text = f.read()
f.close()
words = re.findall('<td class=th><a href=.*>\w+</a>', text)
print (words)
def findfiles():
    k=[]
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.html'):
            k.append(file)
    return k

def textopener(t):
    f = open (t,'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text
def cleaner(t):
    regTag = re.compile('<.*?>', re.DOTALL)  
    regScript = re.compile('<script>.*?</script>', re.DOTALL) 
    regComment = re.compile('<!--.*?-->', re.DOTALL)  
    clean_t = regScript.sub("", t)
    clean_t = regComment.sub("", clean_t)
    clean_t = regTag.sub("", clean_t)
    return clean_t
def thwordfinder():
    w = []
    m = findfiles()
    for t in m:
        text = textopener(t)
        words = re.findall('<td class=th><a href=.*></a>', text)
        print (words)
        w.append(words)
        return w

#clthwords = []
#thwords = thwordfinder()
#for word in thwords:
#    clthw = cleaner(word)
#    clthwords.append(clthw)
#print (clthwords)






        
