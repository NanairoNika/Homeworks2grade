import urllib.request
import re
import os

def siteopener():
    req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
    with urllib.request.urlopen(req) as response:
       html = response.read().decode('utf-8')
    return html

def cleaner(text):
    text = re.sub('<script>.*?</script>', ' ', text)
    text = re.sub('<!--.*?-->', ' ', text)
    text = re.sub('<.*?>', ' ', text)
    return text

def wordsfinder():
    file = siteopener()
    file = cleaner(file)
    words = re.findall(r'\w+', file)
    return words

def Swords(words):
    swr = []
    for k in words:
        if k[0] == 'с':
            swr.append(k)
    return swr

def duplicatedel(swr):
    shortswr = []
    for i in swr:
        c = 0
        for z in shortswr:
            if i == z:
                c += 1
        if c == 0:
            shortswr.append(i)
    return shortswr

def printf(mass):
    for i in mass:
        print (i)
        
def markup(lst):
    string = '\n'.join(lst)
    f = open ('C:\input.txt', 'w', encoding = 'utf-8')
    f.write(string)
    f.close
    
def main():
    allwords = wordsfinder()
    allswords = Swords(allwords)
    allswords = duplicatedel(allswords)
    printf(allswords)
    markup(allswords)

main()
os.system("C:/mystem.exe -nid C:/input.txt  C:/output.txt")
with open('C:/output.txt', encoding = 'utf-8') as f:
    my_crawl = f.readlines()
for i in my_crawl:
    if re.match(".*=V.*", i):
            print(i) 
