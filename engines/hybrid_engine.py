from engines.engine import Engine
from engines.gas_engine import GasEngine
from engines.electric_engine import ElectricEngine

class HybridEngine(Engine):
    def __init__(self):
        super().__init__()
        self.gas = GasEngine()
        self.electric = ElectricEngine()

    def update_speed(self, car_speed):
        if car_speed < 50:
            print("[Hybrid] Using Electric Engine")
            self.electric.update_speed(car_speed)
        else:
            print("[Hybrid] Using Gas Engine")
            self.gas.update_speed(car_speed)