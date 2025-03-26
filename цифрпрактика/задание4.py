class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __getattr__(self, item):
        return "This attribute is not available"

# Пример использования:
c = Car("Toyota", "Audi")
print(c.make)
print(c.color)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name not in ['width', 'height']:
            raise AttributeError("Local attributes are not allowed")
        else:
            super().__setattr__(name, value)

r = Rectangle(10, 20)
r.width = 15  
r.height = 25 
try:
  r.color = 'red' 
except AttributeError as e:
  print(e)
