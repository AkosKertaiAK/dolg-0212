fajl = open("lotto.txt","r")

tartalom = fajl.read()

print("Hetek száma: ",tartalom.count("\n") + 1)

print(tartalom)

szamok = tartalom.split()

leggyakoribb = max(szamok, key=szamok.count)

print("A leggyakoribb szám:", leggyakoribb)
print("Ennyiszer húzták ki:", szamok.count(leggyakoribb))

szam1 = input("Add meg az első számot: ")
szam2 = input("Add meg az második számot: ")
szam3 = input("Add meg az harmadik számot: ")
szam4 = input("Add meg az negyedik számot: ")
szam5 = input("Add meg az ötödik számot: ")

huzasok = tartalom.splitlines()

max_talalat = 0

for huzas in huzasok:
    huzott = huzas.split()
    talalat = 0

    if szam1 in huzott:
        talalat += 1
    if szam2 in huzott:
        talalat += 1
    if szam3 in huzott:
        talalat += 1
    if szam4 in huzott:
        talalat += 1
    if szam5 in huzott:
        talalat += 1

    if talalat > max_talalat:
        max_talalat = talalat

print("Ennyi találatod lett volna:", max_talalat)



szamok = tartalom.split()

tuti = []

for i in range(5):
    leggyakoribb = max(szamok, key=szamok.count)
    tuti.append(leggyakoribb)

    while leggyakoribb in szamok:
        szamok.remove(leggyakoribb)

fajl = open("tipp.txt", "w")
fajl.write(" ".join(tuti))

fajl.close()