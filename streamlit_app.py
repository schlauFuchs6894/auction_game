import streamlit as st
import random

st.title("🎨 Auction Guess Game")

# --- Liste der Kunstwerke mit Bild-URLs und Preisen ---
kunstwerke = [
    {"name": "Mona Lisa", "price": 780000000, "img": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg"},
    {"name": "Starry Night", "price": 100000000, "img": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"},
    {"name": "The Scream", "price": 120000000, "img": "https://upload.wikimedia.org/wikipedia/commons/f/f4/The_Scream.jpg"},
    {"name": "Girl with a Pearl Earring", "price": 74000000, "img": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Meisje_met_de_parel.jpg"},
    {"name": "Guernica", "price": 200000000, "img": "https://upload.wikimedia.org/wikipedia/en/7/74/PicassoGuernica.jpg"},
    {"name": "The Persistence of Memory", "price": 55000000, "img": "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg"},
    {"name": "American Gothic", "price": 6000000, "img": "https://upload.wikimedia.org/wikipedia/commons/7/76/Grant_Wood_-_American_Gothic_-_Google_Art_Project.jpg"},
    {"name": "The Night Watch", "price": 500000000, "img": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Rembrandt_Harmensz._van_Rijn_-_De_Nachtwacht.jpg"},
    {"name": "Water Lilies", "price": 80000000, "img": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg"},
    {"name": "The Kiss", "price": 90000000, "img": "https://upload.wikimedia.org/wikipedia/commons/7/73/Gustav_Klimt_016.jpg"},
    {"name": "The Birth of Venus", "price": 200000000, "img": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg"},
    {"name": "Las Meninas", "price": 150000000, "img": "https://upload.wikimedia.org/wikipedia/commons/4/41/Las_Meninas_01.jpg"},
    {"name": "The Garden of Earthly Delights", "price": 100000000, "img": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Hieronymus_Bosch_050.jpg"},
    {"name": "The Last Supper", "price": 450000000, "img": "https://upload.wikimedia.org/wikipedia/commons/4/4b/%C3%9Altima_Cena_-_Da_Vinci_5.jpg"},
    {"name": "Liberty Leading the People", "price": 85000000, "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Eug%C3%A8ne_Delacroix_-_La_libert%C3%A9_guidant_le_peuple.jpg"},
    {"name": "The Great Wave off Kanagawa", "price": 30000000, "img": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Great_Wave_off_Kanagawa2.jpg"},
    {"name": "Impression, Sunrise", "price": 70000000, "img": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Monet%2C_Impression%2C_soleil_levant.jpg"},
    {"name": "Whistler's Mother", "price": 12000000, "img": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Whistlers_Mother_high_res.jpg"},
    {"name": "Nighthawks", "price": 60000000, "img": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Nighthawks_by_Edward_Hopper_1942.jpg"},
    {"name": "The Hay Wain", "price": 40000000, "img": "https://upload.wikimedia.org/wikipedia/commons/5/5d/John_Constable_-_The_Hay_Wain.jpg"}
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
    st.image(item["img"], use_column_width=True)
    
    # Preis raten
    user_guess = st.number_input(
        "Schätze den Preis in $",
        min_value=0,
        step=1000
    )
    
    if st.button("🔨"):
        true_price = item["price"]
        if user_guess == true_price:
            points = 10000
            st.balloons()
            st.success(f"Perfekt! Du hast genau richtig geraten und {points} Punkte erhalten!")
        else:
            diff = abs(user_guess - true_price)
            points = max(0, int(1000 - diff / 100000))  # Skaliert Punkte
            st.info(f"Echter Preis: ${true_price:,}")
            st.write(f"Du erhältst {points} Punkte für diese Runde")
        
        st.session_state.score += points
        st.session_state.round += 1
        st.experimental_rerun()
