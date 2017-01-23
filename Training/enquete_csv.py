import csv

class Data():
    patienten = []
    trajecten = []
    vragen = []
    antwoorden = []


    @staticmethod
    def load(bestand, datatype):
        bestand = bestand.lower()
        columns = ''
        workfile = csv.reader(open('enquete_data_' + bestand + '.csv', 'r'))
        for countcolumn in range(len(vars(datatype))):
            columns +=  'row[%s],' %str(countcolumn)
        code = 'for row in workfile: %s.add(%s)' %(datatype.__class__.__name__, columns[:-1])
        exec(code)

    @staticmethod
    def save(bestand, datatype):
        bestand = bestand.lower()
        workfile = csv.writer(open('enquete_data_' + bestand + '.csv', 'w', newline = ''))
        columns = ''
        for column in sorted(vars(datatype)):
            columns +=  'item.' + column + ','
        code = 'for item in Data.%s: workfile.writerow([%s])' %(bestand, columns[:-1])
        exec(code)


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


class Traject(object):
    def __init__(self, patientnummer = 0, trajectnummer = 0, vragenlijstnummer = 0):
        self.patientnummer = patientnummer
        self.trajectnummer = trajectnummer
        self.vragenlijstnummer = vragenlijstnummer

    @staticmethod
    def add(patientnummer, trajectnummer, vragenlijstnummer):
        Data.trajecten.append(Traject(int(patientnummer), int(trajectnummer), int(vragenlijstnummer)))
        return Traject(patientnummer, trajectnummer, vragenlijstnummer)

    @staticmethod
    def exists(patientnummer, trajectnummer):
        for traject in Data.trajecten:
            if traject.patientnummer == patientnummer and traject.trajectnummer == trajectnummer:
                return True

    @staticmethod
    def select(patientnummer, trajectnummer):
        if not Traject.exists(patientnummer, trajectnummer):
            Traject.add(patientnummer, trajectnummer, 1)
            return Traject(patientnummer, trajectnummer, 1)
        else:
            for traject in Data.trajecten:
                if traject.patientnummer == patientnummer and traject.trajectnummer == trajectnummer:
                    Data.trajecten.remove(traject)
                    traject.vragenlijstnummer +=  1
                    Traject.add(patientnummer, trajectnummer, traject.vragenlijstnummer)
                    return traject

class Vraag(object):
    def __init__(self, invoertype = '', trajectnummer = 0, volgnummer = 0, vraag = '', vraagid = 0, vragenlijstnummer = 0):
        self.invoertype = invoertype
        self.trajectnummer = trajectnummer
        self.volgnummer = volgnummer
        self.vraag = vraag
        self.vraagid = vraagid
        self.vragenlijstnummer = vragenlijstnummer

    @staticmethod
    def add(invoertype, trajectnummer, volgnummer, vraag, vraagid, vragenlijstnummer):
        Data.vragen.append(Vraag(invoertype, int(trajectnummer), int(volgnummer), vraag, int(vraagid), int(vragenlijstnummer)))
        return Vraag(invoertype, trajectnummer, volgnummer, vraag, vraagid, vragenlijstnummer)

    @staticmethod
    def exists(trajectnummer, vragenlijstnummer):
        for vraag in Data.vragen:
            if vraag.trajectnummer == trajectnummer and vraag.vragenlijstnummer == vragenlijstnummer:
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
                print('Ongeldige invoer, voer een %s in' % invoertypes[invoertype])
        Antwoord.add(antwoord, patientnummer, vraagid)
        return Antwoord(antwoord, patientnummer, vraagid)

if __name__ == '__main__':
    trajectnamen = {1: 'Bewegen', 2: 'Zintuigen', 3: 'Huid'}
    invoertypes = {'c': 'cijfer', 'j': 'ja of nee', 'o': 'opmerking'}
    Data.load('patienten', Patient())
    Data.load('trajecten', Traject())
    Data.load('vragen', Vraag())
    Data.load('antwoorden', Antwoord())
    another = True

    patient = Patient.login()
    while another:
        traject = Traject()
        while traject.trajectnummer not in (1, 2, 3):
            traject = Traject.select(patient.nummer, int(input('Zorgtraject? [1 = Bewegen, 2 = Zintuigen, 3 =  Huid] ')))
        if not Vraag.exists(traject.trajectnummer, traject.vragenlijstnummer):
            print('U heeft alle vragenlijsten voor dit traject al voltooid.')
        else:
            for vraag in Data.vragen:
                if vraag.trajectnummer == traject.trajectnummer and vraag.vragenlijstnummer == traject.vragenlijstnummer:
                    Antwoord.input(traject.patientnummer, vraag.invoertype, vraag.vraag, vraag.vraagid)
        another = input('Nog een vragenlijst invullen? [j/n]? ').lower()[0:1] == 'j'
        traject.trajectnummer = 0

    Data.save('patienten', Patient())
    Data.save('trajecten', Traject())
    Data.save('antwoorden', Antwoord())

