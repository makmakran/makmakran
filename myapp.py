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
            "My journey into the world of data began in the summer of 2017 when I became a part of Philip Morris Greece - Papastratos AVES through the Inkompass internship program. As a newcomer to the realm of data and still a student, I delved deep into understanding business logic and the key performance indicators (KPIs) critical for the salesforce's monitoring. I played a vital role in the reporting team, where my responsibilities included generating reports and conducting ad hoc analyses for the entire field force of the company. Utilizing basic tools like Microsoft Excel and PowerPoint, my communication skills flourished as I provided daily and weekly reports along with feedback emails to the management team. It's worth noting that I had the privilege of being part of the special team that launched the IQOS heat-not-burn innovation device in Greece—an opportunity for which I am truly grateful. Initially, my tasks revolved around meeting the operational and customer reporting needs of the business stakeholders. After completing my military service year in Cyprus, I returned to Papastratos and assumed the role of Consumer Journey Analyst. This transition was seamless due to the overlap in content with my previous experiences. In this role, I had the exciting responsibility of setting up the Net Promoter Score (NPS) from scratch. We designed NPS queries for every consumer touchpoint around the product, aligning every business initiative with the perspective of the consumer journey map. Six months later, I progressed to the Consumer Voice team—a role that was both intriguing and challenging. As a core member, I contributed significantly to crucial company projects, including Social Media campaigns for the current period, a text analytics project focused on consumer voice feedback, sentiment analysis, and topic clustering. Ensuring data integrity and confidentiality was also part of my responsibilities. My daily routine involved close collaboration with various departments to ensure alignment on updated commercialization strategies. Given my comprehensive understanding of data collection, I became the custodian of the related web platform—an essential tool for fetching our data. This role expanded my skills in managing consulting agencies, a task that was pivotal for successful data utilization. This particular year marked a significant milestone for the company's vision, driving it toward resounding success." )
    
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
        "The Master Program in Informatics addresses contemporary technological challenges and the practical applications of computer science across various modern disciplines. The program's content and nature are meticulously designed to effectively address the distinct scientific requirements stemming from the swift evolution of Information and its applications on both European and global scales. With a background rooted in mathematical thinking, acquired through my education at a Technical University, this postgraduate program aligns seamlessly with my aspirations. It serves as a pivotal opportunity to augment my professional journey in the realm of data by bolstering my expertise with robust IT academic knowledge. This integration of theoretical insights and practical skills promises to significantly enrich my understanding of data-related matters." )
        st.write("[Thesis](https://dione.lib.unipi.gr/xmlui/bitstream/handle/unipi/15143/Makrandreou_20045.pdf?sequence=3&isAllowed=y): Customer Behavior Prediction, based on activities sequence, using Keras and LSTM")
        st.write("##")
        st.title("National Technical University of Athens")
        st.subheader("Diploma in Geomatic Engineering• October 2012 - March 2018")
        st.write(
        "The curriculum of the School is intricately woven around the scientific and technical endeavors of Rural and Surveying Engineers, harmonizing with Greece's production and developmental aspirations. Its primary objective is to equip students with the requisite scientific and technological knowledge, empowering them to excel within the domain of Rural and Surveying Engineering. From my perspective, the essence of my engineering studies extends beyond the mere acquisition of the skill of making assumptions. It's about cultivating confidence. This often underestimated facet plays a significant role, particularly at the outset of one's journey. What holds more weight than raw skill is the assurance to take that leap, to initiate action. In essence, it's about embarking on the journey with the courage to begin, to set something in motion." )
        st.write("[Thesis](https://dspace.lib.ntua.gr/xmlui/bitstream/handle/123456789/47064/%ce%95%cf%81%ce%b3%ce%b1%cf%83%ce%af%ce%b1.pdf?sequence=1&isAllowed=y): 3D City modelling Athens, using CityGML")

    with right_column:
        st_lottie(lottie_coding2, height=300, key="coding2")

