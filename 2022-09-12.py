"""

x = 1
y = 2.8

print(x)
print(y)

a = float(x)
b = int(y)

print(a)
print(b)


print(type(a))
print(type(b))

##########


for x in("banana"):
    print(x)

a = "Hellob World!"

print(len(a))

txt = "The best things in life are free!"

if "free" not in txt:
    print("Yes")

print(txt.upper())
print(txt.lower())

a = "Hello, world"

print(a.split(","))

a = "Hello"
b = "World"
c = a + b

print(c,a + b)
#########


age = 266
txt = "I am {}"

print(txt.format(age))

quantity = 3
itemNo = 44
price = 70.78
myOrder = "I want {} pieces of {} for {} dollars!"

print(myOrder.format(quantity,itemNo,price))

###########

"""


print("Adjon meg 2 egész számot")

a = 20 # int(input())
b = 30 # int(input())

if a > b:
    print("A is greater than B!")
else:
    print("B is greater than A")

thisList = ["apple","banana","orange","ubi","mango","peach","melon"]

print(thisList[2:5])
print(thisList[2:4])
print(thisList[-4:-1])
print(thisList[::-1])
print(thisList[0:len(thisList):3])

# thisList[1:3] = ["valami","cica"]

thisList.insert(2,"watermelon")

thisList.append("watermelon")

print(thisList)