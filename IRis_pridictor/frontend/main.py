import streamlit as st 
import requests
import os 


API_URL = os.getenv("API_URL","http://backend:8000/predict")

st.title("🌸 Iris Flower Prediction")

st.markdown("Enter the features of the iris flower to get the predicted species.")

# Input fields for all four iris features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

if st.button("Predict"):
    input_data = {
        "sepal_length": sepal_length,
        "petal_width": petal_width
    }
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            prediction = response.json()
            confidence_percentage = round(prediction["confidence"] * 100, 2)
            st.success(f"🌼 Predicted Iris: **{prediction['predicted_iris']}** "
                       f"(Confidence: {confidence_percentage}%)")
            st.write("Class Probabilities:")
            for species, prob in prediction["class_probabilities"].items():
                st.write(f"- {species}: {prob * 100:.2f}%")
        else:
            st.error(f"API Error: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")