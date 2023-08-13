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
        "Hi, I'm Makis. I'm a lifelong learner, open-minded and opinionated, always approaching challenges with a positive attitude. I work as a Data Scientist/Insight Analyst, bringing over 5 years of experience analyzing business data in diverse industries such as FMCG, Retail, Banking, and Gambling. My expertise lies in Customer and Product analytics. I'm enthusiastic about harnessing big data, combining it with my interpretation and visualization skills to drive growth, enhance outcomes, and provide valuable insights. I play a crucial role as a core member in identifying and developing new business opportunities. Active listening, empathy, and respect are my principles for an efficient collaboration and the core elements for a strong, solid, and powerful team. I am a fitness and wellness fanatic, in love with sports and travelling!"
    )
    st.write("[Learn More](https://www.linkedin.com/in/makis-makrandreou-7a5082168//)")

# ---- work ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Working experience")
        
        st.title("Retail Customer & Product Insights & Analytics Specialist")
        st.subheader("OPAP S.A. Greece • April 2023 - present")
        st.write(
        "OPAP is the foremost entertainment provider and gambling company in Greece, and it holds a prominent global position within its industry. Being an integral part of a new strategic initiative for such a substantial company aligns perfectly with the aspirations on my personal list of ambitions. OPAP's objective is to establish a novel retail customer and product analytics department, dedicated to harnessing data for valuable insights and to propel business growth by unifying retail, app, and market research data. In my role as the 'Retail Customer & Product Analytics Specialist,' my responsibility is to deliver insightful customer understanding based on factual data. These insights play a vital role in informing strategic, tactical, and operational decisions by drawing from a variety of internal and external systems and data sources. I am tasked with the development and application of advanced statistical and machine learning techniques, utilizing digital browsing and gaming data, in order to provide actionable insights at both customer and product levels. Undoubtedly, it is crucial to meticulously research and contemplate personal ambitions, priorities, and career objectives to discover a role that harmonizes with one's values. As Chris Grosser aptly stated...Opportunities do not happen, you create them."        
     )
        st.write("[OPAP S.A.](https://www.linkedin.com/company/opap-s.a./)")
        
        st.title("Process Efficiency Reporting & Analytics Specialist")
        st.subheader("Alpha Bank Greece • July 2022 - April 2023")
        st.write("After spending nearly 5 years in the FMCG/Retail industry, I found myself intrigued by new ways of working, fresh data opportunities, and exploring different sectors. The realm of Banking, with its vast reserves of data and intricate processes, beckoned as an exciting avenue for my next endeavor. Thus, in July of 2022, I embarked on a new journey by joining ALPHA BANK. At the time of my arrival, ALPHA BANK was at the threshold of a comprehensive Holistic Transformation. Building upon my experience gained during my years at Papastratos, I assumed the role of a Process Efficiency Reporting & Analytics Specialist. This entailed overseeing the management and architectural aspects of the reporting scope's database. The primary goal was to amalgamate employee performance metrics with operational KPIs, fostering an environment conducive to efficient workforce management. During this phase of the Bank's triumphant business transformation, I undertook responsibilities in process reengineering, automation, reporting, and data visualization. Qlik Sense, a potent tool for data visualization, became my companion in driving these initiatives. Additionally, I embraced the role of an intrapreneur, advocating for and imparting knowledge about Business Intelligence tools (Qlik Sense, PowerBI) across various bank departments. One of my noteworthy accomplishments during my tenure involved establishing 'The Qlik Community of Practice.' This dynamic platform was designed to bridge gaps between different departments, aiding employees in familiarizing themselves with Qlik, cultivating a visualization and BI mindset. Through this platform, updates and insights were shared with more experienced users, contributing to a vibrant knowledge-sharing ecosystem. As I reflect on my 'bank year,' I take pride in these achievements and the role I played in the bank's transformative journey."    )
        st.write("[Alpha Bank](https://www.linkedin.com/company/alpha-bank/)")
        
        
        
        st.title("Consumer Data Science Executive")
        st.subheader("Philip Morris Greece • April 2020 - July 2022")
        st.write("I seized the opportunity to express my keen interest in joining the Data Science team. To summarize, I was an integral part of the DS Team from April 2020 to July 2022. My evolving business acumen coupled with continuously honed technical skills enabled my team and me to devise improved problem-solving approaches and compelling narratives. During my tenure, I transitioned from Excel to more robust tools like R and SQL, while harnessing Power BI for data visualization, crafting dynamic dashboards, and generating interactive reports. My focus centered on driving Acquisition and Retention initiatives, entailing the discernment of data patterns, the creation of visually engaging dashboards, end-to-end project management, CRM utilization, participation in ML model development, Data warehouse implementation, and mentoring junior team members. In my perspective, Data Science is akin to mastering the art of dancing in the rain. The insights derived from the data undeniably underscored the valuable role our efforts played in Philip Morris' achievements, from Elevating Consumer Satisfaction and ensuring quality Acquisition, to minimizing average churn probability, expanding Share of Market, and positively impacting various other KPIs. An illustrative instance of this was witnessed during the successful launch of a new product in the Greek market. From meticulously monitoring its impact to strategically planning the subsequent steps, this experience enriched my comprehension of the 'how' and 'why' that drive business thinking."    )
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

