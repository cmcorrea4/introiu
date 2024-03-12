import streamlit as st
from PIL import Image

st.title(" Aplicaciones para Ciudades Inteligentes")

st.header("En este espacio podrás obtener información de tu ciudad.")

image = Image.open('imagenci.jpg')
st.image(image, caption='Inteligencia Urbana')
st.write("Enlace para mi sistema de internet de las cosas")
st.write("Ingresa al link [link](https://demo.thingsboard.io/dashboards/9a61e170-565c-11ee-b6bf-f9525dc44ab3)")
