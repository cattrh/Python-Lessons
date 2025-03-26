import math
def tg(a,b):
  alfa = b/a
  if a >= 0:
    return math.atan(alfa)
  else:
    return math.atan(alfa* -1)    
x1,x2 = map(float,input("Введите координаты Х через пробел: ").split())
y1,y2 = map(float,input("Введите координаты Y через пробел: ").split())
z1,z2 = map(float,input("Введите координаты Z через пробел: ").split())
print("Минимальный угол: ", min(tg(x1, x2), tg(y1, y2), tg(z1, z2)))


def polind(n):
  for i in range(1,n+1):
    count = 0
    a = bin(i)[2:]
    for j in range(len(a)//2):
      if a[j] == a[j*(-1) - 1]:
        count += 1
    if count == len(a)//2:
      print(i, a)
gran=int(input("Введите границы: "))
