class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the make_sound method on each instance
dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
