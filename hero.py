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
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        if len(opponent.abilities) == 0 and len(self.abilities) == 0:
            print("Draw")
        else:
            while opponent.current_health > 0 and self.current_health > 0:
                attack1 = self.attack()
                opponent.take_damage(attack1)

                attack2 = opponent.attack()
                self.take_damage(attack2)

            if not self.is_alive():
                opponent.kills += 1
                self.deaths += 1
                print(f"{opponent.name} won!")
            else:
                self.kills += 1
                opponent.deaths += 1
                print(f"{self.name} won!")

        # if not self.is_alive():
        #     opponent.kills += 1
        #     self.deaths += 1
        #     print(f"{opponent.name} won!")
        #     break

        # while opponent.current_health > 0 and self.current_health > 0:
        #     first_move = choice([self.name, opponent.name])
        #     if first_move == self.name:
        #         attack = self.attack()
        #         opponent.take_damage(attack)
        #         if not opponent.is_alive():
        #         print(f"{self.name} won!")
        # if not opponent.is_alive():
        #     winner = self.name
        #     opponent.deaths -= 1
        #     self.deaths -= 1
        #     break
        # else:
        #     attack = opponent.attack()
        #     self.take_damage(attack)
        # if not self.is_alive():
        #     winner = opponent.name
        #     opponent.kills += 1
        #     self.deaths -= 1
        #     break

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0

        for abilities in self.abilities:
            total_damage += abilities.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    # def defend(self):
    #     total_blocked = 0
    #     if self.current_health != 0 and len(self.armors) != 0:
    #         for armor in self.armors:
    #             total_blocked += armor.block()
    #     return total_blocked
    def defend(self):
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
        return total_armor

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

    # hero = Hero("Wonder Woman")
    # weapon = Weapon("Lasso of Truth", 90)
    # hero.add_weapon(weapon)
    # print(hero.attack())
    hero1 = Hero("Elias")
    ability1 = Ability("speed", 200)
    hero1.add_ability(ability1)
    weapon1 = Weapon("knife", 50)
    hero1.add_weapon(weapon1)
    armor1 = Armor("helmet", 100)
    hero1.add_armor(armor1)

    hero2 = Hero("Dah")
    hero2.add_ability(ability1)
    hero2.add_weapon(weapon1)
    hero2.add_armor(armor1)

    hero1.fight(hero2)
    # hero2.defend()
    # print(hero1.defend())
    # print(len(hero1.abilities))
