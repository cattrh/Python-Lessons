class Animal:
    def speak(self):
        return "Издает звук"

class MixinSwim:
    def swim(self):
        return "Плавает"

class MixinFly:
    def fly(self):
        return "Летает"

class Duck(Animal, MixinSwim, MixinFly):
    def speak(self):
        return "Кря-кря"

class Penguin(Animal, MixinSwim):
    def speak(self):
        return "Буль-буль"



duck=Duck()
penguin=Penguin()



print(f"Говорит: {duck.speak()}")
print(f"Плавание: {duck.swim()}")  
print(f"Полёт: {duck.fly()}")

print(f"Говорит: {penguin.speak()}")
print(f"Плавание: {penguin.swim()}")  


# 2
class Writer:
    def write(self):
        return "пишет текст"

class Painter:
    def draw(self):
        return "рисует картину"

class CreativePerson(Writer, Painter):
    def write(self):
        return "творчески пишет стихотворение"

    def draw(self):
        return "выразительно рисует пейзаж"


writer = Writer()
painter = Painter()
creative_person = CreativePerson()

persons = [writer, painter, creative_person]


for person in persons:
    if hasattr(person, 'write'):
        print(person.write())
    if hasattr(person, 'draw'):
        print(person.draw())