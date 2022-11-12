def main():
    open("kihazifinal.txt","w")
    line = ""
    roz = []
    n = 1
    import string; special = string.punctuation
    mgh = ["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű","y"]
    file = open("hazi.txt","r",encoding="utf-8")
    l = file.readlines()
    for i in l:
        i = i.strip()
        if len(i) != 0:
            for c in i:
                if c not in special and c not in mgh:
                    line += c
            roz.append(line)
            line = ""
    for i in roz:
        if n % 3 == 0:
            out = open("kihazifinal.txt","a",encoding="utf-8")
            out.write(i)
            out.write("\n")
        n += 1

if __name__ == "__main__":
    main()