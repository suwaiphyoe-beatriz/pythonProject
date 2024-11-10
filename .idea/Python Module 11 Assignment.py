##Module 11
#No 1
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

if __name__ == "__main__":
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    donald_duck.print_information()
    print()
    compartment_no_6.print_information()

#No 2
from car import Car
class ElectricCar(Car):
    def __init__(self, reg_plate, max_speed, battery_capacity):
        super().__init__(reg_plate, max_speed)
        self.battery_capacity = battery_capacity
        self.battery_percentage = 100

    def drive(self, hours):
        super().drive(hours)
        self.battery_percentage -= (self.odometer / 100)
        self.battery_percentage = max(self.battery_percentage, 0)

class GasolineCar(Car):
    def __init__(self, reg_plate, max_speed, tank_volume):
        super().__init__(reg_plate, max_speed)
        self.tank_volume = tank_volume
        self.fuel_level = 100

    def drive(self, hours):
        super().drive(hours)
        self.fuel_level = (self.odometer / 100)
        self.fuel_level = max(self.fuel_level, 0)

if __name__ == "__main__":
    tesla = ElectricCar("ABC-15", 180, 52.5)
    audi = GasolineCar("ACD-123", 165, 32.3)

    tesla.accelerate(30)
    tesla.accelerate(50)
    tesla.accelerate(70)

    audi.accelerate(30)
    audi.accelerate(40)
    audi.accelerate(55)

    tesla.drive(3)
    audi.drive(3)

    print(f"Electric Car (Registration: {tesla.reg_plate})")
    print(f"Current Speed: {tesla.current_speed} km/h, Odometer: {tesla.odometer} km, Battery: {tesla.battery_percentage:.2f}%")

    print(f"\nGasoline Car (Registration: {audi.reg_plate})")
    print(f"Current Speed: {audi.current_speed} km/h, Odometer: {audi.odometer} km, Fuel level: {audi.fuel_level:.2f}%")
