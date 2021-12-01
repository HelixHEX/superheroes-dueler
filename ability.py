from random import randint

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage
    
    def attack(self):
        random_value = randint(0, self.max_damage)
        return random_value

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())