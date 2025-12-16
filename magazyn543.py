import streamlit as st

# --- Ustawienia Strony ---
st.set_page_config(layout="wide")

# Inicjalizacja listy produktów w sesji Streamlit
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

def dodaj_produkt(nazwa_produktu):
    """Dodaje produkt do magazynu, jeśli nie jest pusty i czyści pole input."""
    if nazwa_produktu.strip():
        if nazwa_produktu not in st.session_state.magazyn:
            st.session_state.magazyn.append(nazwa_produktu)
            st.success(f"Dodano produkt: **{nazwa_produktu}**")
            # Wyczyść pole tekstowe po dodaniu
            st.session_state.input_dodaj = ""
        else:
            st.warning(f"Produkt '{nazwa_produktu}' jest już w magazynie.")
    else:
        st.error("Nazwa produktu nie może być pusta.")

def usun_produkt(nazwa_produktu):
    """Usuwa produkt z magazynu."""
    try:
        st.session_state.magazyn.remove(nazwa_produktu)
        st.info(f"Usunięto produkt: **{nazwa_produktu}**")
    except ValueError:
        st.error(f"Błąd: Produkt '{nazwa_produktu}' nie znaleziono w magazynie.")

# --- Interfejs użytkownika Streamlit ---

st.title("📦 Grinchowy Magazyn Z Nutką Śmiechu!")
st.markdown("Dodawanie i usuwanie produktów (bez ilości i cen). Stan jest utrzymywany tylko podczas trwania sesji.")

# Utworzenie dwóch kolumn: lewa na aplikację (3 części), prawa na obrazek (1 część)
col_app, col_grinch = st.columns([3, 1]) 

with col_app:
    
    ## 📝 Sekcja Dodawania Produktu
    st.header("1. Dodaj Produkt")
    
    # Upewnienie się, że klucz do pola tekstowego istnieje
    if 'input_dodaj' not in st.session_state:
        st.session_state.input_dodaj = ""
        
    nowy_produkt = st.text_input("Wprowadź nazwę produktu do dodania:", key="input_dodaj")

    if st.button("Dodaj do Magazynu"):
        dodaj_produkt(nowy_produkt)

    st.markdown("---")

    ## 🗑️ Sekcja Usuwania Produktu
    st.header("2. Usuń Produkt")

    if st.session_state.magazyn:
        produkt_do_usunięcia = st.selectbox(
            "Wybierz produkt do usunięcia:",
            options=st.session_state.magazyn,
            key="select_usun"
        )
        
        if st.button("Usuń z Magazynu"):
            usun_produkt(produkt_do_usunięcia)
    else:
        st.info("Magazyn jest pusty, nie ma nic do usunięcia.")

    st.markdown("---")

    ## 📋 Stan Magazynu
    st.header("3. Aktualny Stan Magazynu")

    if st.session_state.magazyn:
        st.write(f"**Liczba unikalnych produktów:** {len(st.session_state.magazyn)}")
        
        st.markdown("#### Lista Produktów:")
        st.dataframe(
            {'Nazwa Produktu': st.session_state.magazyn},
            use_container_width=True,
            hide_index=True
        )
    else:
        st.write("Magazyn jest **pusty**.")

with col_grinch:
    st.header(" ") # Pusta nagłówek dla wyrównania
    st.markdown("### Magazynowy Asystent... Grinch!")
    
    # Wstawienie statycznego obrazka Grincha
    GRINCH_STATIC_URL = "https://i.imgur.com/uR2N8mC.png" # Link do obrazka Grincha
    # Jeśli chcesz użyć pliku lokalnego, zmień na: st.image("grinch_static.png")
    st.image(GRINCH_STATIC_URL, caption="Grinch pilnuje!", use_column_width=True)
    
    st.markdown("---")
    st.markdown("### Grinch obserwuje...")
    
    # Wstawienie animowanego GIF-a Grincha
    GRINCH_GIF_URL = "https://media.giphy.com/media/l0HlxT1R8LpL2rRkY/giphy.gif" # Link do GIF-a Grincha
    st.image(GRINCH_GIF_URL, caption="Grinch myśli o świętach (lub o kradzieży zapasów!)", use_column_width=True)
    
    st.markdown("""
        > **Ważna uwaga od Grincha!**
        > Ten magazyn działa tylko na czas trwania Twojej sesji.
        > Po zamknięciu przeglądarki stan się zresetuje!
        > (No chyba, że Grinch coś zwinie wcześniej!)
    """)
