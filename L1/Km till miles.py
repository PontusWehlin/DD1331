# Kilometer konverterare

def km_to_miles(km):
    return km*0.6214


kilometer = float(input('Ange antal kilometer: '))

print('Det blir ' + str(round(km_to_miles(kilometer),5)) + ' i miles.')

#Behövde använda round för annars blev 10 km 6.2139999999999995
#miles men det borde bli 6.214
