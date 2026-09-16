class Drivable:
    def get_speed(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

class Locatable:
    def get_location(self) -> Coordinate:
        raiseNotImplementedError()

class Car(Drivable, Locatable):
    ...
