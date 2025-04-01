import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define Prompt Template
prompt = PromptTemplate(
    template="Convert this image into Ghibli studio art \n {image}",
    input_variables=["image"]
)

# Streamlit UI
st.title("🎨 AI-Powered Ghibli Art Converter By Bantee Sharma")
st.write("Upload images, and AI will generate Ghibli-style versions!")

# Upload multiple images
uploaded_files = st.file_uploader("📂 Browse Images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Display default image **after** the upload button
default_image_path = "IMG_20250329_1432297.jpg"  # Replace with your image path
default_image = Image.open(default_image_path)
st.image(default_image, use_column_width=True)

# Process uploaded images
if uploaded_files:
    for uploaded_file in uploaded_files:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption=f"📸 Uploaded Image: {uploaded_file.name}", use_column_width=True)

        # Convert image to bytes
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes = image_bytes.getvalue()

        # Process with LangChain & Gemini
        chain = prompt | model
        response = chain.invoke({"image": image_bytes})

        # Display AI-generated result
        st.write(f"### 🎨 AI-Generated Ghibli Art for {uploaded_file.name}:")
        st.write(response)
