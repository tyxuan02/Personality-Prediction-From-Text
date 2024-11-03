import streamlit as st
import json

# Configure the page
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the output
@st.cache_resource()
def load_output():
    with open('custom_output.json', encoding='utf-8') as f:
        return json.load(f)

outputs = load_output()

# Custom CSS for styling
st.markdown("""
    <style>
        button[title="View fullscreen"] {
            visibility: hidden;
        }
        .title-style {
            font-size: 2.5em;
            color: #4B0082;
            font-weight: 700;
        }
        .subheading-style {
            font-size: 1.5em;
            font-weight: 600;
            color: #6A5ACD;
        }
        .trait-box {
            background-color: #f0f0f5;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .trait-title {
            font-weight: bold;
            font-size: 18px;
            color: #ffffff;
        }
        .trait-desc {
            text-align: justify;
            color: #ffffff;
        }
        .mbti-type-box {
            background-color: transparent;
            margin: 2em 0;
        }
        .mbti-type-title {
            font-weight: bold;
            font-size: 18px;
        }
        .mbti-desc {
            margin: 0.5em 0;
        }
        .mbti-view-details {
            color: #2E86C1;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-style">What\'s Your MBTI Personality Type?</div>', unsafe_allow_html=True)
st.write("---")
st.markdown('<div class="subheading-style">Personality Traits</div>', unsafe_allow_html=True)

for i in range(0, len(outputs['mbti_traits']), 2):
    col1, col2 = st.columns(2)
    for idx, col in enumerate((col1, col2)):
        if i + idx < len(outputs['mbti_traits']):
            trait = outputs['mbti_traits'][i + idx]
            col.markdown(f"<div class='trait-box' style='background-color: {trait['color']};'>"
                         f"<div class='trait-title'>{trait['name']}</div>"
                         f"<p class='trait-desc'>{trait['description']}</p>"
                         f"</div>", unsafe_allow_html=True)

# Display MBTI types below traits
st.write("---")
st.markdown('<div class="subheading-style">Personality Types</div>', unsafe_allow_html=True)

for i in range(0, len(outputs['mbti_type']), 2):
    col1, col2 = st.columns(2)
    for idx, col in enumerate((col1, col2)):
        if i + idx < len(outputs['mbti_type']):
            mbti_type = outputs['mbti_type'][i + idx]
            with col:
                st.markdown(f"<div class='mbti-type-box'>", unsafe_allow_html=True)
                inner_col1, inner_col2 = st.columns([1, 2])
                with inner_col1:
                    st.image(mbti_type['img'], use_column_width=True)
                with inner_col2:
                    st.markdown(f"<div class='mbti-type-title'>{mbti_type['type']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='mbti-desc'>{mbti_type['description']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<a href='{mbti_type['url']}' target='_blank' class='mbti-view-details'>View more details</a>", unsafe_allow_html=True)