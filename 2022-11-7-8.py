def main():
    sen = ""
    with open("gyakorisag.txt","r",encoding="utf-8") as f:
        for sor in f:
            sor = sor.strip()
            sen += sor
    letS = set()
    letL = []
    revd = ""
    nums = dict()
    n = 0
    splitsen = sen.split()
    for s in splitsen:
        letS.add(s)
        letL.append(s)
    for l in splitsen:
        for i in letL:
            if l == i:
                n += 1
        nums[l] = n
        n = 0

    v = list(nums.values())
    k = list(nums.keys())
    m = k[v.index(max(v))]

    print(f"Leggyakoribb szó {m}")

if __name__ == "__main__":
    main()
