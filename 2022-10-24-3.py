m = ["a","e","i","o","u","A","E","I","O","U"]
s = "Hello World"
for i in s:
    if i not in m:
        print(i,end="")