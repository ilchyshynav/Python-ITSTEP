class Code:
    def __init__(self, name):
        self.name = name

class Shop:
    def __init__(self, name):
        self.name = name

class Item(Shop):
    def __init__(self, name, value, rarity):
        super().__init__(name)
        self.value = value
        self.rarity = rarity

    def info(self):
        print("Name:", self.name)
        print("Value:", self.value)
        print("Rarity:", self.rarity)

class Headphones(Item):
    def __init__(self, name, value, rarity):
        super().__init__(name, value, rarity)

class MousePad(Item):
    def __init__(self, name, value, rarity):
        super().__init__(name, value, rarity)

class Stylus(Item):
    def __init__(self, name, value, rarity):
        super().__init__(name, value, rarity)

headphones = Headphones("Airpods", 300, 40)
mouse_pad = MousePad("Mouse pad", 150, 15)
stylus = Stylus("Stylus", 200, 65)

yourCode = Code("12345")

items = [headphones, mouse_pad, stylus]

choice1 = input("Oh no! The IT-STEP Academy store's popularity has dropped significantly! New products have been added to boost it! Would you like to buy something? (y/n):")
if choice1 == "y":
    for item in items:
        print("----------------")
        item.info()
else:
    print("You`re not a hero...")

choice2 = input("Need an advise? (item name):")
if choice2 == "headphones":
    print("Nice choice! They sound really good. They're also made of durable material, so they'll last a long time!")
elif choice2 == "mouse_pad":
    print("Tired of scratches on your desk or mouse? Get our mouse pad! It's soft and flexible, making it comfortable for any task!")
elif choice2 == "stylus":
    print("Still drawing art with your finger? Sounds depressing, right? Get our drawing stylus (+ each stylus comes with three spare tips, but that's a secret...)")
elif choice2 == "":
    print("Still drawing art with your finger? Sounds depressing, right? Get our drawing stylus (+ each stylus comes with three spare tips, but that's a secret...)")
else:
    print("I think you need a glasses store. We don't have this product:/")

choice5 = input("Would you like to add something to your favourites? (item name/n):")
if choice5 == "headphones":
    print("Item HEADPHONES is added to favourites!❤️")
elif choice5 == "mouse_pad":
    print("Item MOUSE_PAD is added to favourites!❤️")
elif choice5 == "stylus":
    print("Item STYLUS is added to favourites!❤️")
elif choice5 == "n":
    print("Fine, as you wish...")

choice3 = input("Anything that catches your eye? (item name/n):")
while choice3 == "n":
    print("It`s fine, you`ve still got time to think!")
    choice3 = input("Anything that catches your eye? (item name/n): ")

if choice3 == "headphones":
    print("Nice! It will cost 300 coins!")
elif choice3 == "mouse_pad":
    print("Nice! It will cost 150 coins!")
elif choice3 == "stylus":
    print("Nice! It will cost 200 coins!")

choice4 = input("Will you buy this product? (y/n)")
if choice4 == "y":
    choice5 = input("Perfect, please write down your card code: ")

    if choice5 == yourCode.name:
        print("You really use that code? So basic... wait- you don`t have any coins. You`re a bad student.")
    else:
        print("The code is not working, why lying?")
else:
    print("Fine, we have enough students who want to be heros...")