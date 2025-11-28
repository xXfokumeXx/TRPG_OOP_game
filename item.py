import random
from abc import ABC, abstractmethod
from CONSTANTS import *

class Item(ABC):
    
    def __init__(self, item_type, name=None):
        # 1. nahodný vyběr hodnot
        self.item_type = item_type
        self.rarity = self._select_dropchance(ITEM_COMPONENTS["RARITY_DROPCHANCE"])
        self.condition = random.choice(list(ITEM_COMPONENTS["Condition"].keys()))
        self.material = random.choice(ITEM_COMPONENTS["Material"])
            
        
        # 3. Generace náhodného názvu itemu
        if name is None:
            self.name = self._generate_name()
        else:
            self.name = name

    # abstraktní metoda, kterou musí každá potřída implementovat po svém.
    # abstraktní proto, že item_type weapon přidává nějaké staty, body armor přidává jiné staty a helma také, stejně tak případné další itemy
    @abstractmethod
    def _apply_stats(self):
        pass

    # --- THE FACTORY METHOD ---
    @classmethod
    def generate_random_item(cls):
        # A dictionary mapping item names to their class constructors
        ITEM_TYPES = {
          "Weapon": Weapon,
          "Helm": Helm,
          "BodyArmor": BodyArmor
        }
        # 1. Randomly choose the type
        chosen_type_name = random.choice(list(ITEM_TYPES.keys()))
        chosen_class = ITEM_TYPES[chosen_type_name]
        
        # 2. Call the constructor for the chosen class
        # This returns an instance of Weapon, Helm, or BodyArmor
        new_item = chosen_class() 
        return new_item
    
    # Metoda pro zajištění implementace váhy rarity předmětu viz - RARITY_DROPCHANCE
    def _select_dropchance(self, rarity_dropchance):
        rarity_options = list(rarity_dropchance.keys())
        dropchance = list(rarity_dropchance.values())
        rarity = random.choices(rarity_options, dropchance, k=1)[0]
        return rarity


    def _generate_name(self):
        """Generace nahodneho jmena na základě náhodně vybraných atributů."""
        
        adjective = random.choice(ITEM_COMPONENTS.get("Adjective", []))
        
        name_parts = [
            self.rarity,
            self.condition,
            self.material,
            adjective,
            self.item_type
        ]
        
        return " ".join(name_parts)

        
    def __str__(self):
        return f"""
        --- {self.name} ---
        Type: {self.item_type}
        Rarity: {self.rarity} | Condition: {self.condition} | Material: {self.material}
        """
    

class Weapon(Item):
    # The new Weapon class incorporating logic from the old weapon.py
    
    def __init__(self, name=None):
        self.category = random.choice(list(ITEM_COMPONENTS["WEAPON_CATEGORY"].keys()))
        # 1. Podědí všechny vlastnosti od třídy Item (rarity, condition, material, name)
        super().__init__("Weapon", name) 

        # 2. Generuje základní damage na základě vybrané kategorie zbraně -> viz CONSTANTS.py -> WEAPON_CATEGORY
        self.base_damage = self._generate_base_damage()

        # 3. vypočítá celkové dmg viz funkce _calculate final dmg (zohlednuje kvalitu a raritu zbraně, případně další modifikátory)
        self.damage = self._calculate_final_damage()
        
        # 4. aplikuje změny
        self._apply_stats()

    def _generate_name(self):
        """Generates a random name, using the specific category instead of generic 'Weapon'."""
        
        adjective = random.choice(ITEM_COMPONENTS.get("Adjective", []))
        
        name_parts = [
            self.rarity,
            self.condition,
            self.material,
            adjective,
            self.category # OVERRIDDEN: Uses the specific category (e.g., 'Bow')
        ]
        
        return " ".join(name_parts)


    def _generate_base_damage(self):
        """Generates a random base damage within the range defined for the weapon category."""

        damage_range = ITEM_COMPONENTS["WEAPON_CATEGORY"][self.category]
        return random.randint(damage_range[0], damage_range[1])


    def _calculate_final_damage(self):
        """Calculates total damage by applying the rarity multiplier to the base damage."""
        
        multiplier = ITEM_COMPONENTS["Rarity"].get(self.rarity, 1.0)
        condition_add_dmg = ITEM_COMPONENTS["Condition"].get(self.condition, 1.0)
        
        # Apply rarity multiplier
        final_damage = (self.base_damage * multiplier) + condition_add_dmg
        return round(final_damage)
        
    def _apply_stats(self):
        # Implementation of the abstract method
        self.stats = {"damage": self.damage}

    def __str__(self):
        return f"""
        --- {self.name} ---
        Damage: {self.damage} (Base: {self.base_damage})
        Type: {self.item_type} | Category: {self.category}
        Rarity: {self.rarity} | Condition: {self.condition} | Material: {self.material}
        stats:{self.stats}
        """


class BodyArmor(Item):
    def __init__(self):
        super().__init__("Body Armor")
        self.armor = random.randint(15, 25)
        self._apply_stats()

    def _apply_stats(self):
        # Specific BodyArmor logic goes here
        self.stats = {"Defense": self.armor * 2}

class Helm(Item):
    def __init__(self):
        super().__init__("Helm")
        self.armor = random.randint(5, 10)
        self._apply_stats()

    def _apply_stats(self):
        # Specific Helm logic goes here
        self.stats = {"Defense": self.armor}


class LootSystem:
    def drop_loot(self):
        # This is all LootSystem needs to do!
        new_item = Item.generate_random_item()
        print(f"Loot dropped: {new_item.name} with stats: {new_item.stats}")
        return new_item

# Example run:
loot = LootSystem()
item_drop = loot.drop_loot()