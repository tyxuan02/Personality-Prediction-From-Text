import streamlit as st
import pandas as pd
from model_predictor import ModelPredictor  # Import the model class
from collections import Counter

# Configure the page
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
        .title-style {
            font-size: 2.5em;
            color: #4B0082;
            font-weight: 700;
        }
        .subheading-style {
            font-size: 1.5em;
            color: #6A5ACD;
            margin-bottom: 0.5em;
        }
        div.stButton > button:first-child {
            border: none;
            background-color: #6A5ACD;
            color: white !important;
            font-size: 1.2em;
            padding: 0.5em 1.5em;
            border-radius: 8px;
            transition: 0.3s;
        }
        div.stButton > button:first-child:hover {
            border: none;
            background-color: #4B0082;
        }
        .result-style {
            font-size: 1.8em;
            color: #4B0082;
            margin-top: 1em;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Load the model
@st.cache_resource()
def load_model():
    return ModelPredictor()

predictor = load_model()

# Header Section
st.markdown('<div class="title-style">🔮 Personality Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subheading-style">Discover Your MBTI Personality Type</div>', unsafe_allow_html=True)
st.write("---------")

# Input type selection
option = st.selectbox('Select input type:', ('Text', 'CSV or Excel File'), index=0)

if option == 'Text':
    # Text Input Area
    txt = st.text_area(
        label="Input Text",
        placeholder="Enter text here...",
        height=200,
    )

    # Prediction Button
    if st.button("Predict", key="predict_button"):
        if txt and len(txt.split()) > 20:
            with st.spinner("Analyzing your text..."):
                predicted_label = predictor.predict(txt)
            st.markdown(f'<div class="result-style">Predicted MBTI Type: {predicted_label}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter text with more than 20 words.")

elif option == 'CSV or Excel File':
    # File Upload Area (limit to one file)
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=False)
    if uploaded_file is not None:
        # Load file into a DataFrame
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Limit dataset to 100 rows and check sample
        df = df.head(100)
        st.write("Sample of uploaded data:")
        st.write(df.head(10))

        # Column selection input
        column_name = st.text_input("Enter the column name containing the text:")

        # Validate column name and make predictions
        if column_name and column_name in df.columns:
            if st.button("Predict for all rows", key="predict_all_button"):
                with st.spinner("Analyzing the text in each row..."):
                    predictions = []
                    for _, row in df.iterrows():
                        text = row[column_name]
                        # Check if text is a string and has more than 20 words
                        if isinstance(text, str) and len(text.split()) > 20:
                            prediction = predictor.predict(text)
                            predictions.append(prediction)
                        else:
                            predictions.append("Insufficient words")  # Flag insufficient text entries

                    # Add predictions to the DataFrame and display results
                    df['Predicted MBTI Type'] = predictions
                    st.write("Prediction results:")
                    st.write(df[[column_name, 'Predicted MBTI Type']])

                    # Filter valid predictions for overall type calculation
                    valid_predictions = [p for p in predictions if p != "Insufficient words"]
                    if valid_predictions:
                        overall_mbti_type = Counter(valid_predictions).most_common(1)[0][0]
                        st.markdown(f'<div class="result-style">Overall MBTI Type: {overall_mbti_type}</div>', unsafe_allow_html=True)
                    else:
                        st.warning("All rows have insufficient words. No overall MBTI type calculated. Please ensure all rows have text entries with more than 20 words.")

        elif column_name:
            st.error(f"Column '{column_name}' not found in the file. Please check the column name and try again.")

# Footer Section
st.write("---------")
st.markdown(
    """
    <div style="text-align: center; color: #8A8A8A; font-size: 0.9em;">
        Powered by advanced NLP algorithms &mdash; providing accurate MBTI predictions for curious minds! 💡
    </div>
    """, unsafe_allow_html=True
)