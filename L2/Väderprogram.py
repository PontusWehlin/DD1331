#Väderprogram av Pontus Wehlin
import time

def inmatning():
    Max = 0                 #Sätter initialvärden för nederbörden
    Min = 99999
    Tot = 0
    månader = ['Januari', 'Februari', 'Mars', 'April', 'Maj', 'Juni', 'Juli',
               'Augusti', 'September', 'Oktober', 'November', 'December']   #Lista med alla månader
    for i in range(len(månader)):   #Stegar igenom alla månader och jämför med max och min
        månad = float(input('Ange nederbörden för ' + månader[i] + ':'))
        
        if månad < Min:
            Min = månad
        elif månad > Max:
            Max = månad

        Tot+=månad #Summerar ihop totala nederbörden för hela året

    Medel = Tot/12
    return Max, Min, Medel

def statistik(Max, Min, Medel): #Anger de sparade värdena för nederbörden
    print('Största nederbörden under en månad var: ', Max)
    print('Minsta nederbörden under en månad var: ', Min)
    print('Medel nederbörden under hela året var: ', Medel)

if __name__ == "__main__":
    Max = None      #Sätter dessa värden för att det ska printa None om alt 2 väljs först
    Min = None
    Medel = None
    val = 1
    while val != 3:     #Huvudprogrammet
        print('1 - Mata in nederbörd månadsvis under ett år')
        print('2 - Se statistik för detta år')
        print('3 - Avsluta programmet')
        val = int(input('Ditt val: '))
        if val == 1:
          Max, Min, Medel = inmatning()
        elif val == 2:
            statistik(Max, Min, Medel)
        elif val == 3: 
            pass    #Programmet avslutas i while loopen
        else:       #Kontrollerar så att ett det inte valts ett felaktigt val
            print('Fel val')
        time.sleep(1)   #Pausar programmet i 2 sek för ökad läslighet
                

