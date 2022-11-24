# 1.feladat
def beolvasas():
    playlist = []
    pl = []
    with open("playlist.csv","r",encoding="utf-8") as f:
        for line in f:
            pl.append(line.strip().split(";"))
    for i in pl:
        playlist.append({"eloado":str(i[0]),"cim":str(i[1]),"mufaj":str(i[2]),"hossz":i[3]})
    return(playlist)

# 2.feladat
def teljes_hossz(lejatszasiLista):
    length = 0
    open("02_hossz.txt","w",encoding="utf-8")
    for i in lejatszasiLista:
        for key in i.keys():
            if key.find("hossz") > -1:
                length += int(i[key])
    mins = length // 60
    secs = length - (mins * 60)
    out = open("02_hossz.txt","a",encoding="utf-8")
    out.write(f"{str(mins)} perc {str(secs)} másodperc")
    
# 3.feladat
def leghosszab_rockzene(lejatszasiLista):
    stuff = []
    open("03_leghosszab_rock.txt", "w", encoding="utf-8")
    for i in lejatszasiLista:
        for key in i.keys():
            if key.find("rock"):
                stuff.append([int(i["hossz"]),i["cim"]])

    big = 0
    nev = None
    for i in stuff:
        if i[0] > big:
            big = i[0]
            nev = i[1]

    out = open("03_leghosszab_rock.txt","a",encoding="utf-8")
    out.write(str(big))
    out.write(" ")
    out.write(nev)

# 4.feladat
def leggyakoribb_mufaj(lejatszasiLista):
    nums = {}
    mufajL = []
    mufajH = set()
    n = 0
    out = open("4_kedvenc_mufaj.txt","w",encoding="utf-8")

    for i in lejatszasiLista:
        mufajH.add(i["mufaj"])
        mufajL.append(i["mufaj"])

    for l in mufajH:
        for i in mufajL:
            if l == i:
                n += 1
        nums[l] = n
        n = 0

    v = list(nums.values())
    k = list(nums.keys())
    m = k[v.index(max(v))]

    out.write(str((m)))

# 5.feladat
def zeneket_csoportosit(lejatszasiLista):
    nums = {}
    eloadoL = []
    eloadoH = set()
    eloadoNPHL = []
    n = 0

    for i in lejatszasiLista:
        eloadoH.add(i["eloado"])
        eloadoL.append(i["eloado"])
        eloadoNPHL.append([i["eloado"],int(i["hossz"])])

        for i in eloadoH:
            for l in eloadoNPHL:
                if i == l[0]:
                    n += l[1]
            nums[i] = n
            n = 0
    
    with open("5_osszegzes.txt","w",encoding="utf-8") as out:
        print(nums,file=out)



if __name__ == "__main__":
    beolvasas()
    teljes_hossz(beolvasas())
    leghosszab_rockzene(beolvasas())
    leggyakoribb_mufaj(beolvasas())
    zeneket_csoportosit(beolvasas())