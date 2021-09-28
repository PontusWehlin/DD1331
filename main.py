#Laboration 5 Pontus Wehlin
class Aminosyra: #input: rad med info. raden ska ha uppbyggnaden: kod namn grupp vikt
    def __init__(self, rad):
        rad_delar = rad.split()
        self.kod = rad_delar[0]
        self.namn = rad_delar[1].lstrip('   ')
        self.grupp = rad_delar[2].lstrip('   ')
        self.vikt = float(rad_delar[3])

    def __str__(self):
        return(self.kod + ' ' + '{0:<14s}'.format(self.namn) + '{0:<9s}'.format(self.grupp) +' '+ str(self.vikt))

def filinläsning(filnamn, filtyp='UTF-8'): #Filinläsning, input: filnamn(str), ev filtyp. output: list
    fil = open(filnamn, 'r', encoding=filtyp)
    radlista = []
    rad = fil.readline()
    while rad != '':
        radlista.append(rad)
        rad = fil.readline().rstrip('\n')
    return radlista

def sortering(aminosyror): #tar in en lista med objekt och sorterar enligt användare
    print('Vill du ha aminosyrorna sorterade efter: ')
    print('1 - kod')
    print('2 - namn')
    print('3 - grupp')
    print('4 - molekylvikt')
    val = int(input('Ditt val: '))

    korrektaval = [1, 2, 3, 4]
    while val not in korrektaval:
        val = int(input(str(val) + ' är inte ett möjligt val, testa igen: '))

    if val == 1:
        aminosyror.sort(key=lambda x: x.kod)
    elif val == 2:
        aminosyror.sort(key=lambda x: x.namn)
    elif val == 3:
        aminosyror.sort(key = lambda x: x.grupp)
    else:
        aminosyror.sort(key = lambda x: x.vikt )

    return aminosyror


def main():
    aminosyror = []
    filnamn = 'aminosyror.txt'
    filrader = filinläsning(filnamn)

    for rad in filrader:
       aminosyror.append(Aminosyra(rad))

    aminosyror = sortering(aminosyror)

    for i in aminosyror:
        print(i)

main()