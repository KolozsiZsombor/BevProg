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
