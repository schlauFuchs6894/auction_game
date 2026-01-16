import streamlit as st
import random

st.title("🎨 Auction Guess Game")

# --- Kunstwerke mit Name, Künstler, Preis und Bild-URL ---
# Beispiel für funktionierende Platzhalterbilder
TOTAL_ROUNDS = 10

# mindestens 10 Kunstwerke in der Liste
kunstwerke = [
    {"name": "Mona Lisa", "artist": "Leonardo da Vinci", "price": 780000000, "img": "https://picsum.photos/id/1011/600/400"},
    {"name": "Starry Night", "artist": "Vincent van Gogh", "price": 100000000, "img": "https://picsum.photos/id/1012/600/400"},
    {"name": "The Scream", "artist": "Edvard Munch", "price": 120000000, "img": "https://picsum.photos/id/1013/600/400"},
    {"name": "Girl with a Pearl Earring", "artist": "Johannes Vermeer", "price": 74000000, "img": "https://picsum.photos/id/1014/600/400"},
    {"name": "Guernica", "artist": "Pablo Picasso", "price": 200000000, "img": "https://picsum.photos/id/1015/600/400"},
    {"name": "The Persistence of Memory", "artist": "Salvador Dalí", "price": 55000000, "img": "https://picsum.photos/id/1016/600/400"},
    {"name": "American Gothic", "artist": "Grant Wood", "price": 6000000, "img": "https://picsum.photos/id/1017/600/400"},
    {"name": "The Night Watch", "artist": "Rembrandt", "price": 500000000, "img": "https://picsum.photos/id/1018/600/400"},
    {"name": "Water Lilies", "artist": "Claude Monet", "price": 80000000, "img": "https://picsum.photos/id/1019/600/400"},
    {"name": "The Kiss", "artist": "Gustav Klimt", "price": 90000000, "img": "https://picsum.photos/id/1020/600/400"},
]


TOTAL_ROUNDS = 10

# --- Session State initialisieren ---
if "round" not in st.session_state:
    st.session_state.round = 0
    st.session_state.score = 0
    st.session_state.shown_items = random.sample(kunstwerke, TOTAL_ROUNDS)

# --- Spiel vorbei? ---
if st.session_state.round >= TOTAL_ROUNDS:
    st.success(f"🏆 Spiel vorbei! Dein Endscore: {st.session_state.score} Punkte")
    st.write("Danke fürs Spielen!")
else:
    # Aktuelles Kunstwerk
    item = st.session_state.shown_items[st.session_state.round]
    st.write(f"Runde {st.session_state.round + 1} von {TOTAL_ROUNDS}")
    
    # Bild anzeigen
    st.image(item["img"], use_column_width=True)
    
    # Name und Künstler
    st.markdown(f"**Titel:** {item['name']}")
    st.markdown(f"**Künstler:** {item['artist']}")
    
    # Preis raten
    user_guess = st.number_input(
        "Schätze den Preis in $",
        min_value=0,
        step=1000
    )
    
    # 🔨 Button
    if st.button("🔨"):
        true_price = item["price"]
        if user_guess == true_price:
            points = 10000
            st.balloons()
            st.success(f"Perfekt! Du hast genau richtig geraten und {points} Punkte erhalten!")
        else:
            diff = abs(user_guess - true_price)
            points = max(0, int(1000 - diff / 100000))  # Punkte skaliert
            st.info(f"Echter Preis: ${true_price:,}")
            st.write(f"Du erhältst {points} Punkte für diese Runde")
        
        # Punkte speichern & nächste Runde
        st.session_state.score += points
        st.session_state.round += 1
        st.experimental_rerun()
