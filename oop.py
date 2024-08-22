class Animal():
    _name = "Animal"
    _life = 0
    _sound = ""
    def __init__(self, life, sound):
        self._life = life
        self._sound = sound
    def sound(self):
        print(f"I'm {self._name} with {self._sound} sound.")

my_animal = Animal(life=100, sound="Hello") 
my_animal.sound()

class Dog(Animal):
    def __init__(self, life=15, sound="汪汪"):
        self._name = "Dog"
        self._life = life
        self._sound = sound

class Cat(Animal):
    def __init__(self, life=20, sound="喵喵"):
        self._name = "Cat"
        self._life = life
        self._sound = sound
    # def __init__(self, life, sound):
    #     self.life = life
    #     self.sound = sound
    # def sound(self):
    #     print(self.sound)

my_dog1 = Dog(25, "Super汪汪")
my_dog2 = Dog()
my_cat = Cat(15, "喵喵")
my_dog1.sound()
my_dog2.sound()
my_cat.sound()

    

