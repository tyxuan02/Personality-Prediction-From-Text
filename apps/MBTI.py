import streamlit as st
import json
import base64

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

    st.markdown("""
        <style>
            /* Global Styles */
            .stApp {
                background: linear-gradient(135deg, #f5f7fa 0%, #f8f9fa 100%);
            }
            
            button[title="View fullscreen"] {
                visibility: hidden;
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

            /* Subheading Styling */
            .subheading {
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
                
            /* Description Text */
            .option-desc {
                margin-bottom: 30px;
                text-align: justify;
                line-height: 1.6;
                font-size: 1.1em;
                animation: fadeIn 1s ease-in;
            }
            
            /* Trait Box Styling */
            .trait-box {
                background-color: #f0f0f5;
                padding: 25px;
                border-radius: 20px;
                margin: 15px 0;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }

            .trait-box:hover {
                transform: translateY(-8px);
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
            }

            .trait-box::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
                opacity: 0;
                transition: opacity 0.3s ease;
            }

            .trait-box:hover::before {
                opacity: 1;
            }
            
            .trait-title {
                word-wrap: break-word;
                font-weight: bold;
                font-size: 1.3em;
                color: #ffffff;
                margin-bottom: 15px;
                position: relative;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            }
                
            .trait-desc {
                text-align: justify;
                color: #ffffff;
            }
                
            /* MBTI Type Box Styling */
            .mbti-type-box {
                height: max-content;
                margin: 15px 0;
                padding: 2em;
                border-radius: 20px;
                background: white;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                animation: slideUp 0.6s ease-out forwards;
            }

            .mbti-type-box:hover {
                transform: translateY(-8px);
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
            }

            /* MBTI Type Sections */
            .mbti-upper-section {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 20px;
            }

            .mbti-lower-section {
                margin-top: 25px;
                padding-top: 20px;
                border-top: 2px solid #f0f0f5;
            }

            /* MBTI Type Image */
            .mbti-type-img {
                width: 100%;
                height: auto;
                transition: transform 0.3s ease;
            }

            .mbti-type-box:hover .mbti-type-img {
                transform: scale(1.05);
            }

            /* MBTI Type Title */
            .mbti-type-title {
                font-weight: bold;
                font-size: 2em;
                color: #4B0082;
                margin-left: 20px;
                background: linear-gradient(120deg, #4B0082, #6A5ACD);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            /* MBTI Description */
            .mbti-desc {
                margin: 0.8em 0;
                text-align: justify;
                line-height: 1.6;
                color: #2C3E50;
            }

            /* View Details Link */
            .mbti-view-details {
                text-decoration: none;
                display: inline-block;
                transition: all 0.3s ease;
            }

            .mbti-view-details:hover {
                transform: translateY(-2px);
            }
                
            /* Selectbox Styling */
            .stSelectbox {
                margin-bottom: 30px;
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
                    transform: translateY(30px);
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

                .subheading {
                    font-size: 1.5em;
                }

                .option-desc {
                    font-size: 1em;
                    text-align: left;
                }

                .trait-title {
                    font-size: 1.2em;
                }

                .trait-desc {
                    font-size: 1em;
                    text-align: left;
                }

                .mbti-upper-section {
                    flex-direction: column;
                    align-items: center;
                    gap: 1.5em;
                    text-align: center;
                }

                .mbti-type-title {
                    margin-left: 0;
                    margin-top: 10px;
                }

                .mbti-type-box {
                    padding: 1.5em;
                }

                .trait-box {
                    padding: 20px;
                }

                .mbti-lower-section {
                    margin-top: 15px;
                    padding-top: 15px;
                }

                .mbti-desc {
                    font-size: 1em;
                    text-align: left;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">MBTI Traits & Types Overview</div>', unsafe_allow_html=True)

    option = st.selectbox('Explore MBTI:', ['MBTI Traits', 'MBTI Types'])
    if option == 'MBTI Traits':
        st.markdown('<div class="subheading">MBTI Traits</div>', unsafe_allow_html=True)
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
        st.markdown('<div class="subheading">MBTI Types</div>', unsafe_allow_html=True)
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