import random
from item import *
from abc import ABC, abstractmethod

class Character(ABC):
  def __init__(self, name, max_hp, max_mana, attack, defense, weapon = None):
    self.name = name
    self.max_hp = max_hp
    self.hp = max_hp
    self.max_mana = max_mana
    self.mana = max_mana
    self.attack = attack 
    self.defense = defense
    self.weapon = weapon

  @classmethod
  def create_new_char(cls, name, max_hp, max_mana, attack, defense, weapon = None):
    return cls(name, max_hp, max_mana, attack, defense, weapon)
  
  @staticmethod
  def generuj_nahodne(horni_mez=6):
    return random.randint(1, horni_mez)

  @abstractmethod
  def zautoc(self):
    print(f"{self.name} útočí")

  @abstractmethod
  def heal(self):
    print(f"{self.name} se healuje")

  def get_effective_attack(self):
    """Vypočítá celkový atack power (atack + weapon + další upscalery damage)"""
    total_attack = self.attack
    if self.weapon is not None:
        # Prida k atributu utoku damage zbrane
        total_attack += self.weapon.damage    
    return total_attack

  #----------------------------------Getter and setter----------------------------------
    # Name
# Name
  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    self._name = new_name

    # Max HP
  @property
  def max_hp(self):
    return self._max_hp

  @max_hp.setter
  def max_hp(self, new_max_hp):
    if new_max_hp > 0:
      self._max_hp = new_max_hp
    else:
      print("Chyba: Max HP musí být kladné. Používám 1.")
      self._max_hp = 1

    # Current HP
  @property
  def hp(self):
      return self._hp

  @hp.setter
  def hp(self, new_hp):
    # Zajištění, že HP zůstane v rozsahu [0, max_hp]
    if new_hp < 0:
        self._hp = 0
    elif new_hp > self.max_hp: # Používáme self.max_hp, které volá jeho getter
        self._hp = self.max_hp
    else:
        self._hp = new_hp

    # Max Mana
  @property
  def max_mana(self):
    return self._max_mana

  @max_mana.setter
  def max_mana(self, new_max_mana):
    if new_max_mana >= 0:
        self._max_mana = new_max_mana
    else:
        print("Chyba: Max Mana nemůže být záporná. Používám 0.")
        self._max_mana = 0

    # Current Mana
  @property
  def mana(self):
    return self._mana

  @mana.setter # POZOR: Přejmenováno z 'set_mana' na 'mana' pro shodu s property
  def mana(self, new_mana):
        # Zajištění, že Mana zůstane v rozsahu [0, max_mana]
        if new_mana < 0:
            self._mana = 0
        elif new_mana > self.max_mana:
            self._mana = self.max_mana
        else:
            self._mana = new_mana

    # Attack
  @property
  def attack(self):
    # POZNÁMKA: V budoucnu zde budete chtít vrátit self.attack + weapon.damage
    return self._attack

  @attack.setter
  def attack(self, new_attack):
    if new_attack >= 0:
        self._attack = new_attack
    else:
        print("Chyba: Attack nemůže být záporný. Používám 0.")
        self._attack = 0

  # Defense
  @property
  def defense(self):
    return self._defense

  @defense.setter
  def defense(self, new_defense):
    if new_defense >= 0:
        self._defense = new_defense
    else:
        print("Chyba: Defense nemůže být záporná. Používám 0.")
        self._defense = 0

  # Weapon
  @property
  def weapon(self):
    return self._weapon

  @weapon.setter
  def weapon(self, new_weapon):
    self._weapon = new_weapon

  def __str__ (self):
    weapon_info = str(self.weapon) if self.weapon else "None"
    return f"""
    {self.name}
    class: {(type(self).__name__)}
    hp: {self.hp}/{self.max_hp}
    mana: {self.mana}/{self.max_mana}
    weapon: {weapon_info}
    base attack: {self.attack}
    effective attack: {self.get_effective_attack()}
    defense: {self.defense}
    """