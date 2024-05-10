import easyocr
import streamlit as st
from dash import Dash, html, dcc, callback, Output, Input          

reader = easyocr.Reader(['en'])  
image_path = '1.png'
result = reader.readtext(image_path)
for detection in result:
    print(detection[1]) 
st.write(detection)
