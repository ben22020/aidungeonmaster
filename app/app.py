import streamlit as st
import requests

st.title("AI Dungeon Master")


theme = st.text_input("Enter a theme (e.g., Fantasy, Sci-Fi, Post-Apocalyptic):", "Sci-Fi")
character_name = st.text_input("Enter your character's name:", "Skromdar")
character_description = st.text_area("Describe your character:", "A Space Paladin with a mysterious past.")


# Button to generate world history
if st.button("Start New Adventure"):
    with st.spinner("Generating world history..."):  # Show loading spinner
        response = requests.get(
            f"http://127.0.0.1:8000/generate_world/",
            params={"theme": theme, "character_name": character_name, "character_description": character_description},
        )

    if response.status_code == 200:
        world_history = response.json()["world_history"]  # Extract history text
        st.subheader("Your World’s History:")
        st.write(world_history)  # Display response
    else:
        st.error(f"Error: Unable to generate world history. {response.status_code}")