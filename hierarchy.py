class Vehicle:
    def __init__(self,Vehicle):
        print(Vehicle,'class Vehicle')

class LVehicle(Vehicle):
    def __init__(self,LVehicle):
        print(LVehicle,'class LVehicle')
        super().__init__(LVehicle)

class WVehicle(Vehicle):
    def __init__(self,WVehicle):
        print(WVehicle,'class WVehicle')
        super().__init__(WVehicle)

class AVehicle(Vehicle):
    def __init__(self,AVehicle):
        print(AVehicle,'class AVehicle')
        super().__init__(AVehicle)

class TwoWheeler(LVehicle):
    def __init__(self,TwoWheeler):
        print(TwoWheeler,'class TwoWheeler')
        super().__init__(TwoWheeler)

class FourWheeler(LVehicle):
    def __init__(self,FourWheeler):
        print(FourWheeler,'class FourWheeler')
        super().__init__(FourWheeler)

class Powered(AVehicle):
    def __init__(self,Powered):
        print(Powered,'class Powered')
        super().__init__(Powered)

class Unpowered(AVehicle):
    def __init__(self,Unpowered):
        print(Unpowered,'class Unpowered')
        super().__init__(Unpowered)

class Car(FourWheeler):
    def __init__(self,Car):
        print(Car,'class Car')
        super().__init__(Car)

class Motorcycle(TwoWheeler):
    def __init__(self,Motorcycle):
        print(Motorcycle,'class Motorcycle')
        super().__init__(Motorcycle)

class Bicycle(TwoWheeler):
    def __init__(self,Bicycle):
        print(Bicycle,'class Bicycle')
        super().__init__(Bicycle)

class Propeller(Powered):
    def __init__(self,Propeller):
        print(Propeller,'class Propeller')
        super().__init__(Propeller)

class Jet(Powered):
    def __init__(self,Jet):
        print(Jet,'class Jet')
        super().__init__(Jet)

a=Jet("F16")
print(Jet.__mro__)

b=Propeller("Cessna")
print(Propeller.__mro__)

c=Bicycle("BMX")
print(Bicycle.__mro__)

d=Motorcycle("Kawasaki")
print(Motorcycle.__mro__)

e=Car("Thrust SSC")
print(Car.__mro__)
