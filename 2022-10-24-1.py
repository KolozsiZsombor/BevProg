from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES


ss = "Hello World!"
tt = ss.lower()
tt = ss.upper()
tt = ss.capitalize()
print(tt)

gyumi = "banán"
m = gyumi[1]
print(m)

lista = list(enumerate(gyumi))
print(lista)

hossz = len(gyumi)
print(hossz)

sz = len(gyumi)
utolso = gyumi[sz-1]
print(utolso)

print(gyumi[::-1])

i = 0
while i < len(gyumi):
    karakter = gyumi[i]
    print(karakter)
    i += 1

print()

for c in gyumi:
    print(c)
