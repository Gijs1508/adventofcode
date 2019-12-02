def OpenBestand():
    with open('input.txt', 'r') as file:
        for line in file:
            getallen = [int(x.strip()) for x in line.split(',')]
    return getallen

def GetalIsEen1(getallen, index, getal1, getal2):
    getallen[getallen[index + 3]] = getallen[getal1] + getallen[getal2]
    index += 4
    return getallen, index

def GetalIsEen2(getallen, index, getal1, getal2):
    getallen[getallen[index + 3]] = getallen[getal1] * getallen[getal2]
    index += 4
    return getallen, index

def main():
    getallen = OpenBestand()
    index = 0
    getallen[1] = 12
    getallen[2] = 2

    while True:
        getal1 = getallen[index + 1]
        getal2 = getallen[index + 2]
        if(getallen[index] == 1):
            getallen, index = GetalIsEen1(getallen, index, getal1, getal2)
        elif(getallen[index] == 2):
            getallen, index = GetalIsEen2(getallen, index, getal1, getal2)
        elif(getallen[index] == 99):
            break
    print(getallen)

if __name__ == "__main__":
    main()
