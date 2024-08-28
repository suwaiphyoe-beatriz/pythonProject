name= input("enter your name?:")
print("Hello," +name + "!")

import math
radius= float(input("enter the radius of the circle:"))
area = math.pi*radius**2
print ("the area of the circle:", area)

length=float(input("enter the length of the rectangle:"))
width= float(input("enter the width of the rectangle:"))

perimeter= length*2 + width *2
area= length* width
print("the perimeter of the rectangle:",perimeter)
print ("the area of the rectangle:",area)

number1= int(input("enter the first number:"))
number2=int(input("enter the second number:"))
number3=int(input("enter the third number:"))

sum= number1+number2+number3
product=number1*number2*number3
average=sum/3
print("the sum of the numbers:",sum)
print("product of the numbers:",product)
print("average of the numbers:",average)

talent= float(input("Enter talents:"))
pound= float(input("Enter pounds:"))
lot= float(input("Enter lots:"))
mass= ((talent*20+pound)*32+lot)*13.3
inkg= mass/1000
ing=mass%1000
print("The weight in modern units:", inkg, f"kilograms and {ing:.2f} grams")

import random
digit1=str(random.randint(0,9))
digit2=str(random.randint(0,9))
digit3=str(random.randint(0,9))
print("A 3-digit code where each number is between 0 and 9:"+digit1+digit2+digit3)
digit1=str(random.randint(1,6))
digit2=str(random.randint(1,6))
digit3=str(random.randint(1,6))
digit4=str(random.randint(1,6))
print("A 4-digit code where each number is between 1 and 6:" +digit1+digit2+digit3+digit4)
