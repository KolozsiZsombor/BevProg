def main():
    open("kihazi.txt","w")
    open("kihazifinal.txt","w")
    line = ""
    n = 1
    import string; special = string.punctuation
    file = open("hazi.txt","r",encoding="utf-8")
    l = file.readlines()
    for i in l:
        i = i.strip()
        if len(i) != 0:
            for c in i:
                if c not in special:
                    line += c
            out = open("kihazi.txt","a",encoding="utf-8") 
            out.write(line)
            out.write("\n")
            line = ""
    out.close()
    file = open("kihazi.txt","r",encoding="utf-8")
    l = file.readlines()
    for i in l:
        if n % 3 == 0:
            out = open("kihazifinal.txt","a",encoding="utf-8")
            out.write(i)
        n += 1
    out.close()
    import os;os.remove("kihazi.txt")




if __name__ == "__main__":
    main()