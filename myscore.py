import streamlit as st
import pandas as pd
from datetime import datetime

st.title("This app determines who is the fittest @ Crossfit Kallithea")

st.markdown("""
Full effort is full victory' – Katrin Tanja Davidsdottir
""")

st.title("#onlythebrave")
df=pd.read_csv("myscores.csv")
st.header("Leaderboard")
st.write(df)

st.sidebar.header("Your scores")
options_form=st.sidebar.form("options_form")
user_name = options_form.text_input("Name")
user_age = options_form.text_input("Age")
user_date = options_form.date_input("Date")
user_deadlift = options_form.text_input("DL (kg)")
user_snatch = options_form.text_input("Snatch (kg)")
user_front = options_form.text_input("Front Squat (kg)")
user_back = options_form.text_input("Back Squat (kg)")
user_clean = options_form.text_input("Clean (Kg)")
user_bps = options_form.text_input("Burpees/min")
user_run = options_form.text_input("400m (sec)")

add_data = options_form.form_submit_button()
if add_data:
    new_data = {"Athlete":user_name, "Age":int(user_age),"Date":user_date
    ,"DL (kg)":float(user_deadlift),"Snatch (Kg)":float(user_snatch),"Front Squat (kg)":float(user_front),"Back Squat (kg)":float(user_back),"Clean (Kg)":float(user_clean),"Burpees/min":float(user_bps),"400m (sec)":float(user_run)}
    df=df.append(new_data, ignore_index=True)
    df.to_csv("myscores.csv", index=False)


st.title("#itsanorep")
st.title("#breath")

reload = st.button('Reload page')
if reload:
    st.experimental_rerun()

