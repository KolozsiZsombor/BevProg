def main():
    c = 0
    a = int(input("Enter 'a' value: "))
    b = int(input("Enter 'b' value: "))
    try:
        c = a/b
    except ZeroDivisionError:
        print("Division by zero not allowed")
        print("Out of try except block")

    if c != 0:
        print(c)
        print("Out of try except block")



if __name__ == "__main__":
    main()