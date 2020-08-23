#Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.
'''
Classic Heron's Formula
s = (a+b+c)/2 = 6
Area = √( s(s-a)(s-b)(s-c) )
'''
class Parent:
    def __init__(self):
        print("Area of Triangle with 3 sides")
        self.aSide = int(input("Enter first side length of the triangle- "))
        self.bSide = int(input("Enter 2nd side of the triangle- "))
        self.cSide = int(input("Enter 3rd side of the triangle- "))

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

    def areaOfTriangle(self):
        s = (self.aSide + self.bSide + self.cSide)/2

        # semi-perimeter of the triangle
        print("Semi-perimeter of the triangle=",s)

        area = (s * (s - self.aSide) * (s - self.bSide) * (s - self.cSide)) ** 0.5
        print("Area of Triangle=",area,"sq unit")

c = Child()
c.areaOfTriangle()