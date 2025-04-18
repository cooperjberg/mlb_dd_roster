import pandas as pd

def get_showzone_player_data():
    try:
        df = pd.read_csv("data/sample_showzone_data.csv")
        return df
    except Exception as e:
        print("❌ Error loading ShowZone CSV:", e)
        return pd.DataFrame()
