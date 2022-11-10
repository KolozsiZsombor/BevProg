def main():
    line = ""
    everything = []
    final = []
    import string
    special = string.punctuation
    with open("hazi.txt","r",encoding="utf-8") as f:
        l = f.readline()
        while l:
            if len(l) != 0:
                for c in l:
                    if c not in special:
                        line += c
                everything.append(line)
                line = ""
            l = f.readline()
    for i in everything:
        if i != "\n":
            final.append(i)


    
    return final



if __name__ == "__main__":
    print(main())