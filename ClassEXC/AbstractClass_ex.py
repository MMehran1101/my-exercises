import time
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def die(self):
        pass


class Amphibian(Animal):
    def speak(self):
        print("Hey i'm Amphibian!! 🐟")

    def eat(self):
        print("Amphibian is Eating...")

    def die(self):
        print("Amphibian DIE !! RIP 🪦")


amp = Amphibian()
amp.speak()
time.sleep(2)
amp.eat()
time.sleep(3)
amp.die()
