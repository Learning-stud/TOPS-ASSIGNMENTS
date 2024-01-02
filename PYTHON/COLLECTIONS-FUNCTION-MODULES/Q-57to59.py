# Write a Python program to calculate the area of a trapezoid
#Area = (a+b)/2 * h
#Median = (a+b) / 2.
base1 = float(input('Please Enter the First Base of a Trapezoid: '))
base2 = float(input('Please Enter the Second Base of a Trapezoid: '))
height = float(input('Please Enter the Height of a Trapezoid: '))

# calculate the area
Area = 0.5 * (base1 + base2) * height

# calculate the Median
Median = 0.5 * (base1+ base2)

print("\n Area of a Trapezium = %.2f " %Area)
print(" Median of a Trapezium = %.2f " %Median)


print("---------------------------------------------------------------")
#Calculate the area of a parallelogram
# area = h · b
base = float(input('Length of base: '))
height = float(input('Measurement of height: '))
area = base * height
print("Area is: ", area)


print("---------------------------------------------------------------")

#Calculate surface volume and area of a cylinder
#area formula: pi x r^2 x h
# volume formula: 2 x pi x r x h + 2 x pi x r^2

# First, We declared PI variable and assigned the value as 3.14.
PI = 3.14
# The below statements will ask the user to enter radius and height values and it will assign the user input values to respected variables.


radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))

 # calculating Volume, Surface Area, Lateral Surface Area, Top Or Bottom Surface Area of a Cylinder using their respective Formulas:

sa = 2 * PI * radius * (radius + height)
Volume = PI * radius * radius * height
L = 2 * PI * radius * height
T = PI * radius * radius


print("\n The Surface area of a Cylinder = %.2f" %sa)
print(" The Volume of a Cylinder = %.2f" %Volume)
print(" Lateral Surface Area of a Cylinder = %.2f" %L);
print(" Top OR Bottom Surface Area of a Cylinder = %.2f" %T)

print("---------------------------------------------------------------")
