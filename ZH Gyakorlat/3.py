def main():
    l = int(input("How many numbers of the fibonacchi seqence do you wish to generate? "))
    i = 0
    num1 = 0
    num2 = 1
    num3 = 0
    while i != l:
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        i += 1
        print(num3)


if __name__ == "__main__":
    main()
