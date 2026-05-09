import streamlit as st

st.set_page_config(page_title="Mother's Day 💖")

st.title("🌸 Happy Mother's Day 🌸")



name = "My Lovely Mom ❤️"

st.write("Thank you Mom for your endless love and support 💕")

message = st.selectbox(
    "Choose a Message",
    [
        "You are my first friend and forever hero 💖",
        "Thank you for always being there for me 🌸",
        "I love you Mom ❤️",
        "You make my world beautiful 🌷"
    ]
)

if st.button("Send Wish 💌"):
    st.success(f"{name}, {message}")