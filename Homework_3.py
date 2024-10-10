a = int(input("Введите число от 1 до 100: "))
sum = 0
for i in range(1, a+1):
  sum += i**3
print(sum)

import numpy as np
print("Таблица умножения")
b = []
for i in range(1,10):
  for j in range(1,10):
    if i*j < 10:
      b.append(" "+str(i*j))
    else:
      b.append(str(i*j))
  np.rot90(b)
  print(*b)
  b = []
