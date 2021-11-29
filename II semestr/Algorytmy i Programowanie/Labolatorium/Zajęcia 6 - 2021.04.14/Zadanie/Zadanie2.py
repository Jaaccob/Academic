class Car:
    def __init__(self):
        self.engineCar = False

    def turn_on_engine(self, mode):
        if mode == "Car" and self.engineCar is False:
            self.engineCar = True

    def turn_off_engine(self, mode):
        if mode == "Boat" and self.engineCar is True:
            self.engineCar = True

    def __str__(self):
        return f'engine Car: {self.engineCar}\n'


class Boat:
    def __init__(self):
        self.engine = False
        super(Boat, self).__init__()

    def turn_on_screw(self, mode):
        if mode == "Boat" and self.engine is False:
            self.engine = True

    def turn_off_screw(self, mode):
        if mode == "Car" and self.engine is True:
            self.engine = False

    def __str__(self):
        return f'engine Boat: {self.engine}\n' + super().__str__()


class Amfibia(Boat, Car):
    def __init__(self):
        super(Amfibia, self).__init__()
        self.speed = 0
        self.fuel = 10
        self.mode = "Car"

    def start_engine(self):
        super().turn_on_engine(self.get_mode())

    def change_mode(self):
        if self.get_speed() == 0 and self.get_mode() == "Car":
            self.set_mode("Boat")
            super().turn_off_engine(self.get_mode())
        else:
            self.set_mode("Car")
            super().turn_on_engine(self.get_mode())

    def speed_up(self, speed):
        current = self.get_speed()
        current += speed
        self.set_speed(current)

    def speed_down(self, speed):
        current = self.get_speed()
        current -= speed
        self.set_speed(current)

    def fuel_condition(self):
        if self.get_fuel() == 10:
            return "Zbiornik pełny"
        elif 7 < self.get_fuel() < 10:
            return "Prawie peły zbiornik"
        elif 3 < self.get_fuel() <= 7:
            return "Połowa zbiornika"
        elif 0 < self.get_fuel() <= 3:
            return "Trzeba zatankować"
        else:
            return "Zbiornik pusty"

    def set_speed(self, speed):
        if isinstance(speed, int):
            self.speed = speed
        else:
            raise ValueError("Błędny typ danych. Powinien być int")

    def get_speed(self):
        return self.speed

    def set_fuel(self, fuel):
        if isinstance(fuel, int):
            self.fuel = fuel
        else:
            raise ValueError("Błędny typ danych. Powinien być int")

    def get_fuel(self):
        return self.fuel

    def set_mode(self, mode):
        if isinstance(mode, str):
            self.fuel = mode
        else:
            raise ValueError("Błędny typ danych. Powinien być int")

    def get_mode(self):
        return self.mode

    def __str__(self):
        return f'speed: {self.get_speed()}\n' \
               f'fuel: {self.get_fuel()}\n' \
               f'mode: {self.get_mode()}\n' + super().__str__()


amfibia = Amfibia()
print(amfibia)
amfibia.speed_up(10)
amfibia.speed_down(5)
print(amfibia)
print(amfibia.fuel_condition())
amfibia.start_engine()
print(amfibia)
