import math

class Shape:
    def area(self):
        raise NotImplementedError("Метода area() не существует")

    def perimeter(self):
        raise NotImplementedError("Метода perimeter() не существует")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(5)
print("Площадь круга:", circle.area())
print("Периметр круга:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle.area())
print("Периметр прямоугольника:", rectangle.perimeter())





class Animal:
    def sound(self):
        raise NotImplementedError("Метод sound() не реализован")

class Dog(Animal):
    def sound(self):
        return "Гав-гав"

class Cat(Animal):
    def sound(self):
        return "Мяу"

class Cow(Animal):
    def sound(self):
        return "Муу"


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.sound())