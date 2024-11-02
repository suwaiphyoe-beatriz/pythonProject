#Module 10
#No 1
class Elevator:
    def __init__(self,bottom,top):
        self.bottom= bottom
        self.top= top
        self.current= bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"Elevator is moving from {self.current} to {self.current+1}")
            self.current +=1
            return True
        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f" Elevator is moving from {self.current} to {self.current-1}")
            self.current-=1
            return True
        else:
            return False

    def go_to_floor(self,floor_num):
        if  floor_num > self.current:
            for i in range (floor_num - self.current):
                if not self.floor_up():
                    break
        elif  floor_num< self.current:
            for i in range (floor_num -floor_num):
                if not self.floor_down():
                    break

        else:
            print(f"The elevator is already at this floor{self.current}")

h= Elevator(1,6)
target_floor= int(input("To which floor do you want to go to?(1-6):"))
h.go_to_floor(target_floor)

# No 2 + 3 Extending the program by adding building class+ adding fire alarm

class Building:
    def __init__(self, bottom,top,ele_num):
        self.ele_num=[]
        for i in range (ele_num):
            self.ele_num.append(Elevator(bottom, top))

    def run_elevator(self,elevator, floor_num):
        print(f"The {elevator}is moving")
        self.ele_num[elevator-1].go_to_floor(floor_num)
#for No 3
    def fire_alarm (self):
        print("There is a fire!!!")
        for i in self.ele_num:
            i.go_to_floor(i.bottom)

print(" \nElevators in the building are: ")
building1= Building(1,7,3)
building1.run_elevator(1,5)
building1.run_elevator(2,3)
# for No 3
building1.fire_alarm()

#No 4
import random

class Car:
    def __init__(self, reg_plate, max_speed):
        self.reg_plate = reg_plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0

    def accelerate(self, acceleration):
        self.current_speed = min(max(self.current_speed + acceleration, 0), self.max_speed)

    def drive(self, time):
        self.odometer += self.current_speed * time

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1.0)

    def print_status(self):
        print(f"{self.name}:")
        print("Plate    Speed   Odometer")
        print("--------------------------")
        for car in self.cars:
            print(f"{car.reg_plate:6}: {car.current_speed:3} km/h, {car.odometer:.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.odometer >= self.distance:
                return True
        return False

cars = [Car("ABC-" + str(i + 1), random.randint(100, 200)) for i in range(10)]

race1 = Race("Grand Demolition Derby", 8000.0, cars)
n = 0

while not race1.race_finished():
    race1.hour_passes()
    n += 1
    if n % 10 == 0:
        print(f"After {n} hours")
        race1.print_status()

print("Race has finished!")
race1.print_status()
