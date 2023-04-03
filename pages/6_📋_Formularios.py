import streamlit as st
from PIL import Image
import base64
from pathlib import Path

st.set_page_config(page_title="Formularios", page_icon="📋", layout="wide")
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

tabs = """
        <style>
        [data-baseweb="tab"]{
            background-color: transparent;
        }
"""

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 
    st.markdown(page_bg_image,unsafe_allow_html=True)
    st.markdown(tabs, 
    unsafe_allow_html=True)

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

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

tab1,tab2,tab3,tab4,tab5 = st.tabs(['General','Contratista','Supervisor de Obra','Responsable Subsecretaria de Obras Publicas','Responsable Director Supervision de Obras'])

with tab1:
    col4, col5 = st.columns(2)
    with col4:
        my_input = st.text_input("Proyecto", st.session_state["my_input"],placeholder="Ingresa el nombre del proyecto")
        my_input1 = st.text_input("N° Contrato", st.session_state["my_input"], placeholder="Ingresa el numero del contrato")
        my_input2 = st.text_area("Objeto", st.session_state["my_input"], placeholder="Ingresa el objeto del contrato")
        my_input3 = st.number_input("Importe"), st.session_state["my_input"]
    
    with col5:
        col6, col7 = st.columns(2)
        with col6:
            my_input4 = st.date_input("Fecha")
        with col7:
            my_input5 = st.date_input("Corte para Estimacion")
        
        my_input6 = st.text_input("Plazo", st.session_state["my_input"],placeholder="Ingresa el plazo de ejecucion")

        col8, col9 = st.columns(2)
        with col8:
            my_input7 = st.date_input("Inicio")
        with col9:
            my_input8 = st.date_input("Apertura")
        
    submit = st.button("Submit")

    if submit:
        sesion = st.session_state["my_input"]
        st.write(my_input)

with tab2:
    sesion1 = st.session_state["my_input"]
    st.write(sesion1)

    