
import streamlit as st
import pickle

# Load the model
with open('sentiment_pipeline.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit app title
st.title("Sentiment Analysis App")

# Text input for user to enter a sentence
user_input = st.text_input("Enter a sentence:")

# Predict sentiment when user inputs text
if user_input:
    prediction = loaded_model.predict([user_input])[0]
    st.write("Prediction:", "Positive" if prediction == 1 else "Negative")
