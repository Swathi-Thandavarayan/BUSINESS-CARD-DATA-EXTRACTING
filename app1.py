import easyocr
import streamlit as st
from dash import Dash, html, dcc, callback, Output, Input          

reader = easyocr.Reader(['en'])  
image_path = '1.png'
result = reader.readtext(image_path)
for detection in result:
    st.write(detection[1]) 

st.write('detection')


uploaded_files = st.file_uploader(
    "Choose a file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

    if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
