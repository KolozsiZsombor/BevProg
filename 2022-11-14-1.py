bejarhatom = [1,2,3,4,5,6,16]
for elem in bejarhatom:
    if elem % 3 == 1 and elem > 5:
        kimenet = True, elem
    else:
        kimenet = False

print(kimenet)