"""This project can be used to determine the area of a selected shape"""

from time import sleep

#Prompts user to select a given shape to calculate

print("The calculator is now starting!")
option = input("""Please select a shape:
triangle, circle, trapezoid, square, diamond
or rectangle: """)

option = option.upper()

#Prompts user for applicable measurements for each different shape, then calculates area

if option == "CIRCLE" or option == "C":
  radius = float(input("Please enter the radius: "))
  area = 3.14159 * radius ** 2
  print("I am calculating the answer...")
  sleep(2)
  print("The area is %s!" % area)
elif option == "TRIANGLE" or option == "T":
  base = float(input("Please enter the length of the base: "))
  height = float(input("Please enter the height of the triangle: "))
  area = .5 * base * height
  print("I am calculating the answer...")
  sleep(2)
  print("The area is %s!" % area)
elif option == 'TRAPEZOID':
  base1 = float(input("Please enter the top base length: "))
  base2 = float(input("Please enter the bottom base length: "))
  height = float(input("Please enter the height of the trapezoid: "))
  hbase = base1 + base2
  area = hbase / 2 * height
  print("I am calculating the answer...")
  sleep(2)
  print("The area is %s!" % area)
elif option == "SQUARE" or option == "S":
  side = float(input("Please enter the length of the side: "))
  area = side ** 2
  print("The area is %s!" % area)
elif option == "RECTANGLE" or option == "R":
  length = float(input("Please enter the length: "))
  width = float(input("Please enter the width: "))
  area = length * width
  print("I am calculating the answer...")
  sleep(2)
  print("The area is %s!" % area)
elif option == "DIAMOND" or option == "D":
  d1 = float(input("Please enter the length of the first diagonal: "))
  d2 = float(input("Please enter the length of the second diagonal: "))
  inside = d1 * d2
  area = inside / 2
  print("I am calculating the answer...")
  sleep(2)
  print("The area is %s!" % area)
else:
  print("""That is not a valid option. Please select 
  a valid shape.""")
sleep(2)
print("The calculator is now shutting down.")
