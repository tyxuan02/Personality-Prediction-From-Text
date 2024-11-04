import streamlit as st

# Configure the page
st.set_page_config(
    page_title="About - Personality Predictor",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
        .page-title {
            font-size: 2.5em;
            color: #4B0082;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .section-heading {
            font-size: 1.8em;
            font-weight: bold;
            color: #6A5ACD;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .section-text {
            color: #333333;
            text-align: justify;
            margin-bottom: 20px;
        }
        .disclaimer-text {
            font-size: 1em;
            color: #FF6347;
            font-style: italic;
            text-align: justify;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .usage-step {
            font-size: 1.1em;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown('<div class="page-title">About the Personality Predictor</div>', unsafe_allow_html=True)

# Sections
st.markdown('<div class="section-heading">What is this tool?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
This is a web-based personality prediction tool that analyzes text input to predict your Myers-Briggs Type Indicator (MBTI) personality type.  Using advanced machine learning technology, it can analyze the text input and predict your likely personality type, offering a modern approach to personality assessment.           
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">What is the purpose of this system?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

Traditional personality assessments typically rely on standardized questionnaires, which can be time-consuming and may be influenced by self-reporting bias. This system offers an alternative approach by:

- Analyzing natural language patterns in your writing
- Providing quick insights into personality traits
- Offering a more organic way to understand personality through everyday communication
- Leveraging machine learning to identify subtle patterns that might not be apparent in traditional assessments
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">What is MBTI and how does it work?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

The Myers-Briggs Type Indicator (MBTI) is one of the world's most widely used personality assessment tools. It categorizes personalities across four key dimensions:

- E/I: Extraversion (E) vs. Introversion (I)
- S/N: Sensing (S) vs. Intuition (N)
- T/F: Thinking (T) vs. Feeling (F)
- J/P: Judging (J) vs. Perceiving (P)

These combinations create 16 distinct personality types such INFP, ESTJ, INTJ, etc. Each type has its own unique characteristics, strengths, and weaknesses.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">What technology powers this tool?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

This system utilizes:

- BERT (Bidirectional Encoder Representations from Transformers), a state-of-the-art natural language processing model
- Training data from the MBTI 500 dataset: https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset
- Achievement of ?% accuracy in personality prediction through extensive training and validation
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">How to use the tool?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

<b>1. Text Input Method:</b>
- Enter a text sample (minimum 20 words)
- The text can be any form of writing (emails, social media posts, essays, etc.)
- Click the "Predict" button to get the predicted personality type

<b>2. File Upload Method:</b>
- Upload a CSV or Excel file containing text data
- Enter the column name that contains the text data
- Click the "Predict for all rows" button to get the predicted personality types for all rows
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">What are the limitations and considerations?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

<b>1. Accuracy Considerations:</b>
- While our model achieves good accuracy, it's not 100% definitive
- Results should be considered as insights rather than absolute determinations
- For a comprehensive assessment, consider taking the official MBTI test at 16personalities.com

<b>2. Best Practices:</b>
- Provide genuine text samples for more accurate results
- Use text samples of sufficient length (20+ words)
- Consider multiple analyses for more reliable insights

<b>3. Not Suitable For:</b>
- Clinical or diagnostic purposes
- Major life decisions without additional assessment
- Legal or professional evaluation requirements
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">Can I improve the accuracy of my results?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

- Provide longer text samples (100 words is ideal)
- Use your natural writing style
- Submit multiple different text samples
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">Is my data secure?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

- All text analysis is performed locally
- Your submitted text is not stored or saved
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-heading">How reliable are the results?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-text">

- The model achieve ?% accuracy in validation tests
- However, results are not guaranteed to be accurate
- They are based on statistical patterns and probabilities
- Use the results as a guide, not a definitive assessment
- For a more comprehensive evaluation, consider taking the official MBTI test: https://www.16personalities.com/
</div>
""", unsafe_allow_html=True)
