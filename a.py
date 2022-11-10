import random

i = 0
while i <= 50000:
    i += 1
    with open("be2.txt","a") as f:
        f.write(str(random.randint(0,7000)))
        f.write("\n")