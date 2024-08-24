import altair as alt
import pandas as pd
import streamlit as st
from datetime import datetime
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_vxnelydc.json")
image = Image.open('bill.jpg')

st.set_page_config(layout="centered", page_title="StrongmanWithBill", page_icon="🦍")
st.title("The proof is in the numbers!")
st.markdown("""gamifying your lifting experience 🏋️ | monitor your results 📈 | focus on podium 🥇""")

# Load CSV file
csv_file = "myscores2.csv"

# Function to load data
def load_data(file):
    return pd.read_csv(file)

# Function to save data
def save_data(data, file):
    data.to_csv(file, index=False)

# Load the data each time the app runs
df = load_data(csv_file)

# Display the image
st.image(image, caption='Coach Bill')

st.header("Leaderboard @ Strongman_WithGreekBill")

# Data editing form
with st.form("data_editor_form"):
    st.caption("Edit the dataframe below and click the submit button")
    
    # Allow the user to edit the DataFrame
    edited_df = st.experimental_data_editor(df, use_container_width=True, num_rows="dynamic")
    
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Save the edited DataFrame back to the CSV file
        save_data(edited_df, csv_file)
        st.success("Changes saved to the CSV file!")

    st.caption("Modify cells above 👆 or even ➕ add rows, reload to check 👇")

# Animation at the bottom of the app
st_lottie(lottie_coding, height=300, key="coding")

# Reload button to refresh the app
reload = st.button('Reload page')
if reload:
    st.experimental_rerun()
