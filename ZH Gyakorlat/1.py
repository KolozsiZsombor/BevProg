def main():
    flag = False
    num = int(input("Please give a number"))
    if num == 2:
        return f"{num} is a prime!"
    elif num > 2:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return f"{num} is not a prime number!"
    else:
        return f"{num} is a prime number!"


if __name__ == "__main__":
    print(main())
