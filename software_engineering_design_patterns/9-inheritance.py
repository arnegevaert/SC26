class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def move_at(self, speed):
        self.speed = speed

class Car(Vehicle):
    def info(self):
        print(f"I'm driving at {self.speed}")

car = Car(0)
car.move_at(30)
car.info()
