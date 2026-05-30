class BankAccount:
    def __init__(self, money):
        self.money = money

    def withdraw(self, amount):

        if amount == 0:
            print("Error")
            return

        if amount > self.money:
            ask = int(input("Take credit? y/n: "))

            if ask == "y":
                credit = amount - self.money
                self.money += credit
                print("Credit:", credit)

            else:
                print("Not enough money")
                return

        self.money -= amount

        print("Taken:", amount)
        print("Left:", self.money)

    def add_money(self, amount):

        if amount < 0:
            print("Error")
            return

        self.money += amount

        print("Added:", amount)
        print("Now:", self.money)


account = BankAccount(100)

try:
    choice = input("1 - take money, 2 - add money: ")

    if choice == "1":
        take = int(input("How much?: "))
        account.withdraw(take)

    if choice == "2":
        add = int(input("How much?: "))
        account.add_money(add)

except ValueError as e:
    print("Error:", e)