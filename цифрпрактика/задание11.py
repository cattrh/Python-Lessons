# 3


class Student():
    __slots__ = ('name', 'age', 'grade',)

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Student:
    __slots__ = ('name', 'age', 'grade')

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def average_grade(students):
    total = sum(student.grade for student in students)
    return total / len(students)


students = [
    Student("Аня", 20, 85),
    Student("Миша", 21, 90),
    Student("Ваня", 22, 78),
    Student("Соня", 19, 92),
    Student("Саша", 20, 88)
]

avg = average_grade(students)


print(f"Средняя оценка студентов: {avg}")



# 4

class Product:
    __slots__ = ('name', 'price', 'quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def filter_products_by_price(products, threshold):
    return [product.name for product in products.values() if product.price > threshold]


products = {
    "Яблоки": Product("Яблоки", 80, 50),
    "Молоко": Product("Молоко", 120, 30),
    "Шоколад": Product("Шоколад", 150, 100),
    "Кофе": Product("Кофе", 300, 20),
    "Чай": Product("Чай", 200, 40)
}


print("Товары дороже 100 руб:", filter_products_by_price(products, 100))
print("Товары дороже 200 руб:", filter_products_by_price(products, 200))
print("Товары дороже 500 руб:", filter_products_by_price(products, 500))