import streamlit as st
import time

from core.playlist import get_playlist
from core.platforms import stream_to_all
from config.settings import PLAYLIST, PLATFORMS, CTA_FILE

st.set_page_config(page_title="Live Stream PRO", layout="wide")

st.title("🚀 Live Streaming PRO")

if st.button("▶️ Start Streaming"):
    st.success("Streaming started!")

    playlist = get_playlist(PLAYLIST)

    for item in playlist:
        st.write(f"Now playing: {item['file']}")
        
        stream_to_all(
            item["file"],
            PLATFORMS,
            CTA_FILE
        )

        time.sleep(5)

    st.success("Playlist finished!")

if st.button("⏹️ Stop (Manual)"):
    st.warning("Stop manual (gunakan kill process)")
