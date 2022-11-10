n = int(input("Az első hány sort olvassuk be??? "))
j = 0
with open("be.txt","r",encoding="utf-8") as f:
    for sor in f:
        while j < n:
            sor = sor.strip()
            print(sor)
            j += 1