#P-uppgift Kösimulering
#Pontus Wehlin
import random
class Kund:
    def __init__(self, kundnummer, ankomsttid, ärenden):
        self.kundnummer = kundnummer
        self.ankomst = ankomsttid
        self.ärenden = ärenden
    def __str__(self):
        pass
    def utträdestid(self, betjäningstid, betjänas):
        self.klar = betjänas + betjäningstid * self.ärenden

def filinmatning(filnamn):
    parametrar = []
    fil = open(filnamn, 'r', encoding='UTF')
    for i in range(4):
        rad = fil.readline().rstrip('/n')
        orden = rad.split()
        parametrar.append(int(orden[-1]))
    fil.close()
    return parametrar



def antal_ärenden():
    while True:
        ärenden = 1
        if random.randint(1,2) == 2:
            break
    return ärenden

def main():
    antal_kunder = 0
    parametrar = filinmatning('kösim.txt')
    print(parametrar)
    öppningstid = parametrar[1]
    stängningstid = parametrar[2]


main()
