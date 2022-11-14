bejarhatom = frozenset({1,3,42,2,7,5,42,42,3,14})

for sorszam,elem in enumerate(bejarhatom):
    if elem > 3 and elem < 4:
        kimenet = True, elem, sorszam
    else:
        kimenet = False

print(kimenet)