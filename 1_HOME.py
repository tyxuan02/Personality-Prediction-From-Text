import streamlit as st
import json 
import pandas as pd
from collections import Counter
from model_predictor import ModelPredictor  # Import the model class

# Configure the page
st.set_page_config(
    page_title="Home - Personality Predictor",
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
        .result-subheading {
            font-size: 1.5em;
            color: #4B0082;
            margin-bottom: 1em;
            font-weight: 600;
        }
        .mbti-type-title {
            font-weight: bold;
            font-size: 20px;
            margin-bottom: 0.5em;
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
            font-size: 1.1em;
            # font-weight: 600;
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
    st.info(f"Please enter a text between 20 and 150 words. Words between 100 - 120 are ideal for better predictions. Ensure the text is in English and does not include any numbers.")
    txt = st.text_area(label="Input Text", placeholder="Enter your text here...", height=200)
    words = txt.split()

    col1, col2 = st.columns([1, 1])
    with col1:
        predict_button = st.button("Predict", key="predict_button")
        # generate_text = st.button("Generate Random Text", key="generate_text_button")
    with col2:
        # Display word count
        num_words = len(words)
        st.markdown(f"<div style='text-align: right;'>Number of words: {num_words}</div>", unsafe_allow_html=True)

    # if generate_text:
    #     st.switch_page(page="pages/2_MBTI.py")

    if predict_button:
        # Check if all words digits
        if all(word.isdigit() for word in words):
            st.error("Please enter a text without any numbers.")
        elif 20 <= num_words <= 150:
            st.write("---------")
            with st.spinner("Analyzing your text..."):
                probs, binary_predictions, predicted_mbti_type = predictor.predict(txt)
                
            probabilities = [float(prob) for prob in probs[0]]
            mbti_dimensions = ["IE", "NS", "TF", "JP"]
            mbti_trait = [mbti_dimensions[i][trait] for i, trait in enumerate(binary_predictions[0])]

            # Display the predicted MBTI type with details
            st.markdown(f'<div class="result-subheading">Predicted MBTI Type:</div>', unsafe_allow_html=True)
            predicted_type = [ output for output in outputs['mbti_type'] if output["type"] == predicted_mbti_type ]
            description = predicted_type[0]["description"]
            img = predicted_type[0]["img"]
            url = predicted_type[0]["url"]
            
            col1, col2 = st.columns([1, 2]) 
            with col1:
                st.image(img, caption=f"{predicted_mbti_type}", use_column_width=True)
            with col2:
                st.markdown(f"<div class='mbti-type-title'>{predicted_mbti_type}</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="mbti-desc">{description}</div>', unsafe_allow_html=True)
                st.markdown(f'<a href="{url}" target="_blank" class="mbti-view-details">View more details</a>', unsafe_allow_html=True)
            
            # Display the probabilities
            st.markdown(f'<div class="result-subheading">Probabilities of Each MBTI Dimension:</div>', unsafe_allow_html=True)
            type_probabilities = pd.DataFrame({"MBTI Dimension": mbti_dimensions, "Probability": probabilities, "Trait": mbti_trait})
            st.dataframe(type_probabilities.set_index("MBTI Dimension"), width=800)
            
            # Display the traits of the predicted MBTI type
            mbti_traits = [ trait for trait in predicted_mbti_type ]
            predicted_mbti_traits = [ output for output in outputs['mbti_traits'] if output["trait"] in mbti_traits ]

            st.markdown(f'<div class="result-subheading">Predicted MBTI Traits:</div>', unsafe_allow_html=True)
            for trait in predicted_mbti_traits:
                trait_name = trait["name"]
                trait_desc = trait["description"]
                trait_color = trait["color"]
                st.markdown(f'<div class="trait-label">{trait_name}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="trait-box" style="background-color: {trait_color};">{trait_desc}</div>', unsafe_allow_html=True)        
        else:
            st.error("Please enter a text between 20 and 150 words.")
elif option == 'CSV or Excel File':
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=False)
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        if df.empty:
            st.error("The uploaded file is empty. Please upload a valid file.")
        else:
            # st.write(f"File uploaded: {uploaded_file.name}")
            st.write("Data Preview:")
            st.dataframe(df, width=800)

        column_name = st.text_input("Enter the column name containing the text:")
        if column_name and column_name in df.columns:
            if st.button("Predict for all rows", key="predict_all_button"):
                st.write("---------")
                with st.spinner("Analyzing..."):
                    predictions = [
                        predictor.predict(row[column_name])[2] if (isinstance(row[column_name], str) and len(row[column_name].split()) > 19 and len(row[column_name].split()) < 151)
                        else "Text length not between 20 and 150 words"
                        for _, row in df.iterrows()
                    ]
                df['Predicted MBTI Type'] = predictions
                st.markdown(f'<div class="result-subheading">Predicted MBTI Types for All Rows:</div>', unsafe_allow_html=True)
                st.dataframe(df[[column_name, 'Predicted MBTI Type']], width=800)
                valid_predictions = [p for p in predictions if p != "Text length not between 20 and 150 words"]
                if valid_predictions:
                    overall_mbti = Counter(valid_predictions).most_common(1)[0][0]

                    # Display the predicted MBTI type with details
                    st.markdown(f'<div class="result-subheading">Overall MBTI Type:</div>', unsafe_allow_html=True)
                    predicted_type = [ output for output in outputs['mbti_type'] if output["type"] == overall_mbti ]
                    description = predicted_type[0]["description"]
                    img = predicted_type[0]["img"]
                    url = predicted_type[0]["url"]
                    
                    col1, col2 = st.columns([1, 2]) 
                    with col1:
                        st.image(img, caption=f"{overall_mbti}", use_column_width=True)
                    with col2:
                        st.markdown(f"<div class='mbti-type-title'>{overall_mbti}</div>", unsafe_allow_html=True)
                        st.markdown(f'<div class="mbti-desc">{description}</div>', unsafe_allow_html=True)
                        st.markdown(f'<a href="{url}" target="_blank" class="mbti-view-details">View more details</a>', unsafe_allow_html=True)
                else:                            
                    st.error("No valid predictions found. Please check the text length and try again.")
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