import streamlit as st

# Streamlit App
st.title("Game Recommender System")

# Dropdown for game type selection
game_type = st.selectbox(
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
    if game_type:
        # Display dummy recommendations
        st.write(f"### Recommended Games in {game_type}:")
        recommendations = [
            f"{game_type} Recommendation 1",
            f"{game_type} Recommendation 2",
            f"{game_type} Recommendation 3",
        ]
        for rec in recommendations:
            st.write(f"- {rec}")
    else:
        st.write("Please select a game type before submitting.")
