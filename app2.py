import streamlit as st
import pandas as pd
import base64
#import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('Next Best Action Prediction - Invest in the right opportunities')

st.markdown("""
This app performs the results of a classification NBA model, created to help the marketing team to deliver specific campaings on specific audience!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
""")

st.sidebar.header('Filter Panel')

# Web scraping of NFL player stats
# https://www.pro-football-reference.com/years/2019/rushing.hType1Last5_pred
def load_data():
    df = pd.read_csv("exportv1_noCallCenter_noMGMnoParticipation_4activities.csv")
    return df
df=load_data()



# Type1
unique_Type1 = ['CRM','Coupon','Replacement','OnlineOrder','OfflineOrder', 'Service']
selected_Type1 = st.sidebar.multiselect('Last1', unique_Type1, unique_Type1)
# Type2
unique_Type2 = ['CRM','Coupon','Replacement','OnlineOrder','OfflineOrder', 'Service']
selected_Type2 = st.sidebar.multiselect('Last2', unique_Type2, unique_Type2)
# Type3
unique_Type3 = ['CRM','Coupon','Replacement','OnlineOrder','OfflineOrder', 'Service']
selected_Type3 = st.sidebar.multiselect('Last3', unique_Type3, unique_Type3)
# Type4
unique_Type4 = ['CRM','Coupon','Replacement','OnlineOrder','OfflineOrder', 'Service']
selected_Type4 = st.sidebar.multiselect('Last4', unique_Type4, unique_Type4)


# Prediction type5
Type1Last5_pred = sorted(df.Type1Last5_pred.unique())
selected_Type1Last5_pred = st.sidebar.multiselect('Prediction of the upcomming action', Type1Last5_pred, Type1Last5_pred)


# Filtering data
df_selected_Type1Last5_pred = df[(df.Type1Last5_pred.isin(selected_Type1Last5_pred)) & (df.Type1Last1.isin(selected_Type1))& (df.Type1Last2.isin(selected_Type2))& (df.Type1Last3.isin(selected_Type3))& (df.Type1Last4.isin(selected_Type4))]

st.header('Consolidated Table: Users Info')
st.write('Apply the selection options to filter the dataset.')

st.write('Data Dimension: ' + str(df_selected_Type1Last5_pred.shape[0]) + ' rows and ' + str(df_selected_Type1Last5_pred.shape[1]) + ' columns.')
st.dataframe(df_selected_Type1Last5_pred)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_audience.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_Type1Last5_pred), unsafe_allow_html=True)



