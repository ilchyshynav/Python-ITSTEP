class Item:
    def __init__(self, name):
        self.name = name

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

        self.inventory = []

    def info(self):
        print("Name:", self.name)
        print("HP:", self.health)
        print("Level:", self.level)

    def rest(self):
        self.health += 10
        print(self.name, "is resting")

    def add_item(self, item):
        self.inventory.append(item)
        print(item.name, "is added to inventory")

    def show_inventory(self):
        print("Character's inventory:")

        if len(self.inventory) == 0:
            print("Inventory is empty!")
        else:
            for item in self.inventory:
                print("-", item.name)

class Warrior(Character):
    def __init__(self, name, level, health, shield):
        super().__init__(name, level, health)
        self.shield = shield

    def attack(self):
        print(self.name, "is attacking with a", weapon1.name)

    def use_shield(self):
        print(self.name, "is using", self.shield)

class Mage(Character):
    def __init__(self, name, level, health, teleport):
        super().__init__(name, level, health)
        self.teleport = teleport

    def attack(self):
        print(self.name, "is attacking with a", weapon2.name)

    def teleport(self):
        print(self.name, "is using", self.teleport)

class Archer(Character):
    def __init__(self, name, level, health, shooting):
        super().__init__(name, level, health)
        self.shooting = shooting

    def attack(self):
        print(self.name, "is attacking with a", weapon3.name)

    def shoot(self):
        print(self.name, "is using", self.shooting)


weapon1 = Weapon("Sword", 85)
weapon2 = Weapon("Wand", 50)
weapon3 = Weapon("Bow", 25)

warrior = Warrior("Ben", 15, 100, 100)
mage = Mage("Peter", 20, 150, 70)
archer = Archer("Eugene", 10, 90, 65)

item1 = Item("Magic book")
item2 = Item("Golden apple")
item3 = Item("Regeneration potion")

archer.add_item(item1)
mage.add_item(item2)
warrior.add_item(item3)

archer.show_inventory()
mage.show_inventory()
warrior.show_inventory()

characters = [warrior, mage, archer]

for character in characters:
    character.info()
    character.attack()
    character.rest()