import streamlit as st
import json
import base64
from pathlib import Path
import os
import re

@st.cache_resource()
def load_output():
    with open('custom_output.json', encoding='utf-8') as f:
        return json.load(f)
    
def render_svg(svg_file):

    with open(svg_file, "r") as f:
        lines = f.readlines()
        svg = "".join(lines)

        """Renders the given svg string."""
        b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
        return html
    
def app():
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
                margin-bottom: 1em; 
            }
            .subheading-style {
                font-size: 1.7em;
                font-weight: 700;
                color: #6A5ACD;
                margin-top: 20px;
            }
            .option-desc {
                color: #333333;
                margin-bottom: 20px;
                text-align: justify;
            }
            .trait-box {
                background-color: #f0f0f5;
                padding: 20px;
                border-radius: 20px;
                margin: 10px 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            }
            .trait-box:hover {
                transform: scale(1.03);
                box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
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
                height: max-content;
                margin: 1em 0;
                display: flex;
                flex-direction: column;
                padding: 1.5em;
                border-radius: 20px;
                box-shadow: 0 0 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            }
            .mbti-type-box:hover {
                transform: scale(1.03);
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
            }
            .mbti-upper-section {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
            }
            .mbti-lower-section {
                margin-top: 20px;
                text-align: justify;
            }
            .mbti-type-img {
                width: 100%;
                height: auto;
            }
            .mbti-type-title {
                font-weight: bold;
                font-size: 30px;
            }
            .mbti-desc {
                margin: 0.5em 0;
                text-align: justify;
            }
            .mbti-view-details {
                color: #2E86C1;
                text-decoration: none;
                font-weight: bold;
            }
                
            @media (max-width: 768px) {
                .mbti-upper-section {
                    flex-direction: column;
                    align-items: center;
                    gap: 1em;
                }

                .mbti-lower-section {
                    margin-top: 10px;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title-style">MBTI Traits & Types Overview</div>', unsafe_allow_html=True)

    # Display the options
    option = st.selectbox('Explore MBTI:', ['MBTI Traits', 'MBTI Types'])

    if option == 'MBTI Traits':
        # Display MBTI traits
        st.markdown('<div class="subheading-style">MBTI Traits</div>', unsafe_allow_html=True)
        st.markdown('<div class="option-desc">MBTI traits are the building blocks of the MBTI personality types. They are the characteristics that make up each of the 16 personality types. It assesses four key dimensions, each represented by a pair of opposing traits.</div>', unsafe_allow_html=True)

        for i in range(0, len(outputs['mbti_traits']), 2):
            col1, col2 = st.columns(2, vertical_alignment='center')
            for idx, col in enumerate((col1, col2)):
                if i + idx < len(outputs['mbti_traits']):
                    trait = outputs['mbti_traits'][i + idx]
                    col.markdown(f"<div class='trait-box' style='background-color: {trait['color']};'>"
                                    f"<div class='trait-title'>{trait['name']}</div>"
                                    f"<p class='trait-desc'>{trait['description']}</p>"
                                f"</div>", unsafe_allow_html=True)
    elif option == 'MBTI Types':
        # Display MBTI types
        st.markdown('<div class="subheading-style">MBTI Types</div>', unsafe_allow_html=True)
        st.markdown('<div class="option-desc">MBTI personality types are the result of a combination of traits. Each type is characterized by its unique set of traits and their associated strengths and weaknesses. There are 16 different types, each representing a unique combination of traits.</div>', unsafe_allow_html=True)

        for i in range(0, len(outputs['mbti_type']), 2):
            col1, col2 = st.columns(2, vertical_alignment='center')
            for idx, col in enumerate((col1, col2)):
                if i + idx < len(outputs['mbti_type']):
                    mbti_type = outputs['mbti_type'][i + idx]
                    with col:
                        col.markdown(f"<div class='mbti-type-box'>"
                                        f"<div class='mbti-upper-section'>"
                                            f"<div class='mbti-type-img'>{render_svg(mbti_type['img'])}</div>"
                                            f"<div class='mbti-type-title'>{mbti_type['type']}</div>"
                                        f"</div>"
                                        f"<div class='mbti-lower-section'>"
                                            f"<div class='mbti-desc'>{mbti_type['description']}</div>"
                                            f"<a href='{mbti_type['url']}' target='_blank' class='mbti-view-details'>View more details</a>"
                                        f"</div>"
                                    f"</div>", unsafe_allow_html=True) 