import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from utils.data_fetcher import find_player_stats

st.title("MLB The Show 25 OVR Predictor")

player_name = st.text_input("Enter a player name:")

if player_name:
    st.subheader("Live MLB Stats")
    stats = find_player_stats(player_name)
    if stats.empty:
        st.error("Player not found. Try another name.")
    else:
        st.dataframe(stats)

