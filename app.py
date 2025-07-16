# app.py
import streamlit as st
import pandas as pd
import os
import datetime
from utils.barcode_gen import generate_barcode

# Bestandspaden
DATA_PATH = 'data/voorraad.csv'
BARCODE_DIR = 'barcodes'
os.makedirs('data', exist_ok=True)
os.makedirs(BARCODE_DIR, exist_ok=True)

# Laad of initialiseer data
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        df = pd.DataFr
