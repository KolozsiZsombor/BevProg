A=[6262,4426,3758,5902,3273,5891,6237,1610,1452,4581,2198,3798,1922,4914,5060,2265,1514,2708,2974,913,3227,1371,5916,6498,4095,2676,5069,1125,2490,631]

N = len(A)

for k in range(1,N):

    T = A[k]
    i=k-1
    while i >= 0 and T<A[i]:
        A[i+1] = A[i]
        i=i-1
    
    A[i+1]=T

print(A)