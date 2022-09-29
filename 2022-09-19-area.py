from math import pi


def main(name):
    name = name.lower()
    if name == "rectengale":
        l = int(input("Gib length! "))
        w = int(input("Gib width! "))
        rectArea = l*w
        print(f"The area of the rectengle is: {str(rectArea)}")
    elif name == "square":
        s = int(input("Gib square's side length! "))
        squareArea = s * s
        print(f"The area of the square is: {str(squareArea)}")
    elif name == "triangle":
        l = int(input("Gib triangle's length! "))
        w = int(input("Gib triangle's width! "))
        triArea = 0.5 * w * l
        print(f"The area of the triangle is: {str(triArea)}")
    elif name == "circle":
        r = int(input("Enter the circle's radius: "))
        cirlceArea = r * r * pi
        print(f"The circle's area is: {str(cirlceArea)}")
    else:
        print("Sorry this shape is not avaliable!")


if __name__ == "__main__":
    print("Calculate Shape Area.")
    shapeName = input("Enter the name of the shape whose area you want to find: ")
    main(shapeName)
