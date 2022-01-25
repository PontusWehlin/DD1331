#Ovanliga ord sortering Pontus Wehlin
def sanering(Ord):  #'Sanerar' ord, tar bort tex . , ! " osv. Input:str Output:str
                    # Dock behålls '-' då dessa är nödvändiga för läsningen
    str1 = ''
    sanerat = [] #lista med bokstäverna i ett ord
    for i in range(len(Ord)): #Går igenom varje tecken i ordet
        if Ord[i].isalnum() or Ord[i] == '-' or Ord[i] == '–': #De 2 bindessträcken är tydligen olika
            sanerat.append(Ord[i])

    if not str1.join(sanerat).isalpha(): #rensar ut det som bara är siffror
        temp = sanerat
        sanerat = []
        for i in range(len(temp)):
            if str1.join(temp[i]).isalpha():
                sanerat = temp
        
    
    if len(sanerat)==1 and not sanerat[0].isalnum():    #Tar bort fallen där det endast är ett bindessträck kvar
        sanerat = []
    return str1.join(sanerat)

def filinmatning(filnamn, encoding = 'UTF-8'): #Laddar in en text och spottar ut en lista med alla ord. Output:list

    korrekt_inmatning = False
    
    while not korrekt_inmatning:
        korrekt_inmatning = True
        try:        #Hanterar felaktiga filnamn
            infil = open(filnamn,'r', encoding=encoding) 
        except:
            print('Filen hittades inte!')
            filnamn = input('Ange ett korrekt filnamn: ')
            korrekt_inmatning = False
            
    orden = []
    textrad = infil.readline().rstrip('\n')
    
    while textrad!='':  #Delar upp texten i ord
        tempord = textrad.split(' ')
        for i in range(len(tempord)):
            orden.append(tempord[i].lower())
        textrad = infil.readline().rstrip('\n')
        if textrad == '':
            textrad = infil.readline().rstrip('\n')
            
    infil.close()
    
    for i in range(len(orden)):
        if not orden[i].isalpha():
            orden[i] = sanering(orden[i]) #Skickar iväg vissa ord till saneringen
            
    return orden

def ordsortering(orden, vanligaorden):    #Sorterar ut de vanliga orden. Input:2st list Output:list

    for i in range(len(vanligaorden)):
        vanligaorden[i] = vanligaorden[i].rstrip('\n')
        
    ovanligaord = []
    for i in range(len(orden)):
        if orden[i] not in vanligaorden and orden[i] not in ovanligaord:
            ovanligaord.append(orden[i])
            
    ovanligaord.sort()
    return ovanligaord

def main():
    orden = filinmatning(input('Vilken fil vill du läsa in? '))
    vanligaorden = filinmatning('vanligaord.txt', encoding = 'latin-1')
    ovanligaord = ordsortering(orden, vanligaorden)
    print('Texten innehåller ' + str(len(orden)) + ' ord.')
    print('Varav ' + str(len(ovanligaord)) + ' st av dem anses vara ovanliga.')
    print('De ovanliga orden är:')
    print(*ovanligaord, sep = '\n')
    
if __name__ == '__main__':
    main()
