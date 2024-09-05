import streamlit as st
import requests
from PIL import Image
import io

# Title of the app
st.title('Image Generation Model')

# Input from the user
input_ = st.text_input("Enter Your Prompt ! ")

# Hugging Face API URL and Token
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Ensure the user has entered a prompt before sending the request
if input_:
    try:
        # Fetching the image from the API
        image_bytes = query({
            "inputs": input_,
        })

        # Converting the image bytes to an actual image using PIL
        image = Image.open(io.BytesIO(image_bytes))

        # Displaying the image in Streamlit
        st.image(image, caption="Generated Image")

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.write("Please enter a prompt to generate an image.")
