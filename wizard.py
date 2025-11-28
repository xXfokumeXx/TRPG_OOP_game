
import random
from character import *

class Wizard(Character):
  def __init__(self, name, max_hp, max_mana, attack, defense, weapon = None):
    super().__init__(name, max_hp, max_mana, attack, defense, weapon)

  def zautoc(self, other):
    print(f"{self.name} the {(type(self).__name__)}: útočí svým magickým palcem")
    if random.randint(0,100) < other.defense:
      print(f"{other.name} vyblokoval útok!" )
      return
    else:
      other.hp = other.hp - (self.attack - (self.attack*(other.defense/100)))

  def heal(self):
    print(f"{self.name} the {(type(self).__name__)}: casts ULTRA-MEGA-HEAL")
    heal_for = (self.get_hp + random.randint((self.max_hp/6),(self.max_hp/4)))
    print(f"heal za {heal_for}")
