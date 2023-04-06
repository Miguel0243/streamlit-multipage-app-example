import streamlit as st
from urllib.error import URLError
import base64
from pathlib import Path
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Frame", page_icon="📈", layout="wide")

page_bg_image = """
    <style>
        [data-testid="stAppViewContainer"]{
            background-color: #F5E2E2;
            background-size:cover;
        }

        [data-testid="stHeader"]{
            background-color: rgba(0,0,0,0);
        }
    </style>
"""

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
    st.markdown(page_bg_image,unsafe_allow_html=True)

logo_url = "images/reynosa_logo1.png"
logo = f"url(data:image/png;base64,{base64.b64encode(Path(logo_url).read_bytes()).decode()})"

bg = "images/cultural1.jpg"
bg1 = f"url(data:image/png;base64,{base64.b64encode(Path(bg).read_bytes()).decode()})"

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

            [data-testid="stAppViewContainer"]{{
                background-color: #F5E2E2;
                background-image: {bg1};
                background-size:cover;
                background-position: center;
        }} 
        </style>
        """,
        unsafe_allow_html=True,
)

col1, col2 = st.columns([1,2])
proyecto = "Repavimentacion Avenida Principal"
contratista = "Nombre Contratista"
contrato = "OP12-REY-2433"
objeto = "Repavimentacion de carpeta asfaltica de la avenida principal"

with col1:
        st.subheader("Proyecto #5")
        st.caption("Fecha: 04/06/2023")
        st.write("**Proyecto:** ", proyecto)
        st.write("**Contratista:** ", contratista)
        st.write("**N° Contrato:** ", contrato)
        st.write("**Objeto de Contrato:** ", objeto)

        col3, col4 = st.columns(2)
        with col3:
            st.button("Modificar", use_container_width=True)
        with col4:
            st.button("Eliminar", use_container_width=True)

with col2:
    st.subheader("Bitacora del Proyecto")
    col5, col6 = st.columns(2)
    with col5:
        st.button("Nueva Nota", use_container_width=True)
    with col6:
         st.button("Archivos", use_container_width=True)
    df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=('Fecha','Nota','Estatus'))
    hide_index = """
        <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
        </style>
    """
    st.markdown(hide_index,unsafe_allow_html=True)
    
    st.table(df)