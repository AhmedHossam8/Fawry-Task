from engines.engine import Engine

class GasEngine(Engine):
    def update_speed(self, car_speed):
        print(f"[Gas Engine] Running at car speed: {car_speed} km/h")