import streamlit as st
import random

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
h1 {text-align:center; color:#00ffcc;}
.big {font-size:50px; text-align:center;}
.score {font-size:24px; font-weight:bold; text-align:center;}
button {height:60px; font-size:18px;}
</style>
""", unsafe_allow_html=True)

st.title("🐍 Snake 💧 Water 🔫 Game")
st.write("🏆 Best of 5")

# ---------------- DATA ----------------
choices = {1: "🐍 Snake", -1: "💧 Water", 0: "🔫 Gun"}

# ---------------- SESSION STATE ----------------
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "result_message" not in st.session_state:
    st.session_state.result_message = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# ---------------- GAME LOGIC ----------------
def play(player_choice):
    if st.session_state.game_over:
        return

    computer_choice = random.choice([-1, 0, 1])

    if player_choice == computer_choice:
        result = "🤝 Draw"
    elif (
        (computer_choice == -1 and player_choice == 1) or
        (computer_choice == 1 and player_choice == 0) or
        (computer_choice == 0 and player_choice == -1)
    ):
        st.session_state.player_score += 1
        result = "🎉 You won this round"
    else:
        st.session_state.computer_score += 1
        result = "😢 Computer won this round"

    st.session_state.result_message = (
        f"You chose {choices[player_choice]} | "
        f"Computer chose {choices[computer_choice]}\n{result}"
    )

    if st.session_state.player_score == 5 or st.session_state.computer_score == 5:
        st.session_state.game_over = True

# ---------------- BUTTONS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🐍 Snake"):
        play(1)

with c2:
    if st.button("💧 Water"):
        play(-1)

with c3:
    if st.button("🔫 Gun"):
        play(0)

# ---------------- RESULT ----------------
st.write("---")
if st.session_state.result_message:
    st.subheader("Round Result")
    st.write(st.session_state.result_message)

st.markdown(
    f"<div class='score'>Player: {st.session_state.player_score} | "
    f"Computer: {st.session_state.computer_score}</div>",
    unsafe_allow_html=True
)

# ---------------- FINAL CELEBRATION ----------------
if st.session_state.game_over:
    st.markdown("<div class='big'>🎉🎉 CELEBRATION TIME 🎉🎉</div>", unsafe_allow_html=True)

    if st.session_state.player_score == 5:
        st.success("🏆 YOU WON THE GAME!")
    else:
        st.success("🤖 COMPUTER WON THE GAME!")

    st.markdown("<div class='big'>🥳🎊🎈🎉🥳🎊🎈🎉</div>", unsafe_allow_html=True)
    st.balloons()

# ---------------- RESET ----------------
if st.button("🔄 Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.result_message = ""
    st.session_state.game_over = False
    st.experimental_rerun()
