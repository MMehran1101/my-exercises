class Animal:
    def __init__(self, name, age, species, sound, zoo_name='Not specified'):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound
        self.zoo = zoo_name

    def __str__(self):
        return f"{self.name}, {self.age}, {self.species}, {self.sound}"

    def info(self):
        return f"{self.name} is {self.age} old.\nit's species is {self.species} and sounds like {self.sound}"

    def make_sound(self):
        return self.sound


class Bird(Animal):
    def __init__(self, name, age, species, sound, wing_span):
        super().__init__(name, age, species, sound)
        self.wing_span = wing_span

    def make_sound(self):
        return self.sound


lion = Animal("Lion", 9, "Mammal", "Roar")
eagle = Bird("eagle", 1, "bird", "Wahoo", 2)
print(eagle.info())
