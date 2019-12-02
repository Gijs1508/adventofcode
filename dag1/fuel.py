import math

def functie():
    eindgetal = 0
    for x in range(len(getallen)):
        temporarymass = int(getallen[x])
        mass = 0
        while True:
            print(temporarymass)
            if (math.floor(int(getallen[x]) / 3) - 2) >= 0:
                temporarymass = math.floor(int(getallen[x]) / 3) - 2
                print(temporarymass)
                mass += temporarymass
                print(mass)
            else:
                break
        eindgetal += mass
    return eindgetal

def testfunctie(getallen):
    mass = 0
    for x in range(len(getallen)):
        print(getallen[x])
        tempmass = math.floor(int(getallen[x]) / 3) - 2
        print(tempmass)
        mass += tempmass
        print(mass)
        if tempmass >= 0:
            tempmass = math.floor(int(getallen[x]) / 3) - 2
            print(tempmass)
            mass += tempmass
            print(mass)
        else:
            break
    return mass

def functie3(getallen):
    #pak alle getallen met n loop
    #voer voor elk getal de functie uit tot het niet meer kan
    #voeg al die getallen toe aan het eindgetal
    mass = 0
    tempmass = 0
    for x in range(len(getallen)):
        listmass = []
        listmass.append(getallen[x])
        tempgetal = math.floor(int(getallen[x]) / 3) - 2
        listmass.append(tempgetal)
        finallist = []
        while True:
            if tempgetal >= 0:
                tempgetal = math.floor(tempgetal) / 3 - 2
                if tempgetal >= 0:
                    listmass.append(str(int(tempgetal)).replace("\n", ""))
                else:
                    finallist = listmass
                print(listmass)
            else:
                finallist = listmass
                for z in range(len(finallist)):
                    mass += int(finallist[z])
                break
    return mass



def main():
    getallen = []
    with open('input.txt', 'r') as file:
        for line in file:
            getallen.append(line)
    print(functie3(getallen))

if __name__ == "__main__":
    main()
