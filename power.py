import streamlit as st
import pandas as pd
import joblib

# Load the model
try:
    model = joblib.load('consumer.joblib')
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Streamlit app title
st.title("Power Consumption Prediction")

# Input fields for features
st.sidebar.header("Input Features")
temperature = st.sidebar.number_input("Temperature", value=20.0)
humidity = st.sidebar.number_input("Humidity", value=50.0)
wind_speed = st.sidebar.number_input("Wind Speed", value=10.0)
general_diffuse_flows = st.sidebar.number_input("General Diffuse Flows", value=0.5)
diffuse_flows = st.sidebar.number_input("Diffuse Flows", value=0.5)

# Create a DataFrame from the input features
input_data = pd.DataFrame({
    'Temperature': [temperature],
    'Humidity': [humidity],
    'WindSpeed': [wind_speed],
    'GeneralDiffuseFlows': [general_diffuse_flows],
    'DiffuseFlows': [diffuse_flows]
})

# Make predictions
if st.sidebar.button("Predict"):
    try:
        predictions = model.predict(input_data)
        st.write("### Predictions:")
        st.write(f"Power Consumption Zone 1: {predictions[0][0]:.2f}")
        st.write(f"Power Consumption Zone 2: {predictions[0][1]:.2f}")
        st.write(f"Power Consumption Zone 3: {predictions[0][2]:.2f}")
    except Exception as e:
        st.error(f"Error making predictions: {e}")