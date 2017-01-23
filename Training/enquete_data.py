import csv

class Data:
    trajectnamen = {1: 'Bewegen', 2: 'Zintuigen', 3: 'Huid'}
    invoertypes = {'c': 'cijfer', 'j': 'ja of nee', 'o': 'opmerking'}

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
            columns += 'row[%s],' % str(countcolumn)
        code = 'for row in workfile: %s.add(%s)' % (datatype.__class__.__name__, columns[:-1])
        exec(code)


    @staticmethod
    def save(bestand, datatype):
        bestand = bestand.lower()
        workfile = csv.writer(open('enquete_data_' + bestand + '.csv', 'w', newline=''))
        columns = ''
        for column in sorted(vars(datatype)):
            columns += 'item.' + column + ','
        code = 'for item in Data.%s: workfile.writerow([%s])' % (bestand, columns[:-1])
        exec(code)

