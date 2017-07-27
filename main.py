class Animal:
    _class = None  # млекопитающие, пресмыкающиеся и т.д.
    _type = None
    _position = None  # загон, стойло, курятник
    _quantity = 0
    _sound = None  # звук речи

    def __init__(self, animalclass, animaltype, position, quantity, sound):
        self._class = animalclass
        self._type = animaltype
        self._position = position
        self._quantity = quantity
        self._sound = sound

    def speak(self):
        print(self._sound)

    def add(self):
        self._quantity += 1
        print("Теперь животных типа {0} на ферме стало {1}".format(self._type, self._quantity))

    def minus(self):
        self._quantity -= 1
        print("Теперь животных типа {0} на ферме стало {1}".format(self._type, self._quantity))


class Mammal(Animal):
    _class = "mammal"

    def __init__(self, animaltype, position, quantity, sound):
        self._type = animaltype
        self._position = position
        self._quantity = quantity
        self._sound = sound


class Birds(Animal):
    _class = "birds"

    def __init__(self, animaltype, position, quantity, sound):
        self._type = animaltype
        self._position = position
        self._quantity = quantity
        self._sound = sound


class Cow(Mammal):
    _type = "cow"
    _sound = "moo"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


class Goat(Mammal):
    _type = "goat"
    _sound = "bee"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


class Sheep(Mammal):
    _type = "sheep"
    _sound = "mee"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


class Pig(Mammal):
    _type = "pig"
    _sound = "hruhru"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


class Duck(Birds):
    _type = "duck"
    _sound = "qui"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


class Chicken(Birds):
    _type = "chicken"
    _sound = "quoquo"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


class Geese(Birds):
    _type = "geese"
    _sound = "gaga"

    def __init__(self, position, quantity):
        self._position = position
        self._quantity = quantity


if __name__ == '__main__':
    chick = Chicken("hen house", 20)
    chick.add()
    chick.speak()
