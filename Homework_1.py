import math
r = int(input('Введите радиус в сантиметрах: '))
L = round(2*math.pi*r, 2)
S = round(math.pi*r**2, 2)
print('Длина окружности', L)
print ('Площадь круга', S)




x,y=10, 55
x,y=y,x
print("x принадлежит:",x)
print("y принадлежит:",y)





import math
l = int(input('Введите длину в метрах: '))
g = 9.81
T = round(2*math.pi*math.sqrt(l/g),  2)
print('Период колебания маятника', T)
