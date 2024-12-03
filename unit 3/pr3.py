class Vehicle:
    def speed(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def speed(self):
        return "The car can go up to 200 km/h."

class Bike(Vehicle):
    def speed(self):
        return "The bike can go up to 100 km/h."

class Train(Vehicle):
    def speed(self):
        return "The train can go up to 300 km/h."

def show_speed(vehicle):
    print(vehicle.speed())

if __name__ == "__main__":
    car = Car()
    bike = Bike()
    train = Train()

    print("Vehicle Speeds:")
    show_speed(car)
    show_speed(bike)
    show_speed(train)