a = "орыораыоуггггггннннараранннннарррррарнннннннннннннвыр"
k = 1
c = 0
for i in range(len(a)-1):
  if a[i] == "н" and a[i+1] == "н":
    k += 1
  else:
    k = 1
  if k > c:
    c = k
print(f"Самая длинная последовательность {c} символов") 
print("Замена в строке:", a.replace("н"*c, "!"*c))

a = 'ыовлвы(нннннн)оавлыасф'
print(((a.split( "(" ))[1].split( ")" )) [0])

a = "Аллея анекдот сирень окно адаптациЯ"
ast = a.split(" ")
for i in ast:
  if (i[0] == "а" or i[0] == "А") and (i[-1] == "я" or i[-1] == "Я"):
    if i == ast[-1]:
      print(i, end=".")
    else:
      print(i, end=", ")