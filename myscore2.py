import altair as alt
import pandas as pd
import streamlit as st
from streamlit_extras.altex import _chart
from datetime import datetime
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import requests
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
df=pd.read_csv("myscores2.csv")

df.Date = df.Date.astype("string")
st.image(image, caption='#v_board_adddict'
)


st.header("Leaderboard @ Crossfit Kallithea Strongman_WithBillLittleFree")

# st.sidebar.header("Your scores")
# options_form=st.sidebar.form("options_form")
# user_name = options_form.text_input("Name")
# user_age = options_form.text_input("Age")
# user_date = options_form.date_input("Date")
# user_deadlift = options_form.text_input("DL (kg)")
# user_snatch = options_form.text_input("Snatch (kg)")
# user_front = options_form.text_input("Front Squat (kg)")
# user_back = options_form.text_input("Back Squat (kg)")
# user_clean = options_form.text_input("Clean (Kg)")
# user_bps = options_form.text_input("Burpees/min")
# user_run = options_form.text_input("400m (sec)")

# add_data = options_form.form_submit_button()
# if add_data:
    # new_data = {"Athlete":user_name, "Age":int(user_age),"Date":user_date
    # ,"DL (kg)":float(user_deadlift),"Snatch (Kg)":float(user_snatch),"Front Squat (kg)":float(user_front),"Back Squat (kg)":float(user_back),"Clean (Kg)":float(user_clean),"Burpees/min":float(user_bps),"400m (sec)":float(user_run)}
    # df=df.append(new_data, ignore_index=True)
    
    
with st.form("data_editor_form"):
    st.caption("Edit the dataframe below and click the submit button")
    edited = st.experimental_data_editor(df, use_container_width=True, num_rows="dynamic")
            

    #df.style.highlight_max(color = 'lightgreen', axis = 0)    
    submit_button = st.form_submit_button("Submit")
    # edited_df = st.experimental_data_editor(
        # df,
        # use_container_width=True,
        # num_rows="dynamic",
    #df = df.append(df, ignore_index=True)
    # st.write(df)
    edited.to_csv("myscores.csv", index=False)
    st.caption("Modify cells above 👆 or even ➕ add rows, reload to check 👇")
    
#edited.style.highlight_max(color = 'green', axis = 0) 
st_lottie(lottie_coding, height=300, key="coding")

reload = st.button('Reload page')
if reload:
    st.experimental_rerun()
#st.subheader("#v_board_adddict")




# @st.cache_df
# def get_Age_hist(df: pd.df) -> alt.Chart:
    # return _chart(
        # mark_function="bar",
        # data=pd.cut(
            # df.Age, (0, 18, 30, 45, 60, 100), labels=["0 - 18", "19 - 30", "31 - 45","46 - 60", "61 - 100"]
        # )
        # .value_counts()
        # .sort_index()
        # .reset_index(),
        # x=alt.X("index:N", title="Age", sort="x"),
        # y=alt.Y("age:Q", title="Count"),
    # )


# left.altair_chart(get_Age_hist(df), use_container_width=True)
# # middle.altair_chart(get_(edited), use_container_width=True)
# # right.altair_chart(get_active_hist(edited), use_container_width=True)