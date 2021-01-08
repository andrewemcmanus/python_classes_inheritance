# Class

class Car():
    # This is a car class that displays the make, model and color
    # SELF: equivalent of "this" in javascript
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.gas = 100
    def __str__(self):
        return "{}, {}, {}".format(self.make, self.model, self.color)
      # this __str__ returns the actual object, not the name/memory location below
    def drive(self):
        print('Vroom')
        self.gas -= 10
        # subtract 10 each time
        print(self.gas)

    def fill_tank(self):
        self.gas = 100
        print(self.gas)

    def check_gas(self):
        print(f"Gas handle: {self.gas}")

# don't need to include SELF when you call a class:
car1 = Car('Mercedes', 'C300', 'White')
# printing returns the location in memory?
# <__main__.Car object at 0x10f2604f0>

# print(car1)
# # returns the attributes:
# print(car1.make)
# print(car1.model)
# print(car1.color)

# autogenerated help file for a class! begin with this:
# help(car1)
# invoke the 'drive' method above:
car1.drive()
car1.drive()
car1.check_gas()
car1.fill_tank()
car1.check_gas()