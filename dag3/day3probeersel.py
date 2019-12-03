def OpenBestand():
    with open('input.txt', 'r') as file:
        for line in file:
            directions = [x.strip() for x in line.split(',')]
    return directions

def splitDirections(directions):
    letters = []
    nummers = []

    for str in directions:
        letters.append(str[:1])
        nummers.append(str[1:])
    return letters, nummers

def printBoard(bord):
    lenBord = len(bord)
    # beetje verwarrend, x = verticaal; y = horizontaal
    for x in range(len(bord)) :
        for y in range(len(bord[x])) :
            if(x == lenBord - 2 and y == 1):
                bord[x][y] = 'o'
                startpositie = bord[x][y]
    return bord, startpositie

def gaOmhoog(bord, nummer, positie):
    xStartPos = positie[0]
    yStartPos = positie[1]
    # ff de range fixen
    for x in range(len(nummer)):
        bord[xStartPos - x][yStartPos] = "|"
        if nummer[x] == (max(nummer)):
            positie = (int(nummer[x]), yStartPos)
    return bord, positie

def gaOmlaag(bord, nummer, positie):
    xStartPos = positie[0]
    yStartPos = positie[1]
    # ff de range fixen
    for x in range(len(nummer)):
        bord[xStartPos - x][yStartPos] = '|'
        if nummer[x] == (max(nummer)):
            positie = (int(nummer[x]), yStartPos)
    return bord, positie

def gaLinks(bord, nummer, positie):
    xStartPos = positie[0]
    yStartPos = positie[1]
    # ff de range fixen
    for x in range(len(nummer)):
        bord[xStartPos][yStartPos - x] = '-'
        if nummer[x] == (max(nummer)):
            positie = (xStartPos, int(nummer[x]))
    return bord, positie

def gaRechts(bord, nummer, positie):
    xStartPos = positie[0]
    yStartPos = positie[1]
    # ff de range fixen
    for x in range(len(nummer)):
        bord[xStartPos][yStartPos + x] = '-'
        if nummer[x] == (max(nummer)):
            positie = (xStartPos, int(nummer[x]))
    return bord, positie

def doeBeweegLogica(letter, nummer, bord, startpositie):
    opties = {
        'U': gaOmhoog,
        'D': gaOmlaag,
        'L': gaLinks,
        'R': gaRechts,
    }
    functie=opties.get(str(letter), lambda : 'Rip, er is iets mis pik')
    bord, positie = functie(bord, nummer, startpositie)
    return bord, positie

def main():
    directions = OpenBestand()
    letters, nummers = splitDirections(directions)
    maxNummer = int(max(nummers))
    bord = [['.' for i in range(maxNummer + 3)] for i in range(maxNummer + 3)]
    bord, startpositie = printBoard(bord)
    for x in range(len(letters)):
            print(letters[x])
            bord,positie = doeBeweegLogica(letters[x], nummers[int(x)], bord, startpositie)
            print(positie)
    printBoard(bord)

if __name__ == "__main__":
    main()
