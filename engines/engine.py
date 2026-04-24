from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self):
        self.speed = 0

    def increase(self):
        self.speed += 1

    def decrease(self):
        if self.speed > 0:
            self.speed -= 1

    @abstractmethod
    def update_speed(self, car_speed):
        pass
