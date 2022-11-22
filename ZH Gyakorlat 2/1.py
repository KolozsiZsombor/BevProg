def beolvasas():
    playlist = []
    pl = []
    with open("playlist.csv","r",encoding="utf-8") as f:
        for line in f:
            pl.append(line.strip().split(";"))
    for i in pl:
        playlist.append({"eloado":str(i[0]),"cim":str(i[1]),"mufaj":str(i[2]),"hossz":i[3]})
    return(playlist)

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
    out.write(f"{str(mins)} {str(secs)}")
    
def leghosszab_rockzene(lejatszasiLista):
    stuff = []
    open("03_leghosszab_rock.txt", "w", encoding="utf-8")
    for sub in lejatszasiLista:
        if sub["mufaj"] == "rock":
            stuff.append([sub["hossz"],sub["cim"]])

    big = 0
    # for i in stuff:
    #     for k in i:
    #         if int(k[0]) > big:
    #             big = k[0]
    #             nev = k[1]

    # print(big,nev)
        # out = open("03_leghosszab_rock.txt","a",encoding="utf-8")
        # out.write()
        
def leggyakoribb_mufaj(lejatszasiLista):
    nums = {}
    mufajL = []
    mufajH = set()
    
    for i in lejatszasiLista:
        for k in i:
            mufajL.append(k["mufaj"])
            mufajH.add(k["mufaj"])

    for l in mufajH:
        for i in mufajL:
            if l == i:
                n += 1
        nums[l] = n
        n = 0
        
    print(nums)

if __name__ == "__main__":
    beolvasas()
    teljes_hossz(beolvasas())
    leghosszab_rockzene(beolvasas())
    leggyakoribb_mufaj(beolvasas())