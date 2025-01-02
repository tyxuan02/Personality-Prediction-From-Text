import streamlit as st

def app():
    # Custom CSS for styling
    st.markdown("""
        <style>
            .page-title {
                font-size: 2.5em;
                color: #4B0082;
                font-weight: bold;
            }
            .section-heading {
                font-size: 1.3em;
                color: #6A5ACD;
                margin-top: 30px;
                margin-bottom: 10px;
            }
            .section-text {
                color: #333333;
                text-align: justify;
                margin-bottom: 30px
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

    st.markdown('<div class="section-heading">What machine learning model and data are used?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-text">

    - A pre-trained BERT model is fine-tuned on MBTI personality data to predict personality types based on text input.
    - A [MBTI Dataset](https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset) from Kaggle was used for training the model. The data imbalance issue in the dataset was addressed using oversampling, undersampling and data augmentation techniques.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">How to use the tool?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-text">

    <b>1. Text Input Method:</b>
    - Enter a text sample (between 50 and 250 words)
    - The text can be any form of writing (emails, social media posts, essays, etc.)
    - Click the "Predict" button to get the predicted personality type

    <b>2. File Upload Method:</b>
    - Upload a CSV or Excel file containing text data
    - Enter the column name that contains the text data
    - Click the "Predict for all rows" button to get the predicted personality types for all rows
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">What are the limitations of this tool?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-text">

    - The tool is currently limited to English-language text input
    - The model may not always accurately predict the correct personality type
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">Is my data secure?</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-text">

    - All data is processed on the client-side (your browser)
    - Your submitted text is not stored or saved
    </div>
    """, unsafe_allow_html=True)