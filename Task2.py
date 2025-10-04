# Task 2 Using the Math Module for Calculations
import math


#Square root
a = int(input("Enter a number :"))
print("Square root: ",math.sqrt(a))


#Natural logarithm
# Check karein number positive ho
if a > 0:
    result = math.log(a)
    print("Logarithm of ",a,"is : ", result)
else:
    print("Negative Number")



# Sine of the number (in radians)
result = math.sin(a)
print("Sine",a," is :",result)