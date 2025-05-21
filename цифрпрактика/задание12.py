def find_elements_by_index(values, indices):
    result = []
    try:
        for index in indices:
            result.append(values[index])
        return result
    except IndexError as e:
        return f"Ошибка индекса: {e}"
print(find_elements_by_index([ i for i in range(10)], [ i for i in range(10)][::-1] ))


# 2

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * self.radius ** 2

try:
    c=Circle(1)
    print(c.area())
except TypeError:
    print('Радиус должен быть числом')

# 3


class Employee:
    def __init__(self):
        self._employees = []

    def add_employee(self, name, salary):
        self._employees.append({"name": name, "salary": salary})


    def average_salary(self):
        total_salary = sum(emp["salary"] for emp in self._employees)
        return total_salary / len(self._employees) if self._employees else 0

    def get_sorted_employees(self):
        return sorted(self._employees, key=lambda emp: emp["salary"])
try:
    emp=Employee()
    for i in range(10):
        emp.add_employee(f'sotrudnik_{i}', -10000*i )
    print(emp.get_sorted_employees())
    print(emp.average_salary())
except TypeError:
    print('Зарплата должена быть числом')
