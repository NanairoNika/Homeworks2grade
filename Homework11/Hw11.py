import random
def textcleaner(cleanedtxt):
    f = open ('1.csv','r', encoding = 'utf-8')
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


def dictmaker(text, dicti):
    k = 0
    v = 1
    keys = []
    values = []
    while k < len(text):
        keys.append(text[k])
        k += 2
    while v < len(text):
        values.append(text[v])
        v += 2
    dicti = dict(zip(keys, values))
    return dicti

def riddle(dicti):
    adjlist = list(dicti.keys())
    word = random.choice(adjlist)
    print (word)
    gword = input("Какое слово загадано? ")
    gword = gword.lower()
    if gword == dicti[word]:
        print ("Хорошая работа! Ты прав!")
    else:
        print ("Нет(. Попробуй в другой раз.")

def main():
    dicti = {}
    col = []
    col = textcleaner(col)
    dicti = dictmaker(col, dicti)
    riddle(dicti)


main()
