class Student:
    def __init__(self, name, money, age):
        self.name = name
        self.money = money
        self.age = age

    def work(self):
        self.money = self.money + 100
        print("I earned 100 UAH! My balnce now is:", self.money)

    def rest(self):
        self.money = self.money - 50
        print("Oh, I spend my money... My balace now is:", self.money)

    def live_year(self):
        self.work()
        self.rest()
        self.age = self.age + 1

        print(self.name)
        print("Age:", self.age)
        print("Money:", self.money)

student = Student("James", 100, 20)
student.live_year()

