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
            .title {
                font-size: 2.5em;
                color: #4B0082;
                font-weight: 700;
            }
            .subheading-style {
                font-size: 1.5em;
                color: #6A5ACD;
                margin: 1em 0 0.5em 0;
                font-weight: 600;
            }
            .scenario {
                color: #333333;
                font-size: 1.1em;
                font-style: italic;
                margin-bottom: 20px;
                text-align: justify;
            }
            .question {
                font-size: 1em;
                margin: 1em 0;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">Create Your Text</div>', unsafe_allow_html=True)
    st.write(
        "Not sure what to write? Use these questions to create your text."
        "Once you've completed the answers, copy the generated text into the predictor to discover your MBTI personality."
    )

    question_sets_list = [ question_set for question_set in question_sets['question_sets'] ]
    options = [ option['id'] for option in question_sets_list ]
    question_set_choice = st.selectbox(
        "Choose a set of questions to get started:",
        options,
        format_func = lambda x: question_sets_list[int(x)]['name']
    )

    st.markdown('<div class="subheading-style">Answer the following questions:</div>', unsafe_allow_html=True)
    st.markdown('<div class="scenario"><b>Scenario:</b> ' + question_sets_list[int(question_set_choice)]['scenario'] + '</div>', unsafe_allow_html=True)
    user_answers = []
    for idx, question in enumerate(question_sets_list[int(question_set_choice)]['questions']):
        st.markdown(f"<div class='question'><b>Question {idx+1}:</b> {question}</div>", unsafe_allow_html=True)
        answer = st.text_area(label=question, key=idx, label_visibility='collapsed')
        user_answers.append(answer)

    combine_text_button = st.button("Combine Text")
    if combine_text_button:
        generated_text = " ".join([answer.strip() for answer in user_answers if answer.strip()])
        if generated_text:
            st.write("---")
            st.markdown('<div class="subheading-style">Generated Text:</div>', unsafe_allow_html=True)
            st.write(generated_text)
        else:
            st.error("Please provide answers to the questions to generate text.")
