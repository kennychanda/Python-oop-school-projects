class Car:

  def __init__(self, model, year, mileage, topspeed):

    self.model = model
    self.year = year
    self.mileage = mileage
    self.topspeed = topspeed
    
a = Car("Tesla Roadster", 2018, "N.A", 400)

print(a.model)
print(a.year)
print(a.mileage)
print(a.topspeed)
