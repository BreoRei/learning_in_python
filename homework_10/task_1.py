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
    def __call__(self, type_animal, *args):
        param = args[0]
        if type_animal in "Cat":
            return Cat(name=param.get('name'),
                       age=param.get('age'),
                       color=param.get('color'),
                       breed=param.get('breed'),
                       life=param.get('life'))
        elif type_animal in "Dog":
            return Dog(name=param.get('name'),
                       age=param.get('age'),
                       color=param.get('color'),
                       breed=param.get('breed'))
        elif type_animal in "Fish":
            return Fish(name=param.get('name'),
                        age=param.get('age'),
                        predator=param.get('predator'))


if __name__ == '__main__':
    factory = Factory()
    one = factory('Dog', {'name': 'туман', 'age': 3, 'color': 'серый', 'breed': 'овчарка'})
    two = factory("Cat", {'name': 'ночка', 'age': 1, 'color': 'белый', 'breed': 'сиамская', 'life': 4})
    three = factory("Fish", {'name': 'пиранья', 'age': 3, 'predator': True})
    four = factory("Dog", {'name': 'туман', 'age': 3, 'color': 'серый', 'breed': 'дог'})
    print(one, two, three, four, sep='\n')

