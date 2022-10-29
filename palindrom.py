def main():
    wd = input("Agjon meg egy szavat!: ")
    wdr = wd[::-1]
    if wd == wdr:
        return True
    else:
        return False

if __name__ == "__main__":
    main()