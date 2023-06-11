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
    st.title("Hi, I am Makis:wave:")
    st.subheader("An Insight Analyst/Data Scientist From Athens")
    st.write(
        "A lifelong learner, open-minded, and opinionated professional with a positive attitude. Having 6+ years of experience analyzing business processes, and expertise in developing and managing opportunities for retention and acquisition consumer programs. An effective big data interpreter and user of various visualization techniques to drive growth, serve results, and share insights. Worked in FMCG/Retail/Banking/Gambling industries, with proficiency in Customer & Product analytics. Active listening, empathy, and respect are my principles for an efficient collaboration and the core elements for a strong, solid, and powerful team. I am a fitness and wellness fanatic, in love with sports and travelling!"
    )
    st.write("[Learn More](https://www.linkedin.com/in/makis-makrandreou-7a5082168//)")

# ---- work ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Working experience")
        
        st.title("Retail Customer & Product Insights & Analytics Specialist")
        st.subheader("OPAP Greece • April 2023 - present")
        st.write(
        "OPAP is the leading Entertainment Provider/Gambling company in Greece and among the most recognized ones in its sector worldwide. Being a core member to a fresh strategic initiative of such a huge company, meets the points of my personal ambitions list. OPAP aims to conjure a new retail customer and product analytics department to leverage data to gain valuable insights and drive business growth unifing retail & app & market research data. So my role as the 'Retail Customer & Product Analytics Specialist' is to deliver fact-based customer understanding insights that facilitate strategic, tactical and operational decision-making from various internal & external systems and data sources. Develop and apply advanced statistical and machine learning techniques based on digital browsing and gaming data to deliver actionable insights at customer & product level. It is important to thoroughly research and consider your personal ambitions, priorities, and career goals to find a place that aligns with your values. 'Opportunities do not happen, you create them.' [Chris Grosser]")
        st.write("[OPAP](https://www.linkedin.com/company/opap-s.a./)")
        
        st.title("Process Efficiency Reporting & Analytics Specialist")
        st.subheader("Alpha Bank Greece • July 2022 - April 2023")
        st.write(
        "After almost 5 years in FMCG/Retail industry, I was curious for new ways of workings/ new data/ new industries. Banking is an unlimited source of data/procesdures and I thought that it was the right moment for my new challenge. I joined ALPHA BANK in July of 2022. The Bank was in the staring age of implementation of a Holistic Transformation. Having the experince on this from Papastratos years, I undertook the role of Process Efficiency Reporting & Analytics specialist. I was responsible for the database management and architecture for reporting scope. The aim was to unify the employee performance metrics with the operations KPIs, to drive into an effective workforce management. Process reengineering & automation, Reporting & Data visualization with Qlik Sense was my new accountabilities in the stage of The Bank's successful business transformation while I worked as intrapreneur on BI tools (Qlik Sense, PowerBI) within the bank departments. Setting up the 'The Qlik Community of Practice' to create bridges within different departments, to help more employees to get familiar with Qlik and visualization/BI mindset, to serve upadates of the tool and hints to the more mature users, is one of my achievement in my 'bank year'."
    )
        st.write("[Alpha Bank](https://www.linkedin.com/company/alpha-bank/)")
        
        
        
        st.title("Consumer Data Science Executive")
        st.subheader("Philip Morris Greece • April 2020 - July 2022")
        st.write(
        "I grabbed the chance to express my willingness to join the Data Science team. To be brief, I was a core member of DS Team from April of 2020 until July 2022. My business understanding and the technical skills that I was continuously developing day by day helped me and my team to find out a better approach on the way of solution and storytelling. R and SQL replaced Excel tool while I was using Power BI in order to visualize my data and serve interactive dashboards and reports. Focused on Acquisition and Retention initiatives, identified data patterns, reporting, dashboards creation-visualization, managed projects end to end, CRM, engaged in ML model development, implementation of Data warehouse and coaching junior and new entry colleagues were some of my role responsibilities. If you ask me, Data Science is about learning to dance in the rain. Data cleary said that our work had a valuable impact in Philip Morris success on Boosting Consumer Satisfaction, secured quality Acquisition, decrease of average churn probability, fligt of SOM and many others KPIs. Lauching new product in greek market, monitoring the impact, plan the next strategy teach me the 'how' and 'why' around business thinking."
    )
        st.title("Consumer Journey Analyst")
        st.subheader("Philip Morris Greece • August 2017 - July 2022")
        st.write(
        "My journey in data world started in summer of 2017 when I joined Philip Morris Greece - Papastratos AVES, via an intership program called Inkompass. As a rookie in data, plus not a graduated student yet, I made a deep dive into business logic and understanding of the major KPIs and performance metrics that the saleforce needs to monitor. I was a core member in the reporting team, serving reports and making ad hoc analysis for all the field force of the company. My communication skills started to bloom while I was working by using basic tools as Microsoft Excel and Power Point every day, to provide the management team with reports and feedback emails on a daily/weekly base. I am pleased to say that I was in the special team for the very first launch of IQOS heat no burn innovation device in Greece. I feel lucky that my working journey started here. As first accountabilities my to dos were around operations & customer reporting needs of the business stakeholders. After the completion of my military service year in Cyprus, I made a come back in Papastratos taking the role of Consumer Journey Analyst. It was an easy restart as the content was similar with the previous years. So far so good and I managed to learn more about consumer experience and business. Setting up NPS from scratch was my main responsibility. We created NPS queries on every cosnumer moment around the product (touchpoints). Every business initiative was upon the consumer journey map perspective.After 6 months, I moved upwards as I joined the Consumer Voice team. A very intreresting and challenging role! I was a core member in very crucial projects for the company as the Social Media campaigns for the current period, text analytics project about consumer voice feedback, sentiment analysis and topic clustering. Through the above analysis, data clean up and masking data was one of my accountabilities too. Collaboration with the rest departments and to be aligned about the updated commercialization was my everyday routine. Having the overview on data collection I had to be the owner of the related web platform - the tool that fetched our data. This actually, made me to develop my ability to manage the consulting agencies that we collaborated with. It was a great milestone year for the company vision that drove to ultimate success."
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
        st.title("University of Piraeus")
        st.subheader("Master of Science in Informatics• November 2020 - January 2023")
        st.write(
        "The Master Program in Informatics cures modern technology issues and applications of computer science in other modern sciences. The content and character of the program is configured to respond successfully to the specific scientific needs arising from the rapid development of Information and applications at European and international level. Having already a mathematic way of thinking as a graduated student from a Technical University, the above post graduation program helps me to enhance my professional experience in data in terms of IT academic knowledge."
    )
        st.write("[Thesis](https://dione.lib.unipi.gr/xmlui/bitstream/handle/unipi/15143/Makrandreou_20045.pdf?sequence=3&isAllowed=y): Customer Behavior Prediction, based on activities sequence, using Keras and LSTM")
        st.write("##")
        st.title("National Technical University of Athens")
        st.subheader("Diploma in Geomatic Engineering• October 2012 - March 2018")
        st.write(
        "The School’s curriculum is based on the scientific and technical activities of Rural and Surveying Engineers, Greece’s production and development goals. The curriculum aims at providing students with the necessary scientific and technological education that will enable them to perform satisfactorily in a specific area of Rural and Surveying Engineering. In my view, the point of my studies in engineering is not just the skill of making assumptions…it’s the confidence. And that’s the big part,that a lot of people don’t realize that when you’re starting out, what’s more important than the skill is the confidence to just do it, you know, start something."
    )
        st.write("[Thesis](https://dspace.lib.ntua.gr/xmlui/bitstream/handle/123456789/47064/%ce%95%cf%81%ce%b3%ce%b1%cf%83%ce%af%ce%b1.pdf?sequence=1&isAllowed=y): 3D City modelling Athens, using CityGML")

    with right_column:
        st_lottie(lottie_coding2, height=300, key="coding2")

