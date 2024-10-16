import random
def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        result = roll_dice()
        print(f"You rolled: {result}")
        if result == 6:
            print('You rolled 6! The program is stopping!.')
            break
main()


import random
def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    roll = 0
    while roll != sides:
        roll = roll_dice(sides)
        print(f"Rolled: {roll}")
main()


def gallons_to_liters(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter the volume in gallons (Enter negative value to quit): "))
        if gallons < 0:
            print("Invalid input!Exiting the program.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is approximately {liters:.2f} liters.")
main()


def sum_of_list(numbers):
    return sum(numbers)

def main():
    list = [4,9,88,23,3]
    total = sum_of_list(list)
    print(f"The sum of the list {list} is: {total}")
main()


def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    original_list = [1, 2, 33, 46, 53, 68, 17, 78, 29, 10]
    removed_list = remove_odd_numbers(original_list)

    print(f"Original list: {original_list}")
    print(f"List after removing odd numbers: {removed_list}")
main()


import math

def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    area_square_meters = area / 10000
    unit_price = price / area_square_meters
    return unit_price

def main():
    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    print(f"Unit price of the first pizza: {unit_price1:.2f} euros per square meter.")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros per square meter.")

    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")
main()
