from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Sean Cooke CV"
PAGE_ICON = ":wave:"
NAME = "Sean Cooke"
DESCRIPTION = """
Experienced Data Science professional with a strong background in analytics, machine learning, and data
visualization.
"""
SOCIAL_MEDIA = {

    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",

 }
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    linkedinlink = "https://www.linkedin.com/in/seanolivercooke/"
   
    # "Note, if you don't have an Open AI API key yet, you can get one [by clicking here](%s)" % url
    st.write("📫", f"[Linkedin]({linkedinlink})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python, SQL and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Keras), SQL, PySpark, R, DAX
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("**Data Scientist | Musgrave**")
st.write("May 2023 - Oct 2023")
st.write(
    """
- Data Scientist for Ireland's largest retail group - Insight & Innovation Department.
- Drive projects in various areas: product /sales analytics, customer behaviour analytics (**RFM, LTV**),
loyalty (**Surveys, NPS & Sentiment Analysis**), and marketing (**Segmented Email Personalisation**).
- reation and management of scheduled **ETL pipelines** and data models in **Azure Databricks**,
ensuring data is readily available and refreshed for consumption by visualization tools.
- Utilises best in class dashboard & visualization techniques in **Power BI & Python** to derive business
value and guide strategic initiatives. (Key Driver Analysis Matrix).
- Clearly and concisely explain technical findings to non-technical peers and senior business stakeholders.
- **Example Projects**:
    - Automated theme & sentiment extraction of customer free-text surveys (**NLP**), reducing man
hours and need for manual categorization of feedback.
    - New product launch - first year sales estimation (**Sklearn, Catboost**).
    - Automated email audience segment personalisation & product recommendations.
    - Short term ad-hoc analyses as required (e.g. external event impact on product sales, queueing
analytics, traffic analysis etc.).
"""
)

# --- JOB 2
st.write('\n')
st.write("**Business Intelligence Consultant & Assistant Manager | Grant Thornton**")
st.write("Jul 2021 - Apr 2023")
st.write(
    """
- Data analytics consultant for a variety of private & state bodies in Healthcre, Retail, Trade & Enterprise,
Education, and Pharma.
- Conducted machine learning research & development **(Python, R, Azure AutoML)** e.g. wait
time prediction, KPI breaches / anomaly detection, forecasting, survey analysis **(NLP)**.
- **Power BI** dashboard development; **SQL** database development, data modeling & management.
- Conduct regular presentations to non-technical stakeholders.
- **rocess Automation** internally within Grant Thornton and externally / client facing.
- Provide oversight and mentorship to junior staff working on analytics projects to ensure high quality
outputs within deadlines.
- Hold regular internal training seminars on Data Analytics topics, fostering growth and interest of the
subject amongst non-technical team members.
- Review CVs and act as **Data Science & Analytics subject matter expert** in interviews.
- **Achievements**:
    - Received multiple internal awards (nominated by colleagues) for recognition of Data Analytics work.
    - Eliminated overtime hours on long-term client job through automation of large C-suite report.
    - Developed mission critical cloud-based and interactive reporting solution for a large government body
to replace manually generated reports.
    - Promoted to Assistant Manager within one year.
"""
)

# --- JOB 3
st.write('\n')
st.write("**Data Scientist | Allegiant**")
st.write("May 2019 - Apr 2021")
st.write(
    """
- Data Scientist for AnPost Bank’s Moneyback Programme. Developed machine learning models (LTV,
Churn, Next Purchase Prediction), analytics, and visualizations of operational and customer metrics
using various tools – Python, SQL, R, Rest APIs.
- Automated KYC / Identity Verification / Fraudulent Account detection for bank onboarding via Rest
APIs and custom rule-based classification models.
- Built predictive models (ScikitLearn, Keras) to solve complex business / retail questions – sales
forecasting, customer lookalike models, entity resolution.
- Developed customer segmentation models based on a variety of large and disparate datasets,
transaction patterns and demographics to measure and improve loyalty and acquisition (e.g. RFM / CLV
modelling)
- **Achievements**:
    - Developed Process Automation App with GUI (Python). Monthly manual transaction process was
reduced from several hours to roughly 10 minutes. Human error was eliminated.
    - Eliminated overtime hours on long-term client job through automation of large C-suite report.
    - Developed Python tool to automatically sanitize, correct & enhance customer data prior to loading to
SQL database. Substantially reduced manual workload on 70%wwwwwwww+ of customer records.
"""
)

# --- JOB 4
st.write('\n')
st.write("**Marketing Officer | irish Guide Dogs for the Blind**")
st.write("Feb 2013 - Feb 2015")
st.write(
    """
- Planned and Managed nationwide marketing campaigns (Direct Mail, Phone, Online, TV), conducting
regular pre and post-campaign data analysis to ensure KPIs are met or exceeded, and identify
opportunities for improved performance.
- Forecast and budget monthly and multi-year revenue for the CEO and Board of Directors.
- Maximised income via precise marketing lists, A/B testing, and ensuring donors receive the highest
level of care. Minimised costs by increasing process efficiency and ensuring expenses are within/below
budget.
- Managed Teams of volunteers through marketing campaign logistics.
- Project managed successful delivery of new CRM marketing system – working with Database Admin in
creation of campaign data analysis/extraction processes, troubleshooting, testing and tracking (JIRA)
- **Achievements**:
    - Reduced the cost of a popular biannual marketing campaign by 70%, resulting in a 400% R.O.I.
    - Created a new, sustainable, low-cost annual income stream via IRS Charitable Donation Scheme
"""
)

