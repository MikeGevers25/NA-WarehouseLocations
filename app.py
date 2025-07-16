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
                    "loca
