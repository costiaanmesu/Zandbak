class Patient(object):
    def __init__(self):
        self.naam = ''
        self.nummer = 0
        self.code = ''
        self.antwoorden = []

    def login(self, code):
        if code == self.code:
           return True
    

class Vragenlijst(object):
    def __init__(self, vragenlijst_nummer):
        self.nummer = vragenlijst_nummer
        self.soort_klacht = ''
        self.vragen = []

    def get_user_input(self, patient):
        for vraag in self.vragen:
           vraag.stel(patient)

class Vraag:
    def __init__(self, nummer, tekst):
        self.nummer = nummer
        self.tekst = tekst

    def stel(self, patient):
        inp = input(self.tekst)
        a = Antwoord()
        a.vraag = self
        a.patient = patient
        a.antwoord = inp
        patient.antwoorden.append(a)

class Meerkeuze(Vraag):
    pass



pat = Patient()
pat.code = 'geheim'
if pat.login('geheim2'):
    print('ingelogd')

vragenlijst = Vragenlijst('T0-algemeen')
vragenlijst.soort_klacht = 'Alle'
vragenlijst.vragen.append(Vraag(1, 'wat is uw leeftijd?'))
vragenlijst.vragen.append(Vraag(2, 'wat is uw gewicht?'))
vragenlijst.vragen.append(Vraag(3, 'wat is uw geslacht?'))

vragenlijst2 = Vragenlijst('T0-heup')
vragenlijst2.vragen.append(Vraag(1, 'pijn op schaal van 1-10'))

vragenlijst.get_user_input(pat)
vragenlijst2.get_user_input(pat)
