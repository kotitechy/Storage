class Engine:
    def start_engine(self):
        print("Engine started.")

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle, Engine):
    def drive(self):
        print("Car is being driven.")

class Bicycle(Vehicle, Engine):
    def pedal(self):
        print("Bicycle is being pedaled.")

# Create instances of Car and Bicycle
car = Car()
bike = Bicycle()

# Using methods from both parent classes
car.move()          # Output: Vehicle is moving.
car.start_engine()  # Output: Engine started.
car.drive()         # Output: Car is being driven.

bike.move()         # Output: Vehicle is moving.
bike.start_engine() # Output: Engine started.
bike.pedal()        # Output: Bicycle is being pedaled.
