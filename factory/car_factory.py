from engines.gas_engine import GasEngine
from engines.electric_engine import ElectricEngine
from engines.hybrid_engine import HybridEngine
from cars.car import Car

class CarFactory:

    @staticmethod
    def create_car(engine_type):
        if engine_type == "gas":
            return Car(GasEngine())
        elif engine_type == "electric":
            return Car(ElectricEngine())
        elif engine_type == "hybrid":
            return Car(HybridEngine())
        else:
            raise ValueError("Invalid engine type")

    @staticmethod
    def replace_engine(car, engine_type):
        if engine_type == "gas":
            car.change_engine(GasEngine())
        elif engine_type == "electric":
            car.change_engine(ElectricEngine())
        elif engine_type == "hybrid":
            car.change_engine(HybridEngine())
        else:
            raise ValueError("Invalid engine type")