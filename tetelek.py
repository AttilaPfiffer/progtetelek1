import math

def elso_feladat(szam: float):
    i: int = 2
    osztok = []
    for i in range(2, round(math.sqrt(szam + 1))):
        if szam % i == 0:
            osztok.append(i)
    return osztok

print(elso_feladat(10004))

def masodik_feladat():
    also: int = 42
    felso: int = 67
    i = also
    while (i <= felso and not(i % 10== 0)):
        i += 1
    van: bool = i <= felso
    if (van):
        print("van 0-ra végződő szám: " + i)
    else: 
        print("nincs 0-ra végződő")
