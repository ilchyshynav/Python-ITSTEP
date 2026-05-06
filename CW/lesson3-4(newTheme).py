class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow(self):
        self.age += 1

    def __str__(self):
        return "Собака:" + self.name

dog1 = Dog("Aurora", 5)
dog2 = Dog("Lucas", 2)

dog1.grow()
dog2.grow()

print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
