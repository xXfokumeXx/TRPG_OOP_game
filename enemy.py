import random
from character import *

class Enemy(Character):
  def zautoc(self, other):
    print(f"{self.name} the {(type(self).__name__)}: UAAAAGGGGHHHH!!")
    if random.randint(0,100) < other.defense:
      print(f"{other.name} vyblokoval útok!" )
      return
    else:
      other.hp = other.hp - (self.attack - (self.attack*(other.defense/100)))

  def heal(self):
    print(f"{self.name} the {(type(self).__name__)}: zdlábnul kosti po poražených nepřátelých")

o_enemy1 = Enemy("Hulk", 300, 0, 40, 20)