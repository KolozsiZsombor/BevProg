import sys

randomList = ["a",0,2]

for i in randomList:
    try:
        print(f"The etry is: {i}")
        r = 1/int(i)
        break
    except:
        print(f"Ooops!{sys.exc_info()[0]} occured")
        print("Next entry.")
        print()

print(f"The recoprocal of {i} is {r}")