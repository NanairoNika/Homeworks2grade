import random

def main():
    colloc = {'мобильный' :'телефон',
              'тусклая' :'лампочка',
              'заходящее' :'солнце',
              'воздушный' :'шарик',
              'тюремная' :'камера',
              'кадетский' :'корпус'}
    adjlist = list(colloc.keys())
    word = random.choice(adjlist)
    print (word)
    gword = input("Какое слово загадано? ")
    gword = gword.lower()
    if gword == colloc[word]:
        print ("Хорошая работа! Ты прав!")
    else:
        print ("Нет(. Попробуй в другой раз.")
main()
