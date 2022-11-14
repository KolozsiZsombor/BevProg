bejarhato = [10,1,5,10,2,3]
print(min(bejarhato))

#.....................................
diakok=[("János",17,4.9),("Etel",18,4.2),("Viola",19,4.1)]

def hasonlitando(elem):
    nev,kor,atlag = elem; return atlag
    #return elem[2]
    #return nev

# print(min(diakok,key=hasonlitando))
ldiak = list(diakok)
ldiak.sort(key=hasonlitando) # ldiak.sort(key=hasonlitando, reverse=True)
print(ldiak)
ldiak2 = sorted(diakok, key=hasonlitando, reverse = True)
print(ldiak2)