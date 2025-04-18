import pandas as pd
import os

def get_showzone_player_data():
    file_path = os.path.join("data", "sample_showzone_data.csv")
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print("⚠️ CSV not found at expected path.")
        return pd.DataFrame()
