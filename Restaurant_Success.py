import streamlit as st
import joblib
import pandas as pd

# Load the pipeline and feature configurations
pipeline = joblib.load('decision_tree_pipeline.pkl')
min_max_values = joblib.load('min_max_values.pkl')
unique_values = joblib.load('unique_values.pkl')

def get_signature_options(number_of_signature_features):
    all_signature_features = unique_values['your_signature_features']
    
    if isinstance(all_signature_features, list):
        feature_list = all_signature_features
    else:
        feature_list = [feature.strip() for feature in all_signature_features.split(",")]
    
    if number_of_signature_features < 1 or number_of_signature_features > 7:
        return []
    
    filtered_options = []
    
    for feature in feature_list:
        comma_count = feature.count(',')
        total_items = comma_count + 1
        
        if total_items == number_of_signature_features:
            filtered_options.append(feature)
    
    if number_of_signature_features == 1:
        filtered_options = [feature for feature in filtered_options if ',' not in feature]

    return filtered_options

def prediction(book_table, location, rest_type, chosen_signature_features, cuisines, approx_cost, number_of_signature_features):
    # Create a DataFrame for the input features
    df = pd.DataFrame({
        'book_table': [book_table],
        'location': [location],
        'rest_type': [rest_type],
        'your_signature_features': [', '.join(chosen_signature_features)],
        'cuisines': [cuisines],
        'approx_cost(for two people)': [approx_cost],
        'number_of_signature_features': [number_of_signature_features]  # Include this line
    })
    
    # Use the pipeline to make a prediction
    result = pipeline.predict(df)
    
    return result[0]

def main():
    st.title("Restaurant Success Prediction")
    st.markdown("""
    Welcome to the Restaurant Success Prediction app! 🍽️
    
    This application predicts the success of a restaurant based on various input features. 
    Use the controls below to provide the input data and click the "Get Prediction" button to get the estimate.
    """)

    # Use unique values for book_table
    book_table_options = unique_values['book_table']  # Assuming this is in the unique_values
    book_table = st.radio("Book Table", book_table_options)
    
    location = st.selectbox("Location", unique_values['location'])  
    rest_type = st.selectbox("Restaurant Type", unique_values['rest_type'])  

    # Get min and max values for approx_cost from min_max_values
    approx_cost_min, approx_cost_max = min_max_values['approx_cost(for two people)']
    approx_cost = st.slider("Approximate Cost (for two people)", min_value=approx_cost_min, max_value=approx_cost_max, value=(approx_cost_min + approx_cost_max) // 2, step =10)

    # Set number of signature features using min and max from unique_values
    number_of_signature_features = st.number_input("Number of Signature Features", min_value=1, max_value=7, value=1)
    selected_signature_features = get_signature_options(number_of_signature_features)

    chosen_signature_features = st.selectbox("Select Signature Feature", selected_signature_features)
    
    cuisines = st.selectbox("Cuisines", unique_values['cuisines'])  

    if st.button("Predict"):
        result = prediction(book_table, location, rest_type, [chosen_signature_features], cuisines, approx_cost, number_of_signature_features)
        
        if result == 1:
            st.success("The restaurant is likely to succeed! 🎉")
        else:
            st.error("The restaurant is likely to fail. 🚫")

if __name__ == "__main__":
    main()