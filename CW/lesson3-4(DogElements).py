class Dog:
    def __init__(self,items):
        self.items = items

    def __len__(self):
        return len(self.items)

dog1 = Dog( ["Кісточка", "м'яч", "тарілка"])
print(len(dog1))