def textcleaner(cleanedtxt):
    f = open ('rur.txt','r', encoding = 'utf-8')
    text = f.read()
    text = text.lower()
    text = text.split()
    for word in text:
        word = word.strip('!.,?’:"—()•]')
        cleanedtxt.append(word)
    for word in cleanedtxt:
        if word == '':
            cleanedtxt.remove(word)
    f.close()
    return cleanedtxt


def wordcounter(text):
    counter = 0
    for word in text:
        counter += 1
    return counter

def dicti(text, freq):
    for word in text:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] +=1
    return freq


def dictiwriter(freq):
    f = open ('rur.csv','w', encoding = 'utf-8')
    for k in sorted(freq):
        f.write(k + ',' + str(freq[k]) + '\n')
            

def main():
    cleanedtext = []
    counter = 0
    freq = {}
    cleanedtext = textcleaner(cleanedtext)
    counter = wordcounter(cleanedtext)
    freq = dicti(cleanedtext, freq)
    dictiwriter(freq)
    print (counter)


main()
