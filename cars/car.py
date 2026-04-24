class Car:
    def __init__(self, engine):
        self.engine = engine
        self.speed = 0
        self.running = False

    def start(self):
        self.running = True
        self.speed = 0
        print("Car started.")

    def stop(self):
        if self.speed == 0:
            self.running = False
            print("Car stopped.")
        else:
            print("Stop failed: speed must be 0")

    def accelerate(self):
        if not self.running:
            print("Start the car first.")
            return

        if self.speed < 200:
            self.speed += 20
            print(f"Accelerating... Speed = {self.speed}")
            self.engine.update_speed(self.speed)
        else:
            print("Max speed reached.")

    def brake(self):
        if self.speed > 0:
            self.speed -= 20
            print(f"Braking... Speed = {self.speed}")
            self.engine.update_speed(self.speed)
        else:
            print("Car already stopped.")

    def change_engine(self, new_engine):
        self.engine = new_engine
        print("Engine replaced successfully.")