import math 

# Hypotenuse = sqrt(length^2 + width^2)
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

hypotenuse = math.sqrt(pow(length, 2) + pow(width, 2))

print(f"The hypotenuse is: {hypotenuse}") 