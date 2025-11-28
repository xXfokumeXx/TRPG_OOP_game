ITEM_COMPONENTS = {
    "Type": [ # Item Type (for game logic and name)
        "Helm", "Weapon", "Body Armor"
    ],
    "Rarity": {
        "Common": 1.0,
        "Uncommon": 1.15,
        "Rare": 1.3,
        "Epic": 1.5,
        "Legendary": 2.0
    },
    "Condition": {
        "Broken": -3,
        "Worn": -1,
        "Fair": 0,
        "Good": 1,
        "Pristine": 3,
        "Perfect": 5
    },
    "Material": [
        "Wood", "Iron", "Steel", "Mithril", "Adamantine"
    ],
    "Adjective": [ # Added a list of descriptive adjectives
        "Furious", "Blazing", "Shadow", "Holy", "Vicious", "Silent", "Ancestral"
    ],
    "RARITY_DROPCHANCE": {
        "Legendary": 1,
        "Epic": 10,
        "Rare": 100,
        "Uncommon": 1000,
        "Common": 10000 
    },

    "WEAPON_CATEGORY": {
        "Axe": (15, 25), 
        "Mace": (14, 24),
        "Sword": (12, 22),
        "Spear": (10, 18),
        "Bow": (8, 14), 
        "Blade": (8, 12),
        "Knife": (4, 8),
        "Staff": (7, 13), 
        "Orb": (5, 10)
    }
}
