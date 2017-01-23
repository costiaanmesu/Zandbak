import pickle

class Data():
    patienten = []
    meettrajecten = []
    vragen = []
    antwoorden = []

    Meettrajectnamen = {1: 'Bewegen', 2: 'Zintuigen', 3: 'Huid'}
    invoertypes = {'c': 'cijfer', 'j': 'ja of nee', 'o': 'opmerking'}

    def reset():
        Data.patienten.append(Patient('costiaan@gmail.com', 'costiaan', 123, 'selfie'))
        Data.patienten.append(Patient('rob@gmail.com', 'rob', 456, 'onesie'))
        Data.patienten.append(Patient('hj@gmail.com', 'henk-jan', 789, 'python'))

        Data.vragen.append(Vraag('c', 1, 1, 'Welk cijfer zou u de behandeling geven? (1=zeer slecht -10= zeer goed)', 1, 1))
        Data.vragen.append(Vraag('c', 1, 2, 'Vond u de kliniek goed bereikbaar? (1=totaal niet - 10= uitstekend)', 2, 1))
        Data.vragen.append(Vraag('o', 1, 3, 'Wilt u nog iets kwijt?', 3, 1))
        Data.vragen.append(Vraag('c', 1, 1, 'Welk cijfer geeft u de nazorg?  (1=zeer slecht -10= zeer goed)', 4, 2))
        Data.vragen.append(Vraag('c', 1, 2, 'Hoe ervaart u effect van de behandeling op een schaal van 1 tot 10?', 5, 2))
        Data.vragen.append(Vraag('o', 1, 3, 'Heeft u nog opmerkingen?', 6, 2))
        Data.vragen.append(Vraag('j', 1, 1, 'Bent u tevreden over het resultaat? [j/n]', 7, 3))
        Data.vragen.append(Vraag('j', 1, 2, 'Zou u ons aanraden bij vrienden?  [j/n]', 8, 3))
        Data.vragen.append(Vraag('o', 1, 3, 'Nog tips voor ons?', 9, 3))
        Data.vragen.append(Vraag('c', 2, 1, 'Welk cijfer zou u de behandeling geven? (1=zeer slecht -10= zeer goed)', 10, 1))
        Data.vragen.append(Vraag('c', 2, 2, 'Vond u de kliniek goed bereikbaar? (1=totaal niet - 10= uitstekend)', 11, 1))
        Data.vragen.append(Vraag('o', 2, 3, 'Wilt u nog iets kwijt?', 12, 1))
        Data.vragen.append(Vraag('c', 2, 1, 'Welk cijfer geeft u de nazorg?  (1=zeer slecht -10= zeer goed)', 13, 2))
        Data.vragen.append(Vraag('c', 2, 2, 'Hoe ervaart u effect van de behandeling op een schaal van 1 tot 10?', 14, 2))
        Data.vragen.append(Vraag('o', 2, 3, 'Heeft u nog opmerkingen?', 15, 2))
        Data.vragen.append(Vraag('j', 2, 1, 'Bent u tevreden over het resultaat? [j/n]', 16, 3))
        Data.vragen.append(Vraag('j', 2, 2, 'Zou u ons aanraden bij vrienden?  [j/n]', 17, 3))
        Data.vragen.append(Vraag('o', 2, 3, 'Nog tips voor ons?', 18, 3))
        Data.vragen.append(Vraag('c', 3, 1, 'Welk cijfer zou u de behandeling geven? (1=zeer slecht -10= zeer goed)', 19, 1))
        Data.vragen.append(Vraag('c', 3, 2, 'Vond u de kliniek goed bereikbaar? (1=totaal niet - 10= uitstekend)', 20, 1))
        Data.vragen.append(Vraag('o', 3, 3, 'Wilt u nog iets kwijt?', 21, 1))
        Data.vragen.append(Vraag('c', 3, 1, 'Welk cijfer geeft u de nazorg?  (1=zeer slecht -10= zeer goed)', 22, 2))
        Data.vragen.append(Vraag('c', 3, 2, 'Hoe ervaart u effect van de behandeling op een schaal van 1 tot 10?', 23, 2))
        Data.vragen.append(Vraag('o', 3, 3, 'Heeft u nog opmerkingen?', 24, 2))
        Data.vragen.append(Vraag('j', 3, 1, 'Bent u tevreden over het resultaat? [j/n]', 25, 3))
        Data.vragen.append(Vraag('j', 3, 2, 'Zou u ons aanraden bij vrienden?  [j/n]', 26, 3))
        Data.vragen.append(Vraag('o', 3, 3, 'Nog tips voor ons?', 27, 3))

        Data.meettrajecten.append(Meettraject(456, 2, 1))
        Data.meettrajecten.append(Meettraject(123, 2, 1))
        Data.meettrajecten.append(Meettraject(123, 3, 1))
        Data.meettrajecten.append(Meettraject(123, 1, 1))

        Data.antwoorden.append(Antwoord(10, 123, 13))
        Data.antwoorden.append(Antwoord(6, 123, 14))
        Data.antwoorden.append(Antwoord('geen suggesties', 123, 15))
        Data.antwoorden.append(Antwoord('j', 123, 16))
        Data.antwoorden.append(Antwoord('n', 123, 17))
        Data.antwoorden.append(Antwoord('betere koffie', 123, 18))
        Data.antwoorden.append(Antwoord('j', 123, 25))
        Data.antwoorden.append(Antwoord('j', 123, 26))
        Data.antwoorden.append(Antwoord('test2', 123, 27))
        Data.antwoorden.append(Antwoord(6, 123, 4))
        Data.antwoorden.append(Antwoord(8, 123, 5))
        Data.antwoorden.append(Antwoord('professioneel bedrijf', 123, 6))
        Data.antwoorden.append(Antwoord(3, 123, 22))
        Data.antwoorden.append(Antwoord(2, 123, 23))
        Data.antwoorden.append(Antwoord('nee', 123, 24))
        Data.antwoorden.append(Antwoord('j', 123, 7))
        Data.antwoorden.append(Antwoord('n', 123, 8))
        Data.antwoorden.append(Antwoord('n', 123, 9))


