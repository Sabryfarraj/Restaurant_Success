import streamlit as st
import joblib
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Restaurant Success Predictor",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 20px;
        background-color: #1a1a1a;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff3333;
    }
    .success-box {
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        background-color: #28a745;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .failure-box {
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        background-color: #dc3545;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-container {
        background-color: #2c3e50;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
        color: white;
    }
    .stSelectbox {
        max-height: 200px;
        overflow-y: auto;
    }
    .stSelectbox div[role='listbox'] {
        max-height: 200px;
    }
    div[data-baseweb="select"] > div {
        background-color: #34495e;
        border-radius: 8px;
        border: 1px solid #46637f;
        color: white;
    }
    .feature-header {
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        padding-bottom: 15px;
        border-bottom: 2px solid #46637f;
        margin-bottom: 20px;
    }
    .title {
        text-align: center;
        padding: 20px;
        color: white;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #bdc3c7;
        font-size: 1.2em;
        margin-bottom: 10px;
    }
    .metrics-container {
        background-color: #34495e;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .metric-item {
        text-align: center;
        color: white;
        padding: 10px 20px;
    }
    .metric-value {
        font-size: 1.8em;
        font-weight: bold;
        color: #3498db;
    }
    .metric-label {
        font-size: 1em;
        color: #bdc3c7;
    }
    .info-cards {
        display: flex;
        justify-content: space-between;
        margin: 20px 0;
    }
    .info-card {
        background-color: #34495e;
        padding: 15px;
        border-radius: 10px;
        flex: 1;
        margin: 0 10px;
        text-align: center;
        color: white;
    }
    div.stSlider > div {
        color: white;
    }
    .stRadio > label {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the pipeline and feature configurations
pipeline = joblib.load('decision_tree_pipeline.pkl')
min_max_values = joblib.load('min_max_values.pkl')
unique_values = joblib.load('unique_values.pkl')
def prediction(book_table, location, rest_type, cuisines, approx_cost, num_cuisines):
    df = pd.DataFrame({
        'book_table': [book_table],
        'location': [location],
        'rest_type': [rest_type],
        'cuisines': [cuisines],
        'approx_cost(for two people)': [approx_cost],
        'Num_Cuisines': [num_cuisines]
    })
    return pipeline.predict(df)[0]

def main():
    # Title
    st.markdown("<div class='title'>🍽️ Restaurant Success Predictor</div>", unsafe_allow_html=True)
    
    # Info Cards instead of subtitle
    st.markdown("""
        <div class='info-cards'>
            <div class='info-card'>
                <h3>💡 AI-Powered</h3>
                <p>Advanced machine learning for accurate predictions</p>
            </div>
            <div class='info-card'>
                <h3>📊 Data-Driven</h3>
                <p>Based on real restaurant success patterns</p>
            </div>
            <div class='info-card'>
                <h3>🎯 Precise</h3>
                <p>High accuracy prediction model</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Create three columns for better layout
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-header'>📑 Basic Information</div>", unsafe_allow_html=True)
        book_table_options = unique_values['book_table']
        book_table = st.radio("Table Booking Available", book_table_options, horizontal=True)
        location = st.selectbox(
            "📍 Location", 
            unique_values['location'],
            help="Select the restaurant location"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-header'>🍳 Restaurant Details</div>", unsafe_allow_html=True)
        rest_type = st.selectbox(
            "🏪 Restaurant Type", 
            unique_values['rest_type'],
            help="Choose your restaurant type"
        )
        cuisines = st.selectbox(
            "🥘 Primary Cuisine", 
            unique_values['cuisines'],
            help="Select your main cuisine type"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='feature-container'>", unsafe_allow_html=True)
        st.markdown("<div class='feature-header'>💰 Cost & Variety</div>", unsafe_allow_html=True)
        approx_cost_min, approx_cost_max = min_max_values['approx_cost(for two people)']
        approx_cost = st.slider(
            "💵 Approximate Cost (for two)", 
            min_value=approx_cost_min, 
            max_value=approx_cost_max, 
            value=(approx_cost_min + approx_cost_max) // 2, 
            step=100
        )
        
        num_cuisines_min, num_cuisines_max = min_max_values['Num_Cuisines']
        num_cuisines = st.select_slider(
            "🍽️ Number of Cuisines",
            options=range(num_cuisines_min, num_cuisines_max + 1),
            value=num_cuisines_min
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Centered predict button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        predict_button = st.button("🔮 Predict Success")

    if predict_button:
        result = prediction(book_table, location, rest_type, cuisines, approx_cost, num_cuisines)
        
        st.markdown("<div style='text-align: center; margin-top: 30px;'>", unsafe_allow_html=True)
        if result == 1:
            st.markdown("""
                <div class='success-box'>
                    <h2 style='margin:0;'>🎉 Success Predicted!</h2>
                    <p style='margin:10px 0 0 0;'>Based on our analysis, your restaurant has a strong potential for success. 
                    The combination of location, cuisine, and other factors appears favorable.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class='failure-box'>
                    <h2 style='margin:0;'>⚠️ Caution Advised</h2>
                    <p style='margin:10px 0 0 0;'>Our analysis suggests some potential challenges , your restaurant has a strong potential for failure. 
                    Consider adjusting factors like location, cost, or cuisine type to improve success chances.</p>
                </div>
            """, unsafe_allow_html=True)

    # Model Metrics
    st.markdown("""
        <div class='metrics-container'>
            <div class='metric-item'>
                <div class='metric-value'>91.53%</div>
                <div class='metric-label'>Accuracy</div>
            </div>
            <div class='metric-item'>
                <div class='metric-value'>91.74%</div>
                <div class='metric-label'>Precision</div>
            </div>
            <div class='metric-item'>
                <div class='metric-value'>91.07%</div>
                <div class='metric-label'>Recall</div>
            </div>
            <div class='metric-item'>
                <div class='metric-value'>91.40%</div>
                <div class='metric-label'>F1 Score</div>
            </div>
        </div>
        
        <div style='text-align: center; color: #bdc3c7; padding: 10px;'>
            * These metrics are based on our model's performance on test data
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px; color: #bdc3c7; font-size: 14px; margin-top: 40px;'>
            Made with ❤️ for Restaurant Entrepreneurs | © 2024
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()