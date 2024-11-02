#No 1
class Car:
    def __init__(self,reg_plate,max_speed):
        self.reg_plate= reg_plate
        self.max_speed=max_speed
        self.current_speed=0
        self.odometer=0

if __name__=="__main__":
    tesla=Car("ABC-123",142)
    print (f"Registeration plate : {tesla.reg_plate}, Max speed : {tesla.max_speed}"
           f" ,Current speed : {tesla.current_speed}km/h, Odometer : {tesla.odometer}")
#No 2

class Car:
    def __init__(self,reg_plate,max_speed):
        self.reg_plate= reg_plate
        self.max_speed=max_speed
        self.current_speed=0
        self.odometer=0

    def accelerate(self,acce_speed):
        self.current_speed= min(max(self.current_speed+acce_speed,0),self.max_speed)
        print(self.current_speed)

if __name__=="__main__":
    tesla=Car("ABC-123",142)

    tesla.accelerate(30)
    tesla.accelerate(50)
    tesla.accelerate(70)
    print(f"Current speed of the car is {tesla.current_speed}km/h")
    tesla.accelerate(-200)
    print(f"Current speed after emergency brake={tesla.current_speed}km/h")
#No3

class Car:
    def __init__(self,reg_plate,max_speed):
        self.reg_plate= reg_plate
        self.max_speed=max_speed
        self.current_speed=0
        self.odometer=0

    def accelerate(self,acce_speed):
        self.current_speed= min(max(self.current_speed+acce_speed,0),self.max_speed)
        print(self.current_speed)

    def drive(self,hours):
        self.odometer+=self.current_speed*hours


if __name__=="__main__":
    tesla=Car("ABC-123",142)
    print (f"Registeration plate{tesla.reg_plate}, Max speed{tesla.max_speed}"
           f"Current speed{tesla.current_speed}km/h,Odometer{tesla.odometer}")
    tesla.accelerate(30)
    tesla.accelerate(50)
    tesla.accelerate(70)
    print(f"Current speed of the car is {tesla.current_speed}km/h")
    tesla.accelerate(-200)
    print(f"Current speed after emergency brake={tesla.current_speed}km/h")
    tesla.accelerate(60)
    tesla.drive(1.5)
    print(f"The distance the car travelled was {tesla.odometer}")
# No 4
import random

class Car:
    def __init__(self, reg_plate, max_speed):
        self.reg_plate = reg_plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0

    def accelerate(self, acce_speed):
        self.current_speed = min(max(self.current_speed + acce_speed, 0), self.max_speed)

    def drive(self, hours):
        self.odometer += self.current_speed * hours


if __name__ == "__main__":

    cars = []
    for i in range(10):
        max_speed = random.randint(100, 200)
        cars.append(Car(f"ABC-{i + 1}", max_speed))


    odomax = 0
    while odomax < 10000:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            odomax = max(car.odometer, odomax)

    print(f"\nRace Results:")
    print(f"{'Reg Plate':<10} {'Max Speed (km/h)':<15} {'Odometer (km)':<15}")
    print("=" * 40)
    for car in cars:
        print(f"{car.reg_plate:<10}  {car.max_speed:<15}  {car.odometer:<15}")






