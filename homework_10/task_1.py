class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age)
        self.color = color
        self.breed = breed.capitalize()

    def __str__(self):
        return f'Собака:{self.name} цвет:{self.color} порода:{self.breed}'


class Cat(Animal):
    def __init__(self, name, age, color, breed, life):
        self.color = color
        self.life = life
        self.breed = breed.capitalize()
        super().__init__(name, age)

    def __str__(self):
        return f'Кошка:{self.name} цвет:{self.color} порода:{self.breed} жизни:{self.life}'


class Fish(Animal):
    def __init__(self, name, age, predator):
        self.predator = predator
        super().__init__(name, age)

    def __str__(self):
        if self.predator:
            return f'Рыба:{self.name} хищная:да'
        return f'Рыба:{self.name} хищная:нет'


class Factory:
    animals = {
        'dog': Dog,
        'cat': Cat,
        'fish': Fish
    }

    def clone(self, name, *args, **kwargs):
        return self.animals.get(name)(*args, **kwargs)


if __name__ == '__main__':
    f = Factory()
    one = f.clone('dog', 'туман', 3, 'серый', 'овчарка')
    two = f.clone('cat', 'ночка', 1, 'белый', 'сиамская', 4)
    three = f.clone('fish', 'пиранья', 3, True)
    four = f.clone('dog', 'туман', 3, 'серый', 'дог')
    print(one, two, three, four, sep='\n')

