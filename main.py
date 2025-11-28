from warrior import *
from wizard import *
from enemy import *
from game import *

game = True


# Example Usage: Create 3 dynamically generated weapons
# No base_damage input needed!
w1 = Weapon()
w2 = Weapon()
w3 = Weapon()
"""
o_warrior1 = Warrior("Leonidas", 150, 50, 20, 13)
o_wizard1 = Wizard("Gandalf", 100, 150, 2, 5, w2)
o_enemy1 = Enemy("Hulk", 300, 0, 40, 20, w3)
"""
o_wizard2 = Wizard.create_new_char("Pepa",100, 150, 2, 5, w2)


if __name__ == "__main__":
    o_game = Game.create_game()