class Patient(object):
    def __init__(self, mail = '', naam = '', nummer = 0, wachtwoord = ''):
        self.mail = mail
        self.naam = naam
        self.nummer = nummer
        self.wachtwoord = wachtwoord

    @staticmethod
    def load(nummer, wachtwoord):
        for patient in Data.patienten:
            if patient.nummer == nummer and patient.wachtwoord == wachtwoord:
                return patient
            elif patient.nummer == nummer:
                print('Verkeerde wachtwoord')

    @staticmethod
    def add(mail, naam, nummer, wachtwoord):
        Data.patienten.append(Patient(mail, naam, int(nummer), wachtwoord))
        return Patient(mail, naam, nummer, wachtwoord)

    @staticmethod
    def exists(nummer):
        for patient in Data.patienten:
            if patient.nummer == nummer:
                return True

    @staticmethod
    def login():
        user = False
        while not user:
            input_nr = int(input('Patientnummer: '))
            input_ww = input('Wachtwoord: ')
            user = Patient.load(input_nr, input_ww)
            if not Patient.exists(input_nr):
                if input('Nieuwe patient %s aanmaken met wachtwoord: %s [j/n]?' %(input_nr, input_ww)).lower()[0:1] == 'j':
                    user = Patient.add(input('E-mail:'), input('Naam patient:'), input_nr, input_ww)
        print('U bent aangemeld als: %s' %user.naam)
        return user


class Meettraject(object):
    def __init__(self, patientnummer = 0, Meettrajectnummer = 0, vragenlijstnummer = 0):
        self.patientnummer = patientnummer
        self.Meettrajectnummer = Meettrajectnummer
        self.vragenlijstnummer = vragenlijstnummer

    @staticmethod
    def add(patientnummer, Meettrajectnummer, vragenlijstnummer):
        Data.meettrajecten.append(Meettraject(int(patientnummer), int(Meettrajectnummer), int(vragenlijstnummer)))
        return Meettraject(patientnummer, Meettrajectnummer, vragenlijstnummer)

    @staticmethod
    def exists(patientnummer, Meettrajectnummer):
        for Meettraject in Data.meettrajecten:
            if Meettraject.patientnummer == patientnummer and Meettraject.Meettrajectnummer == Meettrajectnummer:
                return True

    @staticmethod
    def select(patientnummer, Meettrajectnummer):
        if not Meettraject.exists(patientnummer, Meettrajectnummer):
            Meettraject.add(patientnummer, Meettrajectnummer, 1)
            return Meettraject(patientnummer, Meettrajectnummer, 1)
        else:
            for Meettraject in Data.meettrajecten:
                if Meettraject.patientnummer == patientnummer and Meettraject.Meettrajectnummer == Meettrajectnummer:
                    Data.meettrajecten.remove(Meettraject)
                    Meettraject.vragenlijstnummer +=  1
                    Meettraject.add(patientnummer, Meettrajectnummer, Meettraject.vragenlijstnummer)
                    return Meettraject

