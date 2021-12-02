from random import choice
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        ''' Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        global winner
        winner = ""
        if len(opponent.abilities) == 0 and len(self.abilities) == 0:
            print("Draw")
            winner = "Draw"
            return winner
        else:
            while opponent.current_health > 0 and self.current_health > 0:
                first_move = choice([self.name, opponent.name])
                if first_move == self.name:
                    attack = self.attack()
                    opponent.take_damage(attack)
                    if not opponent.is_alive():
                        winner = self.name
                        opponent.deaths -= 1
                        self.deaths -= 1
                        break
                else:
                    attack = opponent.attack()
                    self.take_damage(attack)
                    if not self.is_alive():
                        winner = opponent.name
                        opponent.kills += 1
                        self.deaths -= 1
                        break

        if len(winner) > 0 and winner != "Draw":
            print(f"{winner} won!")
            return winner

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0

        for abilities in self.abilities:
            total_damage += abilities.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_blocked = 0
        if self.current_health != 0 and len(self.armors) != 0:
            for armor in self.armors:
                total_blocked += armor.block()
        return total_blocked

    def take_damage(self, damage):
        defended = damage - self.defend()
        if defended >= 0:
            self.current_health -= defended

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)

    # armor = Armor("sheild", 30)
    # another_armor = Armor("helmet", 10)

    # hero = Hero("Grace Hopper", 100)

    # hero.add_ability(ability)
    # hero.add_ability(another_ability)

    # hero.add_armor(armor)
    # hero.add_armor(another_armor)

    # # print(hero.attack())
    # print(hero.defend())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 100)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 130)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
