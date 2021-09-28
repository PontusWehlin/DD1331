#Laboration 4 Pontus Wehlin
class Befolkning:
    def __init__(self, fil): #Input: fil. Läser nästa rad i filen och delar upp landets namn, yta och befolkning
        rad = fil.readline().rstrip('\n')
        rad_delar = rad.split(',')
        self.land = rad_delar[0]
        self.yta = float(rad_delar[1].lstrip('	'))
        self.befolkning = float(rad_delar[2].lstrip('	'))
        self.inv_per_km2 = float()

    def __str__(self):
        return(self.land + '    ' + "{:.2e}".format(self.befolkning) + '    '
               + "{:.2e}".format(self.yta) + '     ' + "{:.2e}".format(self.inv_per_km2))

    def befolkningstäthet(self):
        self.inv_per_km2 = self.befolkning/self.yta


def radräknare(filnamn): #Laddar in en fil och räknar raderna i filen. Input: str Output: int
    radantal = 0
    fil = open(filnamn, 'r', encoding='UTF-8')
    for rad in fil:
        if rad != '\n':
            radantal += 1
    fil.close()
    return radantal


def main():
    länder = list() #Skapar en lista för att senare kunna addera länderna i
    filnamn = 'europa.txt' #Har hårdkodas men kan lätt göras om till att användaren anger en fil
    radantal = radräknare(filnamn)

    fil = open(filnamn, 'r', encoding='UTF-8')
    for i in range(radantal):
        länder.append(Befolkning(fil))
    fil.close()

    for land in länder:
        land.befolkningstäthet()

    länder.sort(key=lambda x: x.inv_per_km2, reverse=True)  #Detta stycke sorterar först upp länderna i storleksordning
    for i in range(len(länder)):                            #m.a.p. befolkningstätheten och sedan
        if länder[i].land == 'Total':                       #flyttar totalen till toppen
            index = i
    länder.insert(0, länder.pop(index))
    länder.pop(index)

    print('---------------------------------')
    print('Land     Invånare  Yta(km^2)   Befolkningstäthet')
    for land in länder:
        print(land)


main()
