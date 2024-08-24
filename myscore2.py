import altair as alt
import pandas as pd
import streamlit as st
from datetime import datetime
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="centered", page_title="StrongmanWithBill", page_icon="🦍")

# ---- CACHE FUNCTIONS ----
@st.cache_data  # Cache the CSV loading
def load_data(file):
    return pd.read_csv(file)

@st.cache_resource  # Cache the Lottie animation to avoid repeated downloads
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_vxnelydc.json")
image = Image.open('bill.jpg')

st.title("The proof is in the numbers!")
st.markdown("""gamifying your lifting experience 🏋️ | monitor your results 📈 | focus on podium 🥇""")

# Load CSV file
csv_file = "myscores2.csv"
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
        try:
            edited_df.to_csv(csv_file, index=False)
            st.success("Changes saved to the CSV file!")
            st.experimental_rerun()  # Reload to ensure the saved data is reflected
        except Exception as e:
            st.error(f"Error saving file: {e}")

    st.caption("Modify cells above 👆 or even ➕ add rows, reload to check 👇")

# Animation at the bottom of the app
st_lottie(lottie_coding, height=300, key="coding")

# Reload button to refresh the app
reload = st.button('Reload page')
if reload:
    st.experimental_rerun()  # This forces the app to reload when the button is pressed
