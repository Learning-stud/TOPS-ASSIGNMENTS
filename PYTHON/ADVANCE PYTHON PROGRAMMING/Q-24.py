#• Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle



class Circle:
    def area(self,radius):
        self.radius = radius
        return 3.14 * self.radius**2

    def perimeter(self,radius):
        self.radius = radius
        return 2 * 3.14 * self.radius

circle = Circle()
area = circle.area(5)
perimeter = circle.perimeter(5)
print(f"Circle Area: {area}, Perimeter: {perimeter}")