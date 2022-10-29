import string

sen = "Nos én sose csináltam mondta Alice"
szavak = sen.split()
print(szavak)

def irasjelEltavolito(szoveg):
    irasjelNelkul = ""
    for i in szoveg:
        if i not in string.punctuation:
            irasjelNelkul += i
    return irasjelNelkul

print(irasjelEltavolito("éajskbfapiuwvagklgwbaaléjbgéa.-m,_:?-:,-.,;'ojf\aw-]o"))

for i in range(1,11):
    print(i, "\t", i**2, "\t", i ** 3, "\t", i ** 5, "\t", i ** 10, "\t", i ** 20, sep = "")

elrendezes = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

# print(elrendezes.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))
for i in range(1,11):
    print(elrendezes.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))