import re
def linecounter(text):
    counter = 0
    for line in text:
        counter +=1
    return counter


def entries(text):
    lemmas = []
    for line in text:
        if re.search('<w lemma=.+>', line):
            lem = re.search('<w lemma=.+>', line)
            lemmas.append(lem.group(0))
    return lemmas


def dicti(lemmas, freq):
    for word in lemmas:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] +=1
    return freq

def countwriter(counter):
    count = str(counter)
    c = open ('irl.txt','w', encoding = 'utf-8')
    c.write(count)
    c.close()


def dictwriter(freq):
    d = open ('keysirl.txt','w', encoding = 'utf-8')
    for k in sorted(freq):
        d.write(k + '\n')
    d.close()


def findalladj(lemmas):
    adj = []
    for line in lemmas:
        if re.search('type=\"l.f.*', line):
            adj.append(line)
    return adj

def adjdic(adj, adjdicti):
    for word in adj:
        if word not in adjdicti:
            adjdicti[word] = 1
        else:
            adjdicti[word] +=1
    return adjdicti


def adjwriter(adjdicti):
    a = open ('adj.txt','w', encoding = 'utf-8')
    for ad in sorted(adjdicti):
        a.write(ad + ' - ' + str(adjdicti[ad]) + '\n')


def lemmacleaner(lemma):
    cleanlem = []
    for line in lemma:
        line = re.sub('"', '', line)
        line = re.sub('w', '', line)
        line = re.sub('/', '', line)
        line = re.sub('<>', '', line)
        line = re.sub('=', '', line)
        line = re.sub('lemma', '', line)
        line = re.sub('type', ',', line)
        line = re.sub('>', ',', line)
        line = re.sub('<', '', line)
        cleanlem.append(line)
    return cleanlem

def lemmawriter(cllemma):
    l = open ('cllemma.csv','w', encoding = 'utf-8')
    for word in cllemma:
        l.write(word + '\n')
    l.close()
    
            
def main():
    f = open ('irl.xml','r', encoding = 'utf-8')
    text = f.readlines()
    f.close()
    freq = {}
    adjdicti = {}
    counter = 0
    lemmas = []
    adj = []
    cllemma = []
    counter = linecounter(text)
    lemmas = entries(text)
    freq = dicti(lemmas, freq)
    countwriter(counter)
    dictwriter(freq)
    adj = findalladj(lemmas)
    adjdicti = adjdic(adj, adjdicti)
    adjwriter(adjdicti)
    cllemma = lemmacleaner(lemmas)
    lemmawriter(cllemma)


main()

            
    

