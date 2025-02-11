import streamlit as st
import requests

st.title("AI Dungeon Master")

# Generate NPC Button
if st.button("Generate NPC"):
    npc = requests.get("http://127.0.0.1:8000/npc/").json()
    st.session_state["npc"] = npc  # Store NPC in session
    st.write(f"**NPC:** {npc['name']} ({npc['race']} {npc['role']})")

# Dialogue Input
if "npc" in st.session_state:
    user_input = st.text_input("Talk to the NPC:")
    if st.button("Send"):
        npc_id = st.session_state["npc"]["id"]
        response = requests.post(f"http://127.0.0.1:8000/dialogue/?npc_id={npc_id}&user_input={user_input}").json()
        st.write(f"NPC: {response['response']}")