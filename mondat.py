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
