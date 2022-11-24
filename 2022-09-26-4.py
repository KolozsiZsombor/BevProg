def fun(a):
    if a < 4:
        b = a / (a-3)
    print(f"The b value is: {b}")
try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occured and Handeled")
except NameError:
    print("NameError Occured and Handeled")
