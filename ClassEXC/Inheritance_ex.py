
#    *** Inheritance Exercise ***

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def Eat(self):
        print("Eating ...")

    def Sleep(self):
        print("Sleeping ...")


class Dog(Animal):
    def Speak(self):
        print("Iam Doooooooog")


class Crocodilo(Animal):
    pass


dog = Dog("Doggy")
print(dog.Sleep())
dog.Speak()

