alap = 0

with open("be2.txt","r") as f:
    osszeg = 0
    darab = 0

    sor = f.readline()

    while sor:
        osszeg += int(sor)
        darab += 1
        sor = f.readline()

atag = osszeg/darab

with open("ki.txt","w") as f:
    f.write(f"Az átlag {str(atag)}\n")