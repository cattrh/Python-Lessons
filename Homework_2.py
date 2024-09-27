x, y = input("Введите числа через пробел:").split()
if x.isdigit() and y.isdigit():
    x, y = map(int, (x, y))
    if y != 0:
        print("Результат деления:", x/y)
    else:
        print("Деление на ноль невозможно")
else:
    print("Вводите целые числа")

s = input("Введите стоимость покупок:")
if s.isdigit():
    sum = int(s)
    if sum > 20:
        discount = sum * 0.65
        print(f"{discount} руб. конечная цена, {sum - discount} руб. скидка")
    else:
        print(f"{sum} руб. конечная цена, {0} руб. скидка")
else:
    print("Введите стоимость покупок")