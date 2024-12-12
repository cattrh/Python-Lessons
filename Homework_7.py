
name= input('Введите имя файла: ')+'.txt'
file = open(name, "w")
s=input('Введите строку (для завершения нажмите ENTER): ')+'\n'
while len(s)>1:
    file.write(s)
    s=input('Введите строку (для завершения нажмите ENTER): ')+'\n'
print('Работа с файлом окончена')


import csv
import datetime
import time
 
file=open('rows_300.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['№', 'Секунда ', 'Микросекунда'])
for i in range(1, 301):
    writer.writerow([i, datetime.datetime.now().second, datetime.datetime.now().microsecond])
    time.sleep(0.01)
        


from random import randint
import os
from PIL import Image, ImageDraw
 
 
def circles_generator(num_of_circles=100):
    if os.path.exists('circles')==False:
        os.mkdir('circles')
    for name in range(1, num_of_circles + 1):
        img = Image.new('RGB', (1200, 1200), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.ellipse((300, 300, 900, 900), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
        img.save('circles/'+str(name)+'.jpg')
 
 
circles_generator()