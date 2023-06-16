class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def apply_damage(self, damage):
        self.health -= damage

    def level_up(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1

    def print_status(self):
        print(f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\nDefence: {self.defense}\n\n")


character1 = Character("Batman", 1, 100, 5, 12)
character2 = Character("Superman", 1, 100, 10, 3)

for i in range(1, 4):
    print(f"Round {i} FIGHT!\n")

    damage = character1.attack - character2.defense
    if damage > 0:
        character2.apply_damage(damage)

    damage = character2.attack - character1.defense
    if damage > 0:
        character1.apply_damage(damage)

    print("Round results:")
    character1.print_status()
    character2.print_status()

print("Fight results:")
if character1.health > character2.health:
    print(f"Winner: {character1.name}")
    print(f"Looser: {character2.name}")
elif character1.health < character2.health:
    print(f"Winner: {character2.name}")
    print(f"Looser: {character1.name}")
else:
    print("Draw")
    