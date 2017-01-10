def textcleaner():
    f = open ('Bulg.txt','r', encoding = 'utf-8')
    text = f.read()
    text = text.lower()
    text = text.replace(",","")
    text = text.replace(".","")
    text = text.replace("!","")
    text = text.replace("?","")
    text = text.replace("»","")
    text = text.replace("«","")
    text = text.split()
    f.close()
    return text


def vowelsearch(text, n):
    for i in text:
        numb = 0
        vow = ["ё", 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'ю', 'е']
        for p in i:
            if p in vow:
                numb = numb + 1
        if numb == n:
            print (i)
    print ("Попробуйте ещё раз")

    
def firstletter(text, l):
    for i in text:
        if i[0] == l:
            print (i)
    print ("Попробуйте ещё раз")

    
def choose(text):
    c = int(input("Вы хотите узнать слова со слогами (Введите 1) или вы хотите узнать слова на определенную букву (Введите 2) ==> "))
    if c == 1:
        n = int(input("Введите количесвто слогов ==> "))
        vowelsearch(text, n)
    if c == 2:
        l = input("Введите букву на которую должно начинаться слово ==> ")
        firstletter(text, l)

        
def main():
    cltex = textcleaner()
    choose(cltex)
main()



