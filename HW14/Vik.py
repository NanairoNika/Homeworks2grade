import re


def textcleaner():
    f = open ('Vik.txt','r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text


def ViktoBars(text):
    text = re.sub('Викинг', 'Барсук', text)
    text = re.sub('викинг', 'барсук', text)
    return text


def textwritter(bars):
    f = open ('Bars.txt', 'w', encoding = 'utf-8')
    f.write(bars)

    
def main():
    text = textcleaner()
    bars = ViktoBars(text)
    textwritter(bars)

    
main()
