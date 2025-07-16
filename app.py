# app.py
import streamlit as st
import pandas as pd
import os
import datetime
from utils.barcode_gen import generate_barcode

# File paths
DATA_PATH = 'data/inventory.csv'
BARCODE_DIR = 'barcodes'
os.makedirs('data', exist_ok=True)
os.makedirs(BARCODE_DIR, exist_ok=True)

# Load or initialize data
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        df = pd.DataFrame(columns=["work_order", "location", "status", "date"])
        df.to_csv(DATA_PATH, index=False)
        return df

# Save
def save_data(df):
    df.to_csv(DATA_PATH, index=False)

# UI
st.set_page_config(page_title="Crate Inventory App", layout="wide")
st.title("💼 Crate Inventory Management - Anilox")

menu = st.sidebar.radio("Navigation", ["New Entry", "Search & Manage"])

df = load_data()

if menu == "New Entry":
    st.header("Register New Crate")
    work_order = st.text_input("Work Order (e.g., W25/012345)")
    location = st.text_input("Location (e.g., MAG-A2)")

    if st.button("Register Crate"):
        if work_order and location:
            barcode_path = generate_barcode(work_order, BARCODE_DIR)
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            df = pd.concat([df, pd.DataFrame.from_records([{
                "work_order": work_order,
                "location": location,
                "status": "In warehouse",
                "date": date
            }])])
            save_data(df)
            st.success(f"Crate {work_order} saved at location {location}!")
            with open(barcode_path, "rb") as f:
                st.download_button("Download Barcode Label (.png)", f, file_name=f"{work_order}.png")
        else:
            st.warning("Please fill in both work order and location.")

elif menu == "Search & Manage":
    st.header("Search & Location Management")
    search_term = st.text_input("Search by Work Order")

    if search_term:
        result = df[df["work_order"].str.contains(search_term, case=False)]
        st.dataframe(result.rename(columns={
            "work_order": "Work Order",
            "location": "Location",
            "status": "Status",
            "date": "Date"
        }))

        if not result.empty:
            selected_row = result.iloc[0]
            new_loc = st.text_input("New Location", value=selected_row["location"])
            if st.button("Update Location"):
                df.loc[df["work_order"] == selected_row["work_order"], "location"] = new_loc
                save_data(df)
                st.success("Location updated")

            if st.button("Mark as Shipped"):
                df.loc[df["work_order"] == selected_row["work_order"], "status"] = "Shipped"
                save_data(df)
                st.success("Crate marked as shipped")

    st.subheader("Inventory Overview")
    st.dataframe(df[df["status"] == "In warehouse"].rename(columns={
        "work_order": "Work Order",
        "location": "Location",
        "status": "Status",
        "date": "Date"
    }))
