import streamlit as st
from multiapp import MultiApp
from apps import HOME, MBTI, ABOUT, TEXT_IDEAS

# Configure the page
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# st.markdown(
#     """
#     <h1 style="text-align: center; font-size: 60px;">FitLifePro</h1>
#     """,
#     unsafe_allow_html=True
# )

app = MultiApp()

# Add all your application here
app.add_app("Home", HOME.app)
app.add_app("Text Ideas", TEXT_IDEAS.app)
app.add_app("MBTI", MBTI.app)
app.add_app("About", ABOUT.app)
# The main app
app.run() 