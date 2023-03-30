import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Data Frame", page_icon="📊", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 

logo_url = "images/reynosa_logo1.png"
logo = f"url(data:image/png;base64,{base64.b64encode(Path(logo_url).read_bytes()).decode()})"

st.markdown(
         f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: {logo};
                background-repeat: no-repeat;
                padding-top: height - 40px;
                background-position: 20px 20px;
                background-size: 80%;
            }}
        </style>
        """,
        unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Resumen de Vo. Bo.")
    st.write("Contenido de la columna 1")
    
with col2:
    st.header("Proyectos en Proceso")
    st.write("Contnido de la columna 2")

with col3:
    st.header("Ultimas Notas en Bitacora")
    st.write("Contenido de la columna 3")

