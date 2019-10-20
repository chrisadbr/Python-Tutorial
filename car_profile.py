class Car:

    def __init__(self):
        self.mileage = 10000
        self.brand = 'BMW'


c1 = Car()
c2 = Car()
c1.brand = 'Volvo'
c1.mileage = 2000
print(c2.mileage, c2.brand)
print(c1.mileage, c1.brand)
