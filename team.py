from hero import Hero
from random import choice

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    
    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(f"{hero.name}")

    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.starting_health = health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero1 = choice(living_heroes)
            hero2 = choice(living_opponents)

            winner = hero1.fight(hero2)

            if winner != "Draw":
                if winner == hero1.name:
                    hero1.kills += 1
                else:
                    hero2.deaths += 1
            