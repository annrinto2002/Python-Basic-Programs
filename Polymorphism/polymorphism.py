class Animal:
    def sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return"Meow"
    
dog=Dog()
cat=Cat()
animal=Animal()

print(dog.sound())
print(cat.sound())
print(animal.sound())



