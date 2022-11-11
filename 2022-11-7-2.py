try:
    file = open("be.txt","r",encoding="UTF-8")
    tartalom = file.readlines()

    for sor in tartalom:
        sor = sor.strip()   # sorvégjel eltávolítása
        print(sor)

    file.close()

except FileNotFoundError as file:
    print("FileNotFound")