import streamlit as st
import json

def app():
    @st.cache_resource()
    def load_question_sets():
        with open('question_sets.json', encoding='utf-8') as f:
            return json.load(f)
        
    question_sets = load_question_sets()

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
                animation: fadeIn 1s ease-in;
            }

            /* Description Styling */
            .desc {
                color: #2C3E50;
                text-align: justify;
                line-height: 1.6;
                font-size: 1.1em;
                margin-top: 20px;
                border-radius: 15px;
                animation: slideIn 0.8s ease-out;
            }

            /* Subheading Styling */
            .subheading {
                font-size: 1.5em;
                color: #4B0082;
                font-weight: 600;
                border-bottom: 3px solid #6A5ACD;
                padding-bottom: 10px;
                width: 100%;
                animation: slideIn 0.8s ease-out;
            }

            /* Scenario Box Styling */
            .scenario {
                color: #2C3E50;
                font-size: 1.2em;
                font-style: italic;
                margin: 20px 0;
                padding: 25px;
                background: white;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
                border-left: 5px solid #6A5ACD;
                animation: slideUp 0.6s ease-out;
                line-height: 1.6;
            }

            /* Question Styling */
            .question {
                font-size: 1.1em;
                margin: 20px 0 10px 0;
                color: #4B0082;
                font-weight: 500;
                text-align: justify;
                animation: slideUp 0.6s ease-out;
            }
                
            /* Result Styling */
            .result {
                color: #2C3E50;
                font-size: 1.1em;
                margin: 20px 0 10px 0;
                font-weight: 500;
                text-align: justify;
                padding: 15px 0;
            }

            /* Selectbox Styling */
            .stSelectbox {
                margin: 25px 0;
            }

            .stSelectbox > div > div {
                background: white;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                transition: all 0.3s ease;
            }

            .stSelectbox > div > div:hover {
                border-color: #6A5ACD;
                box-shadow: 0 2px 8px rgba(106, 90, 205, 0.2);
            }

            /* Textarea Styling */
            .stTextArea textarea {
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                padding: 15px;
                font-size: 16px;
                background: white;
            }

            .stTextArea textarea:focus {
                border-color: #6A5ACD;
                box-shadow: 0 0 0 2px rgba(106, 90, 205, 0.2);
            }

            /* Button Styling */
            .stButton button {
                background: linear-gradient(135deg, #4B0082, #6A5ACD);
                color: white !important;
                border: none;
                padding: 12px 30px;
                border-radius: 25px;
                font-weight: 600;
                transition: all 0.3s ease;
                margin-top: 20px;
            }

            .stButton button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(106, 90, 205, 0.3);
            }

            /* Error Message Styling */
            .stAlert {
                animation: shake 0.5s ease-in-out;
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
                    transform: translateX(-30px);
                    opacity: 0;
                }
                to { 
                    transform: translateX(0);
                    opacity: 1;
                }
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

            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-10px); }
                75% { transform: translateX(10px); }
            }

            /* Responsive Design */
            @media (max-width: 768px) {
                .title {
                    font-size: 2.2em;
                }

                .desc {
                    font-size: 1em;
                    text-align: left;
                }

                .scenario {
                    font-size: 1.1em;
                    padding: 20px;
                    text-align: left;
                }

                .question {
                    font-size: 1em;
                    text-align: left;
                }

                .stTextArea textarea {
                    font-size: 14px;
                }

                .stButton button {
                    padding: 10px 20px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Create Your Text</div>', unsafe_allow_html=True)
    st.markdown(f"<div class='desc'>Not sure what to write? Use these questions to create your text. Once you've completed the answers, copy the generated text into the predictor to discover your MBTI personality.</div>", unsafe_allow_html=True)

    question_sets_list = [ question_set for question_set in question_sets['question_sets'] ]
    options = [ option['id'] for option in question_sets_list ]
    question_set_choice = st.selectbox(
        "Choose a scenario to answer questions:",
        options,
        format_func = lambda x: question_sets_list[int(x)]['name']
    )

    st.markdown('<div class="subheading">Answer the following questions:</div>', unsafe_allow_html=True)
    st.markdown('<div class="scenario"><b>Scenario:</b> ' + question_sets_list[int(question_set_choice)]['scenario'] + '</div>', unsafe_allow_html=True)
    user_answers = []
    for idx, question in enumerate(question_sets_list[int(question_set_choice)]['questions']):
        st.markdown(f"<div class='question'><b>Question {idx+1}:</b> {question}</div>", unsafe_allow_html=True)
        answer = st.text_area(label=question, key=idx, label_visibility='collapsed')
        user_answers.append(answer)

    create_button = st.button("Create")
    if create_button:
        generated_text = " ".join([answer.strip() for answer in user_answers if answer.strip()])
        if generated_text:
            st.write("---")
            st.markdown('<div class="subheading">Generated Text:</div>', unsafe_allow_html=True)
            st.markdown(f"<div class='result'>{generated_text}</div>", unsafe_allow_html=True)
            st.markdown(f"<div><b>Word Count:</b> {len(generated_text.split())}<div>", unsafe_allow_html=True)
        else:
            st.error("Please provide answers to the questions to generate text.")
