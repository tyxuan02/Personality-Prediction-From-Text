import streamlit as st
import json 
import pandas as pd
from collections import Counter
from model_predictor import Model

def app():
    @st.cache_resource()
    def load_model():
        return Model()

    @st.cache_resource()
    def load_output():
        with open('custom_output.json', encoding='utf-8') as f:
            return json.load(f)

    predictor = load_model()
    outputs = load_output()

    st.markdown("""
        <style>
            /* Global Styles */
            .stApp {
                background: linear-gradient(135deg, #f5f7fa 0%, #f8f9fa 100%);
            }
            
            /* Hide fullscreen button */
            button[title="View fullscreen"] {
                visibility: hidden;
            }
            
            /* Main Title Styling */
            .title {
                font-size: 3em;
                background: linear-gradient(120deg, #4B0082, #6A5ACD);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 800;
                text-align: center;
                word-wrap: break-word;
                animation: fadeIn 1s ease-in;
            }
            
            /* Subheading Styling */
            .subheading {
                font-size: 1.5em;
                color: #6A5ACD;
                margin-bottom: 30px;
                text-align: center;
                font-weight: 500;
                animation: slideIn 1s ease-out;
            }
            
            /* Result Styling */
            .result-style {
                font-size: 2.2em;
                background: linear-gradient(120deg, #4B0082, #6A5ACD);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 25px;
                font-weight: bold;
                text-align: center;
            }
            
            .result-subheading {
                font-size: 1.7em;
                color: #4B0082;
                margin: 25px 0;
                font-weight: 600;
                border-bottom: 2px solid #6A5ACD;
                padding-bottom: 10px;
            }
            
            /* MBTI Type Styling */
            .mbti-type-title {
                font-weight: bold;
                font-size: 24px;
                margin-bottom: 15px;
                color: #4B0082;
            }
            
            .mbti-desc {
                display: block;
                text-align: justify;
                line-height: 1.6;
                color: #2C3E50;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .mbti-view-details {
                text-decoration: none;
                display: inline-block;
                margin-top: 5px;
                padding: 8px 16px;
                transition: all 0.3s ease;
            }
            
            .mbti-view-details:hover {
                transform: translateY(-2px);
            }
            
            /* Trait Styling */
            .trait-label {
                font-size: 1.2em;
                font-weight: 600;
                color: #4B0082;
                margin-top: 15px;
            }
            
            .trait-box {
                background-color: #f0f0f5;
                color: #ffffff;
                padding: 20px;
                border-radius: 20px;
                margin: 10px 0;
                text-align: justify;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            }
            
            .trait-box:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
            }
                
            /* Text Field Styling */
            .stTextInput input {
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                padding: 15px;
                font-size: 16px;
            }
                
            .stTextInput input:focus {
                border: 2px solid #6A5ACD;
                box-shadow: 0 0 0 2px rgba(106, 90, 205, 0.2);
            }
            
            /* Input Area Styling */
            .stTextArea textarea {
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                padding: 15px;
                font-size: 16px;
                text-align: justify;
            }
            
            .stTextArea textarea:focus {
                border: 2px solid #6A5ACD;
                box-shadow: 0 0 0 2px rgba(106, 90, 205, 0.2);
            }
            
            /* Button Styling */
            .stButton button {
                background: linear-gradient(135deg, #4B0082, #6A5ACD);
                color: white !important;
                border: none;
                padding: 10px 25px;
                border-radius: 25px;
                font-weight: 600;
                transition: all 0.3s ease;

                &:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(106, 90, 205, 0.3);
                }
            }
            
            /* File Uploader Styling */
            .stFileUploader {
                background: white;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
            }
            
            /* File Upload Button Styling */
            .stFileUploader > section > button {
                background: linear-gradient(135deg, #4B0082, #6A5ACD);
                color: white !important;
                border: none;
                padding: 10px 25px;
                border-radius: 25px;
                transition: all 0.3s ease;

                &:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(106, 90, 205, 0.3);
                }

                &:active {
                    transform: translateY(0);
                    box-shadow: none;
                }
            }
            
            /* DataFrame Styling */
            .stDataFrame {
                background: white;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
                
            /* Divider Styling */
            .stMarkdown hr {
                border: none;
                height: 2px;
                background: linear-gradient(to right, transparent, #6A5ACD, transparent);
                margin: 30px 0;
            }
            
            /* Animations */
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            @keyframes slideIn {
                from { 
                    transform: translateY(-20px);
                    opacity: 0;
                }
                to {
                    transform: translateY(0);
                    opacity: 1;
                }
            }
                
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-10px); }
                75% { transform: translateX(10px); }
            }
            
            /* Error Message Styling */
            .stAlert {
                animation: shake 0.5s ease-in-out;
            }
            
            /* Selectbox Styling */
            .stSelectbox {
                margin-bottom: 20px;
            }
            
            .stSelectbox > div > div {
                background: white;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                transition: all 0.3s ease;
            }
            
            .stSelectbox > div > div:hover {
                border-color: #6A5ACD;
            }
                
            /* Responsive Design */
            @media (max-width: 768px) {
                .mbti-desc {
                    padding: 15px;
                    text-align: left;
                }

                .trait-box {
                    padding: 15px;
                    text-align: left;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Personality Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheading">Discover Your MBTI Personality Type</div>', unsafe_allow_html=True)

    option = st.selectbox('Select input type:', ('Text', 'CSV or Excel File'), index=0)
    if option == 'Text':
        st.info(f"Please provide a text containing 50 to 250 words. For better results, a text of around 200 words is recommended. Ensure the text is written in English.")
        txt = st.text_area(label="Input Text", placeholder="Enter your text here...", height=200)
        words = txt.split()

        num_words = len(words)
        st.markdown(f"<div style='margin: 0 0 20px 5px'><b>Word Count:</b> {num_words}</div>", unsafe_allow_html=True)
        predict_button = st.button("Predict", key="predict_button")
        
        if predict_button:
            if not txt or not txt.strip():
                st.error("Please enter some text to predict.")
            elif all(word.isdigit() for word in words):
                st.error("Please provide text instead of numbers.")
            elif 50 <= num_words <= 250:
                st.write("---------")
                with st.spinner("Analyzing your text..."):
                    probs, binary_predictions, predicted_mbti_type = predictor.predict(txt)
                    
                probabilities = [float(prob) for prob in probs[0]]
                mbti_dimensions = ["IE", "NS", "TF", "JP"]
                mbti_trait = [mbti_dimensions[i][trait] for i, trait in enumerate(binary_predictions[0])]

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
                
                st.markdown(f'<div class="result-subheading">Probabilities of Each MBTI Dimension:</div>', unsafe_allow_html=True)
                type_probabilities = pd.DataFrame({"MBTI Dimension": mbti_dimensions, "Probability": probabilities, "Trait": mbti_trait})
                st.dataframe(type_probabilities.set_index("MBTI Dimension"), width=800)
                
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
                st.error("Please enter a text between 50 and 250 words.")
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
                st.write("Data Preview:")
                st.dataframe(df, width=800)

            column_name = st.text_input("Enter the column name containing the text:")
            if column_name and column_name in df.columns:
                if st.button("Predict for all rows", key="predict_all_button"):
                    st.write("---------")
                    with st.spinner("Analyzing..."):
                        predictions = [
                            predictor.predict(row[column_name])[2] if (isinstance(row[column_name], str))
                        else "Text length is less than 50 words."
                            for _, row in df.iterrows()
                        ]
                    df['Predicted MBTI Type'] = predictions
                    st.markdown(f'<div class="result-subheading">Predicted MBTI Types for All Rows:</div>', unsafe_allow_html=True)
                    st.dataframe(df[[column_name, 'Predicted MBTI Type']], width=800)
                    valid_predictions = [p for p in predictions if p != "Text length is less than 50 words."]
                    if valid_predictions:
                        overall_mbti = Counter(valid_predictions).most_common(1)[0][0]

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