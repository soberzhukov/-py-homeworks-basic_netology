class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eating(self, food):
        self.weight += 0.8 * food


class Bird(Animal):
    def __init__(self, name, weight, egg):
        super().__init__(name, weight)
        self.egg = egg

    def collect_eggs(self):
        self.egg = 0


class Mammalia(Animal):
    def __init__(self, name, weight, milk):
        super().__init__(name, weight)
        self.milk = milk

    def to_milk(self):
        if self.milk == 0:
            return
        self.weight -= 1
        self.milk -= 1


class Goose(Bird):
    def __init__(self, name, weight, egg):
        super().__init__(name, weight, egg)
        self.sound = 'ga ga'


class Cow(Mammalia):
    def __init__(self, name, weight, milk):
        super().__init__(name, weight, milk)
        self.sound = 'mu mu '


class Sheep(Animal):
    def __init__(self, name, weight, wool):
        super().__init__(name, weight)
        self.wool = wool
        self.sound = 'me me'

    def to_cut(self,):
        if self.wool == 0:
            return
        self.wool -= 1
        self.weight -= 0.6


class Chicken(Bird):
    def __init__(self, name, weight, egg):
        super().__init__(name, weight, egg)
        self.sound = 'kr kr'


class Goat(Mammalia):
    def __init__(self, name, weight, milk):
        super().__init__(name, weight, milk)
        self.sound = 'mu mu '
        self.sound = 'be be'


class Duck(Bird):
    def __init__(self, name, weight, egg):
        super().__init__(name, weight, egg)
        self.sound = 'kry kry'


grey_goose = Goose('grey', 14, 3)
white_goose = Goose('white', 13, 5)
manya_cow = Cow('manya', 112, 10)
barashek_sheep = Sheep('barashek', 45, 9)
kudryvii_sheep = Sheep('kudryvii', 52, 12)
koko_chicken = Chicken('koko', 13, 3)
kukareku_chicken = Chicken('kukareku', 15, 0)
roga_goat = Goat('roga', 32, 6)
kopita_goat = Goat('kopita', 27, 4)
krykva_duck = Duck('krykva', 15, 4)

all_animals_list = [
    grey_goose,
    white_goose,
    manya_cow,
    barashek_sheep,
    kudryvii_sheep,
    koko_chicken,
    kukareku_chicken,
    roga_goat,
    kopita_goat,
    krykva_duck
]


def favorite_weight_print_name(animals_list):
    favorite_weight = 0
    favorite = ''
    for animal in animals_list:
        if animal.weight > favorite_weight:
            favorite_weight = animal.weight
            favorite = animal.name
    print(favorite)


def total_weight(animal_list):
    count = 0
    for animal in animal_list:
        count += animal.weight
    print(count)


def eating_animals(animal_list):
    for animal in animal_list:
        print(animal.weight)
        animal.eating(1)
        print(animal.weight)

total_weight(all_animals_list)
favorite_weight_print_name(all_animals_list)
eating_animals(all_animals_list)
