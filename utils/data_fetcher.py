from pybaseball import batting_stats, pitching_stats
import pandas as pd
from datetime import datetime

def get_batter_stats(season_year=None):
    if season_year is None:
        season_year = datetime.now().year
    df = batting_stats(season_year)
    df = df[["Name", "Team", "AVG", "OBP", "SLG", "HR", "BB%", "K%"]]
    df.columns = ["name", "team", "avg", "obp", "slg", "hr", "bb_pct", "k_pct"]
    return df

def get_pitcher_stats(season_year=None):
    if season_year is None:
        season_year = datetime.now().year
    df = pitching_stats(season_year)
    df = df[["Name", "Team", "ERA", "SO9", "BB9", "HR9", "H9"]]
    df.columns = ["name", "team", "era", "k_per_9", "bb_per_9", "hr_per_9", "h_per_9"]
    return df

# Optional: Filter by name
def find_player_stats(name, player_type="batter"):
    if player_type == "batter":
        df = get_batter_stats()
    else:
        df = get_pitcher_stats()
    return df[df['name'].str.contains(name, case=False, na=False)]

