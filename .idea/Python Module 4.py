number=1
while 1<=number<=1000:
    if number%3==0:
        print(number)
    number=number+1

while True:
    number = float(input("Enter a number in inches:"))
    result = number * 2.54
    if number <0 :
        print("The program ends")
        break
    print(f" {number} inches is equal to {result} centimeters")

largest=0
smallest=0
number=input("Enter a number:")
largest = int(number)
smallest = int(number)
while True:
    if number=="":
        print("The program quits")
        break
    else:
        num = int(number)
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
    number = input("Enter a number:")
print("The largest number you entered is", largest)
print("The smallest number you entered is",smallest)

import random
num=random.randint(1,10)
while True:
    guess=int(input("Enter a number:"))
    if guess> num:
        print("Too high")
    elif guess< num:
        print("Too low")
    else:
        print("You are correct")
        break


username=("python")
password="rules"
max_attempts=5
attempts=0
while attempts<max_attempts:
    user_name=input("Enter your username:")
    pw=input("Enter your password:")
    if username==user_name and pw==password:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Invalid username or password")
else:
    print("Access denied")

import random
def approximate_pi(num_points):
    points_in_circle=0
    counts=0
    while counts< num_points:
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if x**2+y**2<1:
            points_in_circle +=1
        counts+=1
    return 4*points_in_circle/num_points
num_points=1000000
approximation_of_pi=approximate_pi(num_points)
print(f"Approximation of pi after {num_points} points:{approximation_of_pi}")
