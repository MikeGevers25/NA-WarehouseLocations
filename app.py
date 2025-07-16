import streamlit as st

st.title("🎉 Test App voor Streamlit")

st.write("Als je dit ziet, werkt je app!")

if st.button("Klik mij!"):
    st.success("Top! De app werkt helemaal goed.")
