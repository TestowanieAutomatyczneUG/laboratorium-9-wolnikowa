from unittest import TestCase, main
from unittest.mock import *


class Car:
    def needsFuel(self):
        pass

    def getEngineTemperature(self):
        pass

    def driveTo(self, destination):
        pass


class CarImpl:
    def __init__(self, car: Car):
        self.car = car

    def carNeedsFuel(self):
        if self.car.needsFuel():
            return "needs fuel!"
        return "does not need fuel!"

    def carGetEngineTemperature(self):
        if self.car.getEngineTemperature():
            temp = self.car.getEngineTemperature()
            return str(temp) + " C"
        return "undefined"

    def carDriveTo(self, destination):
        if self.car.driveTo(destination):
            return str(destination)
        return "No destination"


class test_Carimpl(TestCase):
    def test_needs_fuel(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carNeedsFuel(), "does not need fuel!")

    def test_does_not_need_fuel(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carNeedsFuel(), "needs fuel!")

    def test_temperature_undefined(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carGetEngineTemperature(), "undefined")

    def test_no_destination(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carDriveTo(None), "No destination")

    def test_destination_Sopot(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = "Sopot"
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carDriveTo("Sopot"), "Sopot")

    def test_temperature_defined(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 36.6
        carImpl = CarImpl(car)
        self.assertEqual(carImpl.carGetEngineTemperature(), "36.6 C")






if __name__ == '__main__':
    main()