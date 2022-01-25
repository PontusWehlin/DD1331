# Stadium Seating

def intäkter(bill):
    priser = [290, 220, 140]
    return bill[0]*priser[0]+bill[1]*priser[1]+bill[2]*priser[2]

def antal(bill):
    return sum(bill)


print('Hur många biljetter har sålts? ')
biljetter = [int(input('A: ')), int(input('B: ')), int(input('C: '))]

print('Totalt har ', antal(biljetter), ' sålts och intäkterna blev ', intäkter(biljetter), ' kr.')
