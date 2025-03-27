задание 1

class Rectangle:
    def __init__(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Стороны прямоугольника должны быть числами")
        if a <= 0 or b <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительными")
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Длина стороны а должна быть числом")
        if value <= 0:
            raise ValueError("Длина должна а быть положительной")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Длина стороны b должна быть числом")
        if value <= 0:
            raise ValueError("Длина стороны b должна быть положительной")
        self._b = value

    @property
    def area(self):
        return self._a * self._b

    @property
    def perimeter(self):
        return 2 * (self._a + self._b)

# Примеры проверки
rect = Rectangle(3, 4)  # OK
# rect = Rectangle(-1, 2)  # ValueError
# rect = Rectangle("5", 2)  # TypeError

print(rect.area)  # 12

rect.a = 5.5  # OK
# rect.b = -10  # ValueError

задание 2
class ComplexNumber:
    def __init__(self, real, imag):
        if not isinstance(real, (int, float)) or not isinstance(imag, (int, float)):
            raise TypeError("Обе части комплексного числа должны быть числами")
        self._real = real
        self._imag = imag

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно складывать только комплексные числа")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imag})"

# Примеры проверки
if __name__ == "__main__":
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = c1 + c2  # ComplexNumber(4,6)
    print(c3)  # ComplexNumber(4, 6)

    try:
        c4 = c1 + 5  # TypeError
    except TypeError as e:
        print(e)  # Можно складывать только комплексные числа

    try:
        c5 = ComplexNumber("a", 2)  # TypeError
    except TypeError as e:
        print(e)  # Обе части комплексного числа должны быть числами