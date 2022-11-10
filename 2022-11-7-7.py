n = 0
l = []

with open("be.txt","r") as f:
    for sor in f:
        sor=sor.strip()
        l.append(sor)
        
with open("ki.txt","w") as fki:
    for i in l:
        n += 1
        if n == 4 or n == 6:
                l.pop(n)
        print(i,file=fki)