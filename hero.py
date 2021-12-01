from random import choice


class Hero:
    def __init__(self, name, starting_health=100):
        ''' Instance properties:
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        winner = choice([self.name, opponent.name])
        print(f"{winner} won!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
