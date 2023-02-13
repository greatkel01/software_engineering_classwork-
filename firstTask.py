import math

def circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius

    print("The area of the circle is: {:.2f}".format(area))
    print("The circumference of the circle is: {:.2f}".format(circumference))

radius = float(input("Enter the radius of the circle: "))
circle_properties(radius)