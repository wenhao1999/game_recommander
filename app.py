import streamlit as st

# Streamlit App
st.title("Game Recommender System")
st.sidebar.title("Input")

# User input for the game name
game_name = st.text_input("Enter a game name:")

# Dropdown for game type selection
game_type = st.sidebar.selectbox(
    "Select Game Type:",
    [
        "Action Games",
        "Shooter Games",
        "Fighting Games",
        "Survival Games",
        "Rhythm Games",
        "Battle Royale Games",
        "Adventure Games",
    ],
)

# Submit button
if st.button("Submit"):
    if game_name:
        # Display dummy recommendations
        st.write(f"### Recommended Games for '{game_name}' in {game_type}:")
        recommendations = [
            f"{game_type} Recommendation 1",
            f"{game_type} Recommendation 2",
            f"{game_type} Recommendation 3",
        ]
        for rec in recommendations:
            st.write(f"- {rec}")
    else:
        st.write("Please enter a game name before submitting.")
