import pickle

class Data():
    def __init__(self):
        self.patienten = []
        self.meettrajecten = []

    def reset(self):
        self.patienten.append(Patient('costiaan@gmail.tk', 'costiaan', 123, 'selfie'))
        self.patienten.append(Patient('rob@gmail.tk', 'rob', 456, 'onesie'))
        self.patienten.append(Patient('hj@gmail.tk', 'henk-jan', 789, 'python'))
        trajectnummer = 0
        while trajectnummer < 3:
            trajectnummer += 1
            traject = Meettraject(trajectnummer)
            lijst = Vragenlijst(1)
            lijst.vragen.append(Vraag('c', 'Welk cijfer zou u de behandeling geven? (1=zeer slecht -10= zeer goed)', 1))
            lijst.vragen.append(Vraag('c', 'Vond u de kliniek goed bereikbaar? (1=totaal niet - 10= uitstekend)', 2))
            lijst.vragen.append(Vraag('o', 'Wilt u nog iets kwijt?', 3))
            traject.vragenlijsten.append(lijst)
            lijst = Vragenlijst(2)
            lijst.vragen.append(Vraag('c', 'Welk cijfer geeft u de nazorg?  (1=zeer slecht -10= zeer goed)', 4))
            lijst.vragen.append(Vraag('c', 'Hoe ervaart u effect van de behandeling op een schaal van 1 tot 10?', 5))
            lijst.vragen.append(Vraag('o', 'Heeft u nog opmerkingen?', 6))
            traject.vragenlijsten.append(lijst)
            lijst = Vragenlijst(3)
            lijst.vragen.append(Vraag('j', 'Bent u tevreden over het resultaat? [j/n]', 7))
            lijst.vragen.append(Vraag('j', 'Zou u ons aanraden bij vrienden?  [j/n]', 8))
            lijst.vragen.append(Vraag('o', 'Nog tips voor ons?', 9))
            traject.vragenlijsten.append(lijst)
            self.meettrajecten.append(traject)

    def load(self):
        try:
            file = pickle.load(open('enquete.pickle', 'rb'))
            return file
        except IOError:
            self.reset()
            return self

    def save(self):
        pickle.dump(self, open('enquete.pickle', 'wb'))


class Patient(object):
    def __init__(self, mail = '', naam = '', nummer = 0, wachtwoord = ''):
        self.mail = mail
        self.naam = naam
        self.nummer = nummer
        self.wachtwoord = wachtwoord
        self.antwoorden = []

    @staticmethod
    def login(patientnummer, wachtwoord):
        for patient in data.patienten:
            if patient.nummer == patientnummer and patient.wachtwoord == wachtwoord:
                return patient


class Meettraject(object):
    def __init__(self, nummer = 0):
        namen = {1: 'Bewegen', 2: 'Zintuigen', 3: 'Huid'}
        self.nummer = nummer
        self.naam = namen[self.nummer]
        self.vragenlijsten =[]

    @staticmethod
    def select(nummer):
        for meettraject in data.meettrajecten:
            if meettraject.nummer == nummer:
                return meettraject


class Vragenlijst(object):
    def __init__(self, nummer=0):
        self.nummer = nummer
        self.vragen = []

    @staticmethod
    def select(patient, meettraject):
        laatste = 0
        if patient.antwoorden:
            for antwoord in patient.antwoorden:
                if antwoord.meettraject.nummer == meettraject.nummer and antwoord.vragenlijst.nummer >= laatste:
                    laatste = antwoord.vragenlijst.nummer
        for vragenlijst in meettraject.vragenlijsten:
            if vragenlijst.nummer == laatste+1:
                return vragenlijst


class Vraag(object):
    def __init__(self, invoertype = '', vraag = '', id = 0):
        self.invoertype = invoertype
        self.vraag = vraag
        self.id = id


class Antwoord(object):
    def __init__(self, antwoord = '', meettraject = None, vragenlijst = None, vraag = None):
        self.antwoord = antwoord
        self.meettraject = meettraject
        self.vragenlijst = vragenlijst
        self.vraag = vraag

    def is_valid(self):
        if self.vraag.invoertype == 'c' and self.antwoord.isdigit() and 1 <= int(self.antwoord) <= 10:
            return True
        elif self.vraag.invoertype == 'j' and self.antwoord.lower()[:1] in ('j', 'n'):
            return True
        elif self.vraag.invoertype not in ('c', 'j'):
            return True
        else:
            return False

class UI: #USER INTERFACE

    @staticmethod
    def input_login():
        user = int(input('Patientnummer: '))
        password = input('Wachtwoord: ')
        return user, password

    @staticmethod
    def input_meettraject():
        trajectnummer=0
        while trajectnummer not in ('1', '2', '3'):
            trajectnummer = input('ZorgMeettraject? [1 = Bewegen, 2 = Zintuigen, 3 =  Huid] ')
        return int(trajectnummer)

    @staticmethod
    def input_antwoord(vraag):
        antwoord=input(vraag.vraag)
        return antwoord

    @staticmethod
    def invalid_login(user, data):
        for patient in data.patienten:
            if patient.nummer == user:
                print('Verkeerde wachtwoord')
                break
        if patient.nummer != user:
            print('Patient bestaat niet')

    @staticmethod
    def invalid_answer(vraag):
        invoertypes = {'c': 'cijfer', 'j': 'ja of nee', 'o': 'opmerking'}
        print('Ongeldige invoer, voer een %s in' % invoertypes[vraag.invoertype])

    @staticmethod
    def output_answers(patient):
        for antwoord in patient.antwoorden:
            print(antwoord.meettraject.naam + ' - ' + antwoord.vraag.vraag + ' = ' + antwoord.antwoord)



if __name__ == '__main__':
    data = Data().load()
    user, password = UI.input_login()
    patient = Patient.login(user, password)
    while patient == None:
        UI.invalid_login(user, data)
        user, password = UI.input_login()
        patient = Patient.login(user, password)
    print('Ingelogd als: %s' % patient.naam)
    data.patienten.remove(patient)
    meettrajectnummer = UI.input_meettraject()
    meettraject = Meettraject.select(meettrajectnummer)
    print('Meettraject: %s' % meettraject.naam)
    vragenlijst = Vragenlijst.select(patient, meettraject)
    if vragenlijst:
        for vraag in vragenlijst.vragen:
            user_antwoord = UI.input_antwoord(vraag)
            antwoord = Antwoord(user_antwoord, meettraject, vragenlijst, vraag)
            while not antwoord.is_valid():
                UI.invalid_answer(vraag)
                user_antwoord = UI.input_antwoord(vraag)
                antwoord = Antwoord(user_antwoord, meettraject, vragenlijst, vraag)
            patient.antwoorden.append(antwoord)

    else:
        print('U heeft alle vragenlijsten voor dit meettraject ingevuld')
    data.patienten.append(patient)
    data.save()




