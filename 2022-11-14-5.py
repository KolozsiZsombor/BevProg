bejarhato = ["alma","körte","meggy",1,2,3,"alma","alma",-10]

darabok = {}

for elem in bejarhato:
    if type(elem) == int:
        darabok["egesz_szamok"] = darabok.get("egesz_szamok",0) + 1
    else:
        darabok[elem] = darabok.get(elem,0) + 1

print(darabok)