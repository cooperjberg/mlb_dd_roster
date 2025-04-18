import pandas as pd

def get_showzone_player_data():
    # Fallback hardcoded data if CSV can't be loaded
    data = [
        {
            "name": "Juan Soto",
            "overall": 84,
            "position": "RF",
            "team": "Yankees",
            "rarity": "Gold",
            "contact_left": 70,
            "contact_right": 78,
            "power_left": 85,
            "power_right": 80,
            "vision": 72,
            "discipline": 90,
            "quicksell": 1000
        },
        {
            "name": "Shohei Ohtani",
            "overall": 95,
            "position": "DH",
            "team": "Dodgers",
            "rarity": "Diamond",
            "contact_left": 88,
            "contact_right": 86,
            "power_left": 99,
            "power_right": 95,
            "vision": 74,
            "discipline": 78,
            "quicksell": 5000
        },
        {
            "name": "Spencer Strider",
            "overall": 87,
            "position": "SP",
            "team": "Braves",
            "rarity": "Diamond",
            "contact_left": None,
            "contact_right": None,
            "power_left": None,
            "power_right": None,
            "vision": None,
            "discipline": None,
            "quicksell": 3000
        }
    ]
    return pd.DataFrame(data)
