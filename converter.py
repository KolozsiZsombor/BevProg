def main():
    print("Adjn meg egy számot és egy mértékegységet (cm/inch): ")
    l = int(input())
    ms = input()
    msf = 0
    if ms == "cm":
        msf = l * 2.54
        return(f"{msf} inches")
    elif ms == "inch":
        msf = l / 2.54
        return(f"{msf} cm")
    else:
        print("Not correct unit!")
    return msf

if __name__ == "__main__":
    print(main())