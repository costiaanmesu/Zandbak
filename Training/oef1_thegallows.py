# THE GALLOWS
# python oefening
# author: Costiaan Mesu
# date: 20-06-2016

from random import randint

def clrscr():
    print("\n"*255)

#vul woordenlijst
file=open("oef1_thegallows.dict", "r")
dict=[]
for a in file:
    dict.append(a.replace("\n", ""))
file.close()

spelen='j'

while spelen=='j':
    #(re)set scherm en variabelen en voorkom herhaling
    woord = (dict[randint(0, len(dict) - 1)])
    dict.remove(woord)
    missers=0
    correct = ''
    gevraagd=' '
    clrscr()

    while missers < 4 and correct != woord:
        # input en beoordeling
        input_char = input("Geef een letter in: ").lower()[0:1]
        if woord.find(input_char) < 0 and gevraagd.find(input_char) < 0:
            missers += 1
        gevraagd += input_char

        # correcte letters
        correct = ""
        for b in woord:
            if gevraagd.find(b) > 0:
                correct += b
            else:
                correct += "."

        # schermopbouw
        clrscr()
        if missers >= 3:
            print(" ------")
        if missers >= 2:
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
        if missers >= 1:
            print("=======")
        if missers == 4:
            clrscr()
            print("VERLOREN!")
            print(" ------")
            print(" |    |")
            print(" O    |")
            print("\*/   |")
            print("/ \   |")
            print("      |")
            print("=======")
        if correct == woord:
            clrscr()
            print("*-" * 12)
            print("HOERA! JE HEBT GEWONNEN!")
            print("*-" * 12)
            print("")
        print("Geraden letters:", correct)
        print("Gevraagde letters:", gevraagd)
    print("\nHet juiste antwoord was:", woord, "\n")
    #nog een keer?
    spelen=""
    while spelen not in ("j", "n"):
        spelen=input("Nog een spelletje? (j/n)").lower()[0:1]
