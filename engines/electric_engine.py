from engines.engine import Engine

class ElectricEngine(Engine):
    def update_speed(self, car_speed):
        print(f"[Electric Engine] Running at car speed: {car_speed} km/h")