class Vraag(object):
    def __init__(self, invoertype = '', Meettrajectnummer = 0, volgnummer = 0, vraag = '', vraagid = 0, vragenlijstnummer = 0):
        self.invoertype = invoertype
        self.Meettrajectnummer = Meettrajectnummer
        self.volgnummer = volgnummer
        self.vraag = vraag
        self.vraagid = vraagid
        self.vragenlijstnummer = vragenlijstnummer

    @staticmethod
    def add(invoertype, Meettrajectnummer, volgnummer, vraag, vraagid, vragenlijstnummer):
        Data.vragen.append(Vraag(invoertype, int(Meettrajectnummer), int(volgnummer), vraag, int(vraagid), int(vragenlijstnummer)))
        return Vraag(invoertype, Meettrajectnummer, volgnummer, vraag, vraagid, vragenlijstnummer)

    @staticmethod
    def exists(Meettrajectnummer, vragenlijstnummer):
        for vraag in Data.vragen:
            if vraag.Meettrajectnummer == Meettrajectnummer and vraag.vragenlijstnummer == vragenlijstnummer:
                return True

class Antwoord(object):
    def __init__(self, antwoord = '', patientnummer = 0, vraagid = 0):
        self.antwoord = antwoord
        self.patientnummer = patientnummer
        self.vraagid = vraagid

    @staticmethod
    def remove(patientnummer, vraagid):
        for antwoord in Data.antwoorden:
            if antwoord.patientnummer == patientnummer and antwoord.vraagid == vraagid:
                Data.antwoorden.remove(antwoord)

    @staticmethod
    def add(antwoord, patientnummer, vraagid):
        Antwoord.remove(patientnummer, vraagid)
        Data.antwoorden.append(Antwoord(antwoord, int(patientnummer), int(vraagid)))
        return Antwoord(antwoord, patientnummer, vraagid)

    @staticmethod
    def input(patientnummer, invoertype, vraag, vraagid):
        validated  = False
        while not validated:
            antwoord = input(vraag)
            if invoertype == 'c' and antwoord.isdigit() and 1 <= int(antwoord) <= 10:
                validated = True
            elif invoertype == 'j' and antwoord.lower()[:1] in ('j', 'n'):
                antwoord = antwoord.lower()[:1]
                validated = True
            elif invoertype not in('c', 'j'):
                validated = True
            else:
                print('Ongeldige invoer, voer een %s in' % Data.invoertypes[invoertype])
        Antwoord.add(antwoord, patientnummer, vraagid)
        return Antwoord(antwoord, patientnummer, vraagid)

if __name__ == '__main__':

    #Data.patienten = pickle.load(open('enquete.pickle', 'rb'))

    Data.reset()
    another = True

    patient = Patient.login()
    while another:
        Meettraject = Meettraject()
        while Meettraject.Meettrajectnummer not in (1, 2, 3):
            Meettraject = Meettraject.select(patient.nummer, int(input('ZorgMeettraject? [1 = Bewegen, 2 = Zintuigen, 3 =  Huid] ')))
        if not Vraag.exists(Meettraject.Meettrajectnummer, Meettraject.vragenlijstnummer):
            print('U heeft alle vragenlijsten voor dit Meettraject al voltooid.')
        else:
            for vraag in Data.vragen:
                if vraag.Meettrajectnummer == Meettraject.Meettrajectnummer and vraag.vragenlijstnummer == Meettraject.vragenlijstnummer:
                    Antwoord.input(Meettraject.patientnummer, vraag.invoertype, vraag.vraag, vraag.vraagid)
        another = input('Nog een vragenlijst invullen? [j/n]? ').lower()[0:1] == 'j'
        Meettraject.Meettrajectnummer = 0

   # pickle.dump(Data.patienten, open('enquete.pickle', 'wb'))


