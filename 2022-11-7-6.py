j = []
with open("leghosszab.txt","r") as f:
    for sor in f:
        sor = sor.strip().split()
        if len(sor) != 0:
            j.append(sor)

lg = 0
lgs = ""

for i in j:
    for k in i:
        if len(k) > lg:
            lg = len(k)
            lgs = k

print(lgs)