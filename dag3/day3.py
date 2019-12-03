from shapely.geometry import LineString

def OpenBestand():
    with open('input.txt', 'r') as file:
        for line in file:
            directions1 = [x.strip() for x in line.split(',')]
            directions2 = [x.strip() for x in line.split(',')]
    return directions1, directions2

def splitDirections(directions):
    letters = []
    cijfers = []

    for str in directions:
        letters.append(str[:1])
        cijfers.append(str[1:])
    return letters, cijfers

def gaOmhoog(cijfers, startpositie):
    puntlist = [startpositie[0], startpositie[1]]
    puntlist[1] += int(cijfers)
    punt = [(puntlist[0], puntlist[1])]
    positie = (startpositie[0], puntlist[1])
    return punt, positie

def gaOmlaag(cijfers, startpositie):
    puntlist = [startpositie[0], startpositie[1]]
    puntlist[1] -= int(cijfers)
    punt = [(puntlist[0], puntlist[1])]
    positie = (startpositie[0], puntlist[1])
    return punt, positie

def gaLinks(cijfers, startpositie):
    puntlist = [startpositie[0], startpositie[1]]
    puntlist[0] -= int(cijfers)
    punt = [(puntlist[0], puntlist[1])]
    positie = (puntlist[0], startpositie[1])
    return punt, positie

def gaRechts(cijfers, startpositie):
    puntlist = [startpositie[0], startpositie[1]]
    puntlist[0] += int(cijfers)
    punt = [(puntlist[0], puntlist[1])]
    positie = (puntlist[0], startpositie[1])
    return punt, positie

def berekenPunten(letter, cijfers, startpositie):
    opties = {
        'U': gaOmhoog,
        'D': gaOmlaag,
        'L': gaLinks,
        'R': gaRechts,
    }
    functie=opties.get(str(letter), lambda : 'Rip, er is iets mis pik')
    punt, positie = functie(cijfers, startpositie)
    return punt, positie

def bepaalSnijPunt(puntenLijn1, puntenLijn2):
    line1 = LineString(puntenLijn1)
    line2 = LineString(puntenLijn2)

    snijpunt = line1.intersection(line2)
    return snijpunt

def main():
    directions1, directions2 = OpenBestand()
    puntenLijn1 = []
    puntenLijn2 = []
    lettersLijn1, cijfersLijn1 = splitDirections(directions1)
    lettersLijn2, cijfersLijn2 = splitDirections(directions2)

    hoogsteGetal = 0
    if max(cijfersLijn1) > max(cijfersLijn2):
        hoogsteGetal = max(cijfersLijn1)
    else:
        hoogsteGetal = max(cijfersLijn2)
    positie = (1, int(hoogsteGetal) - 1)

    for x in range(len(lettersLijn1)):
        punt, positie = berekenPunten(lettersLijn1[x], cijfersLijn1[x], positie)
        puntenLijn1.extend(punt)
    for x in range(len(lettersLijn2)):
        punt, positie = (berekenPunten(lettersLijn2[x], cijfersLijn2[x], startpositie))
        puntenLijn2.extend(punt)

    print(bepaalSnijPunt(puntenLijn1, puntenLijn2))

if __name__ == "__main__":
    main()
