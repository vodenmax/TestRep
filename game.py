class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.gold = 0
        self.inventory = []


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0


class Location:
    def __init__(self, name, description, enemies=None, items=None):
        self.name = name
        self.description = description
        self.enemies = enemies or []
        self.items = items or []

    def has_enemies(self):
        return len(self.enemies) > 0

    def has_items(self):
        return len(self.items) > 0


class Game:
    def __init__(self, player):
        self.player = player
        self.locations = []
        self.current_location = None

    def add_location(self, location):
        self.locations.append(location)

    def start(self):
        print("Добро пожаловать в игру")
        self.current_location = self.locations[0]
        self.show_location()

    def show_location(self):
        print(self.current_location.name)
        print(self.current_location.description)

        if self.current_location.has_enemies():
            self.start_battle()

        if self.current_location.has_items():
            self.pickup_item()

        self.choose_action()

    def start_battle(self):
        enemy = self.current_location.enemies[0]
        print(f"Ты встречаешься с  {enemy.name}!")

        while self.player.health > 0 and enemy.is_alive():
            print(f"{self.player.name} здоровье: {self.player.health}")
            print(f"{enemy.name} здоровье: {enemy.health}")

            action = input("Что ты хочешь сделать? (атака, побег) ")

            if action == "атака":
                enemy.health -= 10
                print(f"Ты наносишь 10 урона {enemy.name}!")

                if not enemy.is_alive():
                    self.player.gold += 50
                    print(f"Ты победил {enemy.name}! и заработал {self.player.gold}")

                    self.current_location.enemies.remove(enemy)

            elif action == "побег":
                print("ты сбегаешь")
                break

            else:
                print("Недоступное действие!")

            self.player.health -= enemy.damage

            if self.player.health <= 0:
                print("Ты умер!")
                break

    def pickup_item(self):
        item = self.current_location.items[0]
        print(f"Ты нашел {item}!")
        self.player.inventory.append(item)
        self.current_location.items.remove(item)

    def choose_action(self):
        action = input("Что ты хочешь сделать?(двигаться, инвентарь)")

        if action == "двигаться":
            self.move()

        elif action == "инвентарь":
            self.show_inventory()

        else:
            print("Недоступное действие")
            self.choose_action()

    def move(self):
        locations = [location.name for location in self.locations if location != self.current_location]
        destination = input(f"Куда ты хочешь пойти? {locations} ")

        for location in self.locations:
            if location.name.lower() == destination.lower():
                self.current_location = location
                self.show_location()
                return

        print("Invalid location!")
        self.move()

    def show_inventory(self):
        print("Inventory:")
        for item in self.player.inventory:
            print("- " + item)


forest = Location("Темный лес", "Ты находишься в темном лесу, прислушайся-ты77\ листья звучат зловеще.")
cave = Location("Пещера",
                "Ты оказался в пещере. Здесь сыро и грязно, интересно, это как то связанно с этими скелетами?.")
castle = Location("Замок", "Ты стоишь перед воротами замка, двери тебе не открылись ")

forest.enemies.append(Enemy("Гоблин", 20, 5))
cave.enemies.append(Enemy("Тролль", 30, 10))
castle.enemies.append(Enemy("Дракон", 50, 20))

forest.items.append("Зелье здоровья")
cave.items.append("Зелье маны")
castle.items.append("Меч")
name_player = input('Введите имя игрока')
game = Game(Player(name_player))
game.add_location(forest)
game.add_location(cave)
game.add_location(castle)
game.start()