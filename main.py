from factory.car_factory import CarFactory

def test_car(car):
    car.start()
    car.accelerate()
    car.accelerate()
    car.brake()
    car.brake()
    car.stop()
    print("-" * 30)


def main():
    print("=== Gas Car ===")
    gas_car = CarFactory.create_car("gas")
    test_car(gas_car)

    print("=== Electric Car ===")
    electric_car = CarFactory.create_car("electric")
    test_car(electric_car)

    print("=== Hybrid Car ===")
    hybrid_car = CarFactory.create_car("hybrid")
    test_car(hybrid_car)

    print("=== Replace Engine (Gas -> Hybrid) ===")
    CarFactory.replace_engine(gas_car, "hybrid")
    test_car(gas_car)


if __name__ == "__main__":
    main()