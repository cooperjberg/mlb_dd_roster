def get_showzone_player_data():
    url = "https://api.showzone.io/api/cards"
    params = {
        "game": "MLB The Show 25",
        "page": 1,
        "limit": 5000
    }

    headers = {
        "accept": "application/json"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "data" not in data:
            print("⚠️ No 'data' key in ShowZone response")
            return pd.DataFrame()

        players = []
        for card in data["data"]:
            players.append({
                "name": card.get("name", "N/A"),
                "overall": card.get("overall_rating", 0),
                "position": card.get("position", ""),
                "team": card.get("team", ""),
                "rarity": card.get("rarity", ""),
                "contact_left": card.get("contact_left", None),
                "contact_right": card.get("contact_right", None),
                "power_left": card.get("power_left", None),
                "power_right": card.get("power_right", None),
                "vision": card.get("vision", None),
                "discipline": card.get("discipline", None),
                "pitching_attributes": card.get("pitching_attributes", {}),
                "quicksell": card.get("quicksell_value", None)
            })

        df = pd.DataFrame(players)
        print(f"✅ Loaded {len(df)} players from ShowZone")
        return df

    except Exception as e:
        print(f"ShowZone scrape error: {e}")
        return pd.DataFrame()
