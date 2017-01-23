# THE GALLOWS
# python oefening
# author: Costiaan Mesu
# date: 20-06-2016

from random import randint

#vul woordenlijst voor alle spellen
f=open("oef1_thegallows.dict", "r")
d=[]
for a in f:
    d.append(a.replace("\n", ""))
f.close()

#functies
def cls():
    print("\n"*255)


#klasse
class WordObject(object):
    def __init__(self):
        self._antwoord=(d[randint(0, len(d) - 1)])
        d.remove(self._antwoord)
        self._correct = ""
        self._gevraagd=" "
        self._missers=0

    def correct(self):
        self._correct=''
        for b in self._antwoord:
            if self._gevraagd.find(b)>0:
                self._correct+=b
            else:
                self._correct += "."
        return self._correct

    def input(self):
        if self.afgelopen()==0:
            i=input("Geef een letter in: ").lower()[0:1]
            if self._antwoord.find(i) < 0 and self._gevraagd.find(i) < 0:
                self._missers+=1
            self._gevraagd+=i
            self.correct()

    def output(self):
        cls()
        if self._missers >= 3:
            print(" ------")
        if self._missers >= 2:
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
        if self._missers >= 1:
            print("=======")
        if self.afgelopen() == 1 and self._missers >= 4:
            cls()
            print("VERLOREN!")
            print(" ------")
            print(" |    |")
            print(" O    |")
            print("\*/   |")
            print("/ \   |")
            print("      |")
            print("=======")
        elif self.afgelopen() == 1:
            cls()
            print("*-" * 12)
            print("HOERA! JE HEBT GEWONNEN!")
            print("*-" * 12)
            print("")
        print("Geraden letters:", self.correct())
        print("Gevraagde letters:", self._gevraagd)

    def afgelopen(self):
        if (self._antwoord == self._correct or self._missers>=4):
            return 1
        else: return 0

    def antwoord(self):
        return self._antwoord


spelen="j"

#main
while spelen=="j":
    woord=WordObject()
    cls()

    while woord.afgelopen()==0:
        #print(woord.antwoord())
        woord.input()
        woord.output()

    print("\nHet juiste antwoord was:", woord.antwoord(), "\n")
    spelen=""
    while spelen not in ("j", "n"):
        spelen=input("Nog een spelletje? (j/n)").lower()[0:1]



