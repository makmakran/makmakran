import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="About me", page_icon=":rocket:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_ps1145pz.json")
lottie_coding2 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_hxart9lz.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Efthymios (Makis) :wave:")
    st.title("A Business Intelligence Analyst/Data Scientist From Athens")
    st.write(
        "A lifelong learner, open-minded, and opinionated professional with a positive attitude. Having 6+ years of experience analyzing business processes, and an expert in developing and managing opportunities for retention and acquisition consumer programs. An effective big data interpreter and user of various visualization techniques to drive growth, serve results, and share insights. Active listening, empathy, and respect are my principles for an efficient collaboration and the core elements for a strong, solid, and powerful team. I am a fitness and wellness fanatic, in love with sports and travelling!"
    )
    st.write("[Learn More >](https://www.linkedin.com/in/efthymios-makrandreou-7a5082168/)")

# ---- work ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Working experience")
        st.subheader("Process Efficiency Reporting & Analytics Specialist")
        st.title("Alpha Bank Greece • July 2022 - present")
        st.write(
        "After almost 5 years in FMCG/Retail industry, I was curious for new ways of workings/ new data/ new industries. Banking is an unlimited source of data and processing and I thought that it was the moment for a new challenge. I joined ALPHA BANK in July of 2022. The Bank was in the staring age of implementation of a Holistic Transformation. Having the experince on this from Papastratos years, I undertook the role of Process Efficiency Reporting & Analytics specialist. I was responsible for the database management and architecture for reporting scope. Process reengineering & automation, Reporting & Data visualization with Qlik Sense was my new accountabilities in the stage of The Bank's successful business transformation."
    )
        st.write("[Alpha Bank](https://www.linkedin.com/company/alpha-bank/)")
        
        
        
        st.subheader("Consumer Data Science Executive")
        st.title("Philip Morris Greece • April 2020 - July 2022")
        st.write(
        "I grabbed the chance to express my willingness to join the Data Science team. To be brief, I was a core member of DS Team from April of 2020 until July 2022. My business understanding and the technical skills that I was continuously developing day by day helped me and my team to find out a better approach on the way of solution and storytelling. R and SQL replaced Excel tool while I was using Power BI in order to visualize my data and serve interactive dashboards and reports. Focused on Acquisition and Retention initiatives, identified data patterns, reporting, dashboards creation-visualization, managed projects end to end, CRM, engaged in ML model development, implementation of Data warehouse and coaching junior and new entry colleagues were some of my role responsibilities. For me, Data Science is about learning to dance in the rain. Data cleary said that our work had a valuable impact in Philip Morris success on Boosting Consumer Satisfaction, secured quality Acquisition, decrease of average churn probability, fligt of SOM and many others KPIs."
    )
        st.subheader("Consumer Journey Analyst")
        st.title("Philip Morris Greece • August 2017 - July 2022")
        st.write(
        "After the completion of my military service year in Cyprus, I made a come back in Papastratos taking the role of Consumer Journey Analyst. It was an easy restart as the content was similar with the previous years. So far so good and I managed to learn more about consumer experience and business. Setting up NPS from scratch was my main responsibility. We created NPS queries on every cosnumer moment around the product (touchpoints). Every business initiative was upon the consumer journey map perspective.After 6 months, I moved upwards as I joined the Consumer Voice team. A very intreresting and challenging role! I was a core member in very crucial projects for the company as the Social Media campaigns for the current period, text analytics project about consumer voice feedback, sentiment analysis and topic clustering. Through the above analysis, data clean up and masking data was one of my accountabilities too. Collaboration with the rest departments and to be aligned about the updated commercialization was my everyday routine. Having the overview on data collection I had to be the owner of the related web platform - the tool that fetched our data. This actually, made me to develop my ability to manage the consulting agencies that we collaborated with. It was a great milestone year for the company vision that drove to ultimate success.My journey in data world started in summer of 2017 when I joined Philip Morris Greece - Papastratos AVES, via an intership program called Inkompass. As a rookie in data, plus not a graduated student yet, I made a deep dive into business logic and understanding of the major KPIs and performance metrics that the saleforce needs to monitor. I was a core member in the reporting team, serving reports and making ad hoc analysis for all the field force of the company. My communication skills started to bloom while I was working by using basic tools as Microsoft Excel and Power Point every day, to provide the management team with reports and feedback emails on a daily/weekly base. I amp pleased to say that I was in the special team for the very first launch of IQOS heat no burn innovation device in Greece."
    )
    
        st.write("[Philip Morris - Papastratos S.A.](https://www.linkedin.com/company/papastratosmazi/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- education ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My education")
        st.subheader("University of Piraeus")
        st.title("Master of Science in Informatics• November 2020 - January 2023")
        st.write(
        "The Master Program in Informatics cures modern technology issues and applications of computer science in other modern sciences. The content and character of the program is configured to respond successfully to the specific scientific needs arising from the rapid development of Information and applications at European and international level. Having already a mathematic way of thinking as a graduated student from a Technical University, the above post graduation program helps me to enhance my professional experience in data in terms of IT academic knowledge."
    )
        st.write("Thesis: Customer Behavior Prediction, based on activities sequence, using Keras and LSTM")
        st.write("##")
        st.subheader("National Technical University of Athens")
        st.title("Diploma in Geomatic Engineering• October 2012 - March 2018")
        st.write(
        "The School’s curriculum is based on the scientific and technical activities of Rural and Surveying Engineers, Greece’s production and development goals. The curriculum aims at providing students with the necessary scientific and technological education that will enable them to perform satisfactorily in a specific area of Rural and Surveying Engineering. In my view, the point of my studies in engineering is not just the skill of making assumptions…it’s the confidence. And that’s the big part,that a lot of people don’t realize that when you’re starting out, what’s more important than the skill is the confidence to just do it, you know, start something."
    )
        st.write("[Thesis](https://dspace.lib.ntua.gr/xmlui/bitstream/handle/123456789/47064/%ce%95%cf%81%ce%b3%ce%b1%cf%83%ce%af%ce%b1.pdf?sequence=1&isAllowed=y)")
    with right_column:
        st_lottie(lottie_coding2, height=300, key="coding2")

