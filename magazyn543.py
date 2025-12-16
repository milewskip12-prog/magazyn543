import streamlit as st

# Inicjalizacja listy produktów w sesji Streamlit,
# aby stan magazynu był utrzymywany podczas interakcji użytkownika.
if 'magazyn' not in st.session_state:
    st.session_state.magazyn = []

def dodaj_produkt(nazwa_produktu):
    """Dodaje produkt do magazynu, jeśli nie jest pusty."""
    if nazwa_produktu.strip():
        # Dodajemy produkt tylko, jeśli nie jest już w magazynie (opcjonalnie, ale ułatwia)
        if nazwa_produktu not in st.session_state.magazyn:
            st.session_state.magazyn.append(nazwa_produktu)
            st.success(f"Dodano produkt: {nazwa_produktu}")
        else:
            st.warning(f"Produkt '{nazwa_produktu}' jest już w magazynie.")
    else:
        st.error("Nazwa produktu nie może być pusta.")

def usun_produkt(nazwa_produktu):
    """Usuwa produkt z magazynu."""
    try:
        st.session_state.magazyn.remove(nazwa_produktu)
        st.info(f"Usunięto produkt: {nazwa_produktu}")
    except ValueError:
        st.error(f"Błąd: Produkt '{nazwa_produktu}' nie znaleziono w magazynie.")

# --- Interfejs użytkownika Streamlit ---

st.title("📦 Prosta Aplikacja Magazynowa")
st.markdown("Dodawanie i usuwanie produktów (bez ilości i cen). Stan jest utrzymywany tylko podczas trwania sesji.")

## 📝 Sekcja Dodawania Produktu
st.header("1. Dodaj Produkt")
nowy_produkt = st.text_input("Wprowadź nazwę produktu do dodania:", key="input_dodaj")

if st.button("Dodaj do Magazynu"):
    dodaj_produkt(nowy_produkt)
    # Wyczyść pole tekstowe po dodaniu (wymaga ustawienia wartości w text_input, ale
    # na potrzeby prostoty, pole zostanie wyczyszczone automatycznie przy nowej interakcji).

st.markdown("---")

## 🗑️ Sekcja Usuwania Produktu
st.header("2. Usuń Produkt")

if st.session_state.magazyn:
    # Użycie pola wyboru (select box) do usuwania
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
    
    # Wyświetlanie jako lista
    st.markdown("#### Lista Produktów:")
    st.dataframe(
        {'Nazwa Produktu': st.session_state.magazyn},
        use_container_width=True,
        hide_index=True
    )
else:
    st.write("Magazyn jest **pusty**.")
