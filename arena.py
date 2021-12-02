from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        ''' Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = Team('Team 1')
        self.team_two = Team('Team 2')

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = int(input("What is the max damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon name?  ")
        max_damage = int(input("What is the max damage of the weapon?  "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name?  ")
        max_block = int(input("What is the max block of the armor?  "))

        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
            return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(
            input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    # HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add the created hero to team two.
        numOfTeamMembers = int(
            input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)

    def calc_stats(self, team):
        print(f"Stats for {team.name}:")
        kills = 0
        deaths = 0
        alive_heroes = 0
        for hero in team.heroes:
            kills += hero.kills
            deaths += hero.deaths
            if hero.deaths == 0:
                print("survived from " + team.name + ": " + hero.name)
                alive_heroes += 1
        if deaths == 0:
            deaths = 1
        print(team.name + " average K/D was: " + str(kills/deaths))
        return alive_heroes

    def show_stats(self):
        print("")
        stats_team_one  = self.calc_stats(self.team_one)
        print("")
        stats_team_two  = self.calc_stats(self.team_two)
        print("")
        if stats_team_one > stats_team_two:
            print(f"{self.team_one.name} defeated {self.team_two.name}")
        else:
            print(f"{self.team_two.name} defeated {self.team_one.name}")

if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

#Build Teams
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

