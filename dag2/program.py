def OpenBestand():
    with open('input.txt', 'r') as file:
        for line in file:
            getallen = [int(x.strip()) for x in line.split(',')]
    return getallen

def OpCode1(getallen, index, getal1, getal2):
    getallen[getallen[index + 3]] = getallen[getal1] + getallen[getal2]
    index += 4
    return getallen, index

def OpCode2(getallen, index, getal1, getal2):
    getallen[getallen[index + 3]] = getallen[getal1] * getallen[getal2]
    index += 4
    return getallen, index

def machine(getallen, indexGetal1, indexGetal2):
    index = 0
    result = getallen[0]
    while True:
        getallen[1] = indexGetal1
        getallen[2] = indexGetal2
        getal1 = getallen[index + 1]
        getal2 = getallen[index + 2]
        if(getallen[index] == 1):
            getallen, index = OpCode1(getallen, index, getal1, getal2)
        elif(getallen[index] == 2):
            getallen, index = OpCode2(getallen, index, getal1, getal2)
        elif(getallen[index] == 99):
            result = getallen[0]
            break
    return result

def main():
    getallen = OpenBestand()
    for x in range(99*99):
        y = x//99
        z = x%100
        result = machine(getallen, y, z, restart)
        if result == 19690720:
            print(f"output: {result}")
            break
        else:
            print('nog niet t goede antwoord')
            break
        # print(f"getal1: {y}")
        # print(f"getal2: {z}")
        # print(f"uitkomst is: {100*y + z}")

if __name__ == "__main__":
    main()
