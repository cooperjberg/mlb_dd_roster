import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.data_fetcher import find_player_stats
from utils.showzone_scraper import get_showzone_player_data

st.title("MLB The Show 25 OVR Predictor")

# Player input
player_name = st.text_input("Enter a player name:")

# LIVE MLB STATS
if player_name:
    st.subheader("Live MLB Stats")
    stats = find_player_stats(player_name)

    if stats.empty:
        st.error("Player not found. Try another name.")
    else:
        st.dataframe(stats)

    # SHOWZONE STATS
    st.subheader("ShowZone Live OVR")
    sz_data = get_showzone_player_data()

    if sz_data.empty or "name" not in sz_data.columns:
        st.error("Failed to load ShowZone data. Please try again later.")
    else:
        matching = sz_data[sz_data['name'].str.contains(player_name, case=False)]
        if not matching.empty:
            st.dataframe(matching.head(1))
        else:
            st.warning("Player not found in ShowZone sample data.")
