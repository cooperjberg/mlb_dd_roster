import pandas as pd

def get_showzone_player_data():
    try:
        print("🔍 Trying to load ShowZone data from: data/sample_showzone_data.csv")
        df = pd.read_csv("data/sample_showzone_data.csv")
        print("✅ Loaded ShowZone CSV with columns:", df.columns.tolist())
        return df
    except Exception as e:
        print("❌ Error loading ShowZone CSV:", e)
        return pd.DataFrame()
