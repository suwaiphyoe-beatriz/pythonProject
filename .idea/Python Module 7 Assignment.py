def get_season(month):
    seasons = ("Winter","Spring","Summer","Autumn" )

    if month == 12 or month in (1, 2):
        return seasons[0]
    elif month in (3, 4, 5):
        return seasons[1]
    elif month in (6, 7, 8):
        return seasons[2]
    elif month in (9, 10, 11):
        return seasons[3]
    else:
        return "Invalid month number. Please enter a number between 1 and 12."

def main():
    month = int(input("Enter the number of the month (1-12): "))
    season = get_season(month)
    print(f"The season is: {season}")
main()



def main():
    names = set()

    while True:
        name = input("Enter a name (or press Enter to quit): ")

        if name == "":
            break

        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nList of names:")
    for name in names:
        print(name)
main()



def main():
    airports = {}

    while True:
        print("\nOptions:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            icao_code = input("Enter the ICAO code: ").strip().upper()
            airport_name = input("Enter the name of the airport: ").strip()
            airports[icao_code] = airport_name
            print(f"Airport {airport_name} with ICAO code {icao_code} has been added.")

        elif choice == "2":
            icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
            if icao_code in airports:
                print(f"The airport with ICAO code {icao_code} is: {airports[icao_code]}")
            else:
                print("Airport not found.")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")
main()
