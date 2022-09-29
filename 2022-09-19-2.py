def main(name):
    marks = {"James":90,"Jule":60,"Bob":75,"Katy":90}
    for student in marks:
        if student == name:
            print(marks[student])
            break
    else:
        print("No entry with that name found.")

if __name__ == "__main__":
    print("Maths test results.")
    studentName = input("Type students name: ")
    main(studentName)