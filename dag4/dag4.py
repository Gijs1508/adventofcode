import collections

def check(getal):
    zelfde_getallen = 0
    laatste_getal = 0
    zelfde_twee = 0
    for char in str(getal):
        if int(char) < laatste_getal:
            return False
        elif laatste_getal == int(char):
            zelfde_getallen += 1
        elif laatste_getal < int(char):
            if zelfde_getallen == 2:
                zelfde_twee += 1
            zelfde_getallen = 1
        laatste_getal = int(char)
    if zelfde_twee >= 1:
        return True

def check_twee(opties, top=2):
    common = collections.Counter(opties).most_common(top)
    return (i for i, _ in common)

lage_getal = 183564
hoge_getal = 657474
aantal_opties = 0
opties_list = []
for x in range(lage_getal, hoge_getal):
    if check(x):
        aantal_opties+=1
print(aantal_opties)

#print(check_twee(opties_list))
