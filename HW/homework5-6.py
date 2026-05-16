class Item:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(item.name, "is added to inventory")

    def show_inventory(self):
        print("Character`s inventory:")

        if len(self.inventory) == 0:
            print("Inventory`s empty!")

        for item in self.inventory:
            print("-", item.name)

    def show_stats(self):
        print("Name:", self.name)
        print("HP:", self.health)
        print("Damage:", self.damage)

    def attack(self):
        print(self.name, "attacks", enemy.name)

        enemy.health -= self.damage

        print(enemy.name, "is damaged")
        print("Enemy`s HP:", enemy.health)

class Enemy:
    def __init__(self, name, health, damage):
            self.name = name
            self.health = health
            self.damage = damage

    def show_stats(self):
        print("Name:", self.name)
        print("HP:", self.health)
        print("Damage:", self.damage)

    def attack(self):
        print(self.name, "attacks", player.name)

        player.health -= self.damage

        print(player.name, "is damaged")
        print("Player`s HP:", player.health)

player = Player("Larry", 100, 15)
enemy = Enemy("Zombie", 80, 10)
item1 = Item("Magic book")
item2 = Item("Golden apple")

player.add_item(item1)
player.add_item(item2)

enemy.show_stats()
player.show_stats()

player.show_inventory()

while player.health > 0 and enemy.health > 0:
    player.attack()

    if enemy.health <= 0:
        print(enemy.name, "lost!")
        break

    enemy.attack()
    if player.health <= 0:
        print(player.name, "lost!")
        break
        