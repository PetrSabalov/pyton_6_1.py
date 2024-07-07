class Animal:
    def __init__(self, name, alive = True,fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

class Plant:
    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name

class Mammal(Animal):
   def eat(self,food):
       pass


class Predator(Animal):
    def about (self):
        print(self.name)

class Flower(Plant):
    if Plant.edible == true:


class Fruit(Plant):
    def __init__(self, edible = True):
        self.edible = edible

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
