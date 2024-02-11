# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def area(self,length,width):
        self.length = length
        self.width = width
        return self.length * self.width

rectangle = Rectangle()
area = rectangle.area(3,2)
print(f"Rectangle Area: {area}")