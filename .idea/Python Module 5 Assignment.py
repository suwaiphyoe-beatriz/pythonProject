import random
num_dice= int(input("How many dices do you want to roll?:"))
total_sum=0
for i in range(num_dice):
    total_sum+=random.randint(1,6)
print(f"The sum of the rolled dices is {total_sum}")

def greatest():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    numbers.sort(reverse=True)
    top_five = numbers[:5]
    print("The five greatest numbers are:", top_five)
greatest()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def main():
    user_input = input("Please enter an integer: ")

    try:
        number = int(user_input)
        if is_prime(number):
            print(f"{number} is a prime number!")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("That's not a valid integer. Please try again.")
main()

def city():
    cities = []
    for _ in range(5):
        city = input("Enter the name of a city: ")
        cities.append(city)

    print("\nThe cities you entered are:")
    for city in cities:
        print(city)
city()