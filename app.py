import streamlit as st
from multiapp import MultiApp
from apps import HOME, MBTI, ABOUT, TEXT_IDEAS

st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

app = MultiApp()

app.add_app("Home", HOME.app)
app.add_app("MBTI", MBTI.app)
app.add_app("Text Ideas", TEXT_IDEAS.app)
app.add_app("About", ABOUT.app)

app.run() 