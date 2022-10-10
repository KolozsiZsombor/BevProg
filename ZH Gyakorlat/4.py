def main():
    chn = int(input("How many chickens are there?"))
    con = int(input("How many cows are there?"))
    pign = int(input("How many pigs are there?"))
    chl = 2
    col = 4
    pigl = 4
    chf = chl * chn
    cof = col * con
    pigf = pigl * pign
    return chf + cof + pigf


if __name__ == "__main__":
    print(main())
