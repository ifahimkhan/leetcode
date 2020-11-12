class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = {
            1: [0, big],
            2: [0, medium],
            3: [0, small]
        }

    def addCar(self, carType: int) -> bool:
        if self.slots[carType][0] >= self.slots[carType][1]:
            return False
        self.slots[carType][0] += 1
        return True
