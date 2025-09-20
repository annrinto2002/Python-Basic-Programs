class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof woof"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow meow"
    
class Cow(Animal):
    def make_sound(self):
        return "Moo moo"
    
animals=[Dog(),Cat(),Cow()]

for animal in animals:
    print(animal.make_sound())
        
    