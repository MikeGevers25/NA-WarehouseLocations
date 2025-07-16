import streamlit as st
import pandas as pd
import os
import datetime
from utils.barcode_gen import generate_barcode

# Mappen en bestandsnamen
DATA_PATH = 'data/voorraad.csv'
BARCODE_DIR = 'barcodes'
os.makedirs('data', exist_ok=True)
os.makedirs(BARCODE_DIR, exist_ok=True)

# Data laden of initialiseren
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        df = pd.DataFrame(columns=["werkorder", "locatie", "status", "datum"])
        df.to_csv(DATA_PATH, index=False)
        return df

# Data opslaan
def save_data(df):
    df.to_csv(DATA_PATH, index=False)

# Streamlit configuratie
st.set_page_config(page_title="Kisten Voorraad App", layout="wide")
st.title("💼 Kisten Voorraadbeheer - Anilox")

menu = st.sidebar.radio("Navigatie", ["Nieuwe Binnenkomst", "Zoeken & Beheer"])

df = load_data()

if menu == "Nieuwe Binnenkomst":
    st.header("Nieuwe kist registreren")
    werkorder = st.text_input("Werkorder (bijv. W25/012345)")
    locatie = st.text_input("Locatie (bijv. MAG-A2)")

    if st.button("Registreer kist"):
        if werkorder and locatie:
            if werkorder in df['werkorder'].values:
                st.warning("Deze werkorder bestaat al!")
            else:
                barcode_path = generate_barcode(werkorder, BARCODE_DIR)
                datum = datetime.datetime.now().strftime("%Y-%m-%d")
                df = pd.concat([df, pd.DataFrame.from_records([{
                    "werkorder": werkorder,
                    "locatie": locatie,
                    "status": "In magazijn",
                    "datum": datum
                }])])
                save_data(df)
                st.success(f"Kist {werkorder} opgeslagen op locatie {locatie}!")
                st.download_button("Download barcode label", open(barcode_path, "rb"), file_name=f"{werkorder}.pdf")
        else:
            st.warning("Vul zowel werkorder als locatie in.")

elif menu == "Zoeken & Beheer":
    st.header("Zoeken & Locatiebeheer")
    zoekterm = st.text_input("Zoek op werkorder")

    if zoekterm:
        result = df[df["werkorder"].str.contains(zoekterm, case=False)]
        st.dataframe(result)

        if not result.empty:
            selected_row = result.iloc[0]
            new_loc = st.text_input("Nieuwe locatie", value=selected_row["locatie"])
            if st.button("Update locatie"):
                df.loc[df["werkorder"] == selected_row["werkorder"], "locatie"] = new_loc
                save_data(df)
                st.success("Locatie bijgewerkt")

            if st.button("Markeer als verzonden"):
                df.loc[df["werkorder"] == selected_row["werkorder"], "status"] = "Verzonden"
                save_data(df)
                st.success("Kist gemarkeerd als verzonden")

    st.subheader("Voorraadoverzicht")
    st.dataframe(df[df["status"] == "In magazijn"])
