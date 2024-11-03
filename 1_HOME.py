import streamlit as st
import json 
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
            color: #6A5ACD;
        }
        .result-style {
            font-size: 2em;
            color: #4B0082;
            margin-bottom: 1em;
            font-weight: bold;
        }
        .mbti-desc {
            display: block;
            text-align: justify;
        }
        .mbti-view-details {
            display: block;
            margin-top: 1em;
        }
        .trait-label {
            font-size: 1.5em;
            font-weight: 600;
        }
        .trait-box {
            margin: 0.5em 0;
            padding: 1em;
            border-radius: 8px;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Load the model
@st.cache_resource()
def load_model():
    return ModelPredictor()

# Load the output
@st.cache_resource()
def load_output():
    with open('custom_output.json', encoding='utf-8') as f:
        return json.load(f)

predictor = load_model()
outputs = load_output()

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
                predicted_label, trait_probabilities = predictor.predict(txt)

            # Display the predicted MBTI type
            st.write("---------")
            st.markdown(f'<div class="result-style">Predicted MBTI Type: {predicted_label}</div>', unsafe_allow_html=True)

            predicted_mbti_type = [ output for output in outputs['mbti_type'] if output["type"] == predicted_label ]
            description = predicted_mbti_type[0]["description"]
            img = predicted_mbti_type[0]["img"]
            url = predicted_mbti_type[0]["url"]
            
            # Display MBTI Type details
            col1, col2 = st.columns([1, 2]) 
            with col1:
                st.image(img, caption=f"{predicted_label}", use_column_width=True)
            with col2:
                st.markdown(f'<div class="mbti-desc">{description}</div>', unsafe_allow_html=True)
                st.markdown(f'<a href="{url}" target="_blank" class="mbti-view-details">View more details</a>', unsafe_allow_html=True)

            # Display the trait probabilities (in a table) (trait label in the first row and trait probability in the second row)
            trait_probabilities = pd.DataFrame(trait_probabilities.items(), columns=["Trait", "Probability"])
            # Remove index column
            trait_probabilities.set_index("Trait", inplace=True)
            df = pd.DataFrame([trait_probabilities["Probability"]])
            st.dataframe(df, width=800)
            
            mbti_traits = [ trait for trait in predicted_label ]
            predicted_mbti_traits = [ output for output in outputs['mbti_traits'] if output["trait"] in mbti_traits ]

            # Display the traits of the MBTI type
            for trait in predicted_mbti_traits:
                trait_name = trait["name"]
                trait_desc = trait["description"]
                trait_color = trait["color"]
                st.markdown(f'<div class="trait-label">{trait_name}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="trait-box" style="background-color: {trait_color};">{trait_desc}</div>', unsafe_allow_html=True)        
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
                            prediction, _ = predictor.predict(text)
                            predictions.append(prediction)
                        else:
                            predictions.append("Insufficient words")  # Flag insufficient text entries

                    # Add predictions to the DataFrame and display results
                    df['Predicted MBTI Type'] = predictions
                    st.markdown("---------")
                    st.markdown(f'<div class="result-style">Prediction Results</div>', unsafe_allow_html=True)
                    st.write(df[[column_name, 'Predicted MBTI Type']])

                    # # Filter valid predictions for overall type calculation
                    # valid_predictions = [p for p in predictions if p != "Insufficient words"]
                    # if valid_predictions:
                    #     overall_mbti_type = Counter(valid_predictions).most_common(1)[0][0]
                    #     st.markdown(f'<div class="result-style">Overall MBTI Type: {overall_mbti_type}</div>', unsafe_allow_html=True)
                    # else:
                    #     st.warning("All rows have insufficient words. No overall MBTI type calculated. Please ensure all rows have text entries with more than 20 words.")

        elif column_name:
            st.error(f"Column '{column_name}' not found in the file. Please check the column name and try again.")

# # Footer Section
# st.write("---------")
# st.markdown(
#     """
#     <div style="text-align: center; color: #8A8A8A; font-size: 0.9em;">
#         Powered by advanced NLP algorithms &mdash; providing accurate MBTI predictions for curious minds! 💡
#     </div>
#     """, unsafe_allow_html=True
# )