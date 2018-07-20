f = open('crime_rates.csv', 'r')
bestand= f.read()
crime_rates = bestand.split('\n')
print(crime_rates)