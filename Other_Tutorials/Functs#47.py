# assign a new name to a function
length = float(input("Enter the length of the rectangle\n"))
width = float(input("Enter the width of the rectangle\n"))
def Area(length, width):
    Area = length * width
    return Area
print("The area of the rectangle is:")
print(Area(length, width))

AreaOfRectangle = Area
print("The area of the rectangle with the renamed function is:")
print(AreaOfRectangle(length, width))
