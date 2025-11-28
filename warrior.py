import random
from character import *

class Warrior(Character):
  def zautoc(self, other):
    print(f"{self.name} the {(type(self).__name__)}: útočí - For Frodo and for the Aliance!")
    if random.randint(0,100) < other.defense:
      print(f"{other.name} vyblokoval útok!" )
      return
    else:
      other.hp = other.hp - (self.attack - (self.attack*(other.defense/100)))

  def heal(self):
    print(f"{self.name} the {(type(self).__name__)}: cháluje kuře aby se healnul")