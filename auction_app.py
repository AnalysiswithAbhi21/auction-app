import streamlit as st

# Initialize session state variables if not present
if 'player_index' not in st.session_state:
    st.session_state.player_index = 0
if 'coins' not in st.session_state:
    st.session_state.coins = {'Team A': 100, 'Team B': 100, 'Team C': 100}
if 'teams' not in st.session_state:
    st.session_state.teams = {'Team A': [], 'Team B': [], 'Team C': []}
if 'current_bid' not in st.session_state:
    st.session_state.current_bid = 0
if 'current_bidder' not in st.session_state:
    st.session_state.current_bidder = None

# Player list
players = [
    "Vaishnav", "Sahil", "Daya", "Zarkar", "Shrnav",
    "Rohit", "Abhi", "Bilat", "Prashant", "Rohan"
]

st.title("🏏 3-Team Player Auction")

# Check if auction is over
if st.session_state.player_index >= len(players):
    st.success("Auction completed! Here's the final team distribution:")
    for team, members in st.session_state.teams.items():
        st.subheader(team)
        st.write(", ".join(members) if members else "No players assigned")
    st.stop()

# Current player being auctioned
current_player = players[st.session_state.player_index]
st.header(f"Auctioning: {current_player}")
st.write(f"Current Bid: {st.session_state.current_bid}")
if st.session_state.current_bidder:
    st.write(f"Current Highest Bidder: {st.session_state.current_bidder}")

# Bidding buttons for each team
cols = st.columns(3)
for i, team in enumerate(['Team A', 'Team B', 'Team C']):
    with cols[i]:
        st.write(f"{team} Coins: {st.session_state.coins[team]}")
        if st.button(f"{team} Bid +5", key=team):
            if st.session_state.coins[team] >= st.session_state.current_bid + 5:
                st.session_state.current_bid += 5
                st.session_state.current_bidder = team

# Finalize bid
if st.button("🏁 Finalize Bid"):
    if st.session_state.current_bidder:
        winner = st.session_state.current_bidder
        cost = st.session_state.current_bid
        st.session_state.teams[winner].append(current_player)
        st.session_state.coins[winner] -= cost
    st.session_state.player_index += 1
    st.session_state.current_bid = 0
    st.session_state.current_bidder = None
    st.experimental_rerun()

# Team Display
st.divider()
st.subheader("Team Lineups So Far")
for team, members in st.session_state.teams.items():
    st.markdown(f"**{team}**: {', '.join(members) if members else 'No players yet'}")
