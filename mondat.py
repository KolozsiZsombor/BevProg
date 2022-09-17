<<<<<<< HEAD
def main():
    letS = set()
    letL = []
    revd = ""
    nums = dict()
    n = 0
    sen = input("Adjon meg egy mondatot: ")
    for s in sen:
        letS.add(s)
        letL.append(s)
    splitsen = sen.split()
    print(f"Listába rendezve szavanként: {splitsen}")
    for r in reversed(sen):
        revd += r
    print(f"Fordítva: {revd}")
    for l in letS:
        for i in letL:
            if l == i:
                n += 1
        nums[l] = n
        n = 0
    print(f"Betűk gyakorisága: {nums}")

if __name__ == "__main__":
    main()
=======
def main():
    letS = set()
    letL = []
    revd = ""
    nums = dict()
    wrds = ""
    wrdt = []
    n = 0
    sen = input("Adjon meg egy mondatot: ")
    for s in sen:
        letS.add(s)
        letL.append(s)
        wrds += s
        if s == " ":
            wrdt.append(wrds)
            wrds = ""
    for r in reversed(sen):
        revd += r
    for l in letS:
        if letL == letS:
            n += 1
        nums[l] = n
        n = 0
    
    
    return revd, nums, wrdt
    



if __name__ == "__main__":
    print(main())
>>>>>>> ace4562bc3311e7552b10854d56de5dfea327fc9
