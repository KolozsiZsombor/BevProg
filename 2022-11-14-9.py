# Bináris kersés
A=[631, 913, 1125, 1371, 1452, 1514, 1610, 1922, 2198, 2265, 2490, 2676, 2708, 2974, 3227, 3273, 3758, 3798, 4095, 4426, 4581, 4914, 5060, 5069, 5891, 5902, 5916, 6237, 6262, 6498]
N = len(A)
also, felso = 0, N-1
keresett = 3758
while also <=felso:
    k = (felso+also)//2
    if keresett < A[k]:
        felso = k-1
    elif keresett > A[k]:
        also = k+1
    else:
        kimenet = True,k
        break
else:
    kimenet = False

print(kimenet)