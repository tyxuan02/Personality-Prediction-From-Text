import streamlit as st

def app():
    st.markdown("""
        <style>
            /* Global Styles */
            .stApp {
                background: linear-gradient(135deg, #f5f7fa 0%, #f8f9fa 100%);
            }

            /* Title Styling */
            .title {
                font-size: 3em;
                background: linear-gradient(120deg, #4B0082, #6A5ACD);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 800;
                text-align: center;
                word-wrap: break-word;
                margin-bottom: 30px;
                animation: fadeIn 1s ease-in;
            }

            /* Section Heading Styling */
            .section-heading {
                font-size: 1.8em;
                color: #4B0082;
                margin-bottom: 20px;
                font-weight: 600;
                text-align: left;
                animation: slideIn 0.8s ease-out;
                border-bottom: 3px solid #6A5ACD;
                padding-bottom: 10px;
                width: 100%;
            }

            /* Section Text Styling */
            .section-text {
                color: #2C3E50;
                text-align: justify;
                padding: 25px;
                border-radius: 15px;
                background: white;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
                margin-bottom: 50px;
                animation: slideUp 0.6s ease-out;

                > li, p {
                    line-height: 1.6;
                    font-size: 1.1em;
                }
            }
                
            /* Divider Styling */
            .stMarkdown hr {
                border: none;
                height: 2px;
                background: linear-gradient(to right, transparent, #6A5ACD, transparent);
                margin: 30px 0;
            }
                
            p {
                margin: 0;
                padding: 0;
            }

            /* Animations */
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            @keyframes slideIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            @keyframes slideUp {
                from { 
                    transform: translateY(20px);
                    opacity: 0;
                }
                to { 
                    transform: translateY(0);
                    opacity: 1;
                }
            }

            /* Responsive Design */
            @media (max-width: 768px) {
                .title {
                    font-size: 2.2em;
                }

                .section-heading {
                    font-size: 1.5em;
                }

                .section-text {
                    font-size: 1em;
                    text-align: left;
                    padding: 20px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">About the Personality Predictor</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-heading">What is this tool?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <p>This is a web-based personality prediction tool that analyzes text input to predict your Myers-Briggs Type Indicator (MBTI) personality type.  Using advanced machine learning technology, it can analyze the text input and predict your likely personality type, offering a modern approach to personality assessment.</p>           
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">What is the purpose of this system?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <p style='margin-bottom: 15px;'>Traditional personality assessments typically rely on standardized questionnaires, which can be time-consuming and may be influenced by self-reporting bias. This system offers an alternative approach by:</p>
        <li>Analyzing natural language patterns in your writing</li>
        <li>Providing quick insights into personality traits</li>
        <li>Leveraging machine learning to identify subtle patterns that might not be apparent in traditional assessments</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">What is MBTI and how does it work?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <p style='margin-bottom: 15px;'>The Myers-Briggs Type Indicator (MBTI) is one of the world's most widely used personality assessment tools. It categorizes personalities across four key dimensions:<p>
        <li>E/I: Extraversion (E) vs. Introversion (I)</li>
        <li>S/N: Sensing (S) vs. Intuition (N)</li>
        <li>T/F: Thinking (T) vs. Feeling (F)</li>
        <li>J/P: Judging (J) vs. Perceiving (P)</li>
        <p style='margin-top: 15px;'> These 4 dimensions combine to form 16 possible personality types, such as INFP, ESTJ, etc.</p>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">What machine learning model and data are used?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <li>A pre-trained BERT model is fine-tuned on MBTI personality data to predict personality types based on text input.</li>
        <li>A <a href="https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset">MBTI Dataset</a> from Kaggle was used for training the model. The data imbalance issue in the dataset was addressed using oversampling, undersampling and data augmentation.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">How to use the tool?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <p style='font-weight: bold;'>1. Text Input Method:</p>
        <li>Enter a text sample (between 50 and 250 words)</li>
        <li>The text can be any form of writing (emails, social media posts, essays, etc.)</li>
        <li>Click the "Predict" button to get the predicted personality type</li>
        <br>
        <p style='font-weight: bold;'>2. File Upload Method:</p>
        <li>Upload a CSV or Excel file containing text data</li>
        <li>Enter the column name that contains the text data</li>
        <li>Click the "Predict for all rows" button to get the predicted personality types for all rows</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">What are the limitations of this tool?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <li>The tool is currently limited to English-language text input</li>
        <li>The model may not always accurately predict the correct personality type</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-heading">Is my data secure?</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="section-text">
        <li>All submitted text is processed on the client-side (your browser)</li>
        <li>Your submitted text is not stored or saved</li>
    </ul>
    """, unsafe_allow_html=True)
