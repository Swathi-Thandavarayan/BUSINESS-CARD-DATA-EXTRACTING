import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

# Image processing function
def preprocess_image(image):
    # Convert PIL image to OpenCV format (numpy array)
    open_cv_image = np.array(image)
    # Convert RGB to BGR (as OpenCV uses BGR by default)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    # Resize the image to improve OCR readability
    open_cv_image = cv2.resize(open_cv_image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding (binarization)
    _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    
    return thresh_image

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    # Save preprocessed image to a temporary file
    cv2.imwrite("temp_preprocessed_image.png", preprocessed_image)
    # Initialize the easyocr reader
    reader = easyocr.Reader(['en'])
    # Perform OCR on the preprocessed image
    result = reader.readtext("temp_preprocessed_image.png")
    # Display OCR results
    st.write("OCR Results:")
    for detection in result:
        st.write(detection[1])  # Display detected text

    st.write('Detection completed.')
