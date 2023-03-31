import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Analyse immobilière en France 2020")

st.write("## Analyse immobilière en France 2020 🏠")

st.write("# 1°) Les regions avec le plus de vente")
st.image("./images/mostVenteByRegionFig.jpeg")

st.write("# 2°) Nombre de Maison par région")
st.image("./images/Nombre de Maison par région.png")

st.write("# 3°) Les Prix moyens du mètre carré par région")
st.image("./images/Les Prix moyens du mètre carré par région.jpeg")

st.write("# 4°) Le classement des départements par la surface moyenne habitable")

st.write("Classement des 10 plus grandes surfaces par département en France")
st.image("./images/Classement des 10 plus grandes surfaces par département en France.jpeg")

st.write("Classement des 10 plus petites surfaces par département en France")
st.image("./images/Classement des 10 plus petites surfaces par département en France.jpeg")

