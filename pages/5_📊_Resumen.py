import streamlit as st
import base64
from pathlib import Path
import matplotlib.pyplot as plt

st.set_page_config(page_title="Resumen", page_icon="📊", layout="wide")

page_bg_image = f"""
    <style>
        [data-testid="stHeader"]{{
            background-color: rgba(0,0,0,0);
        }}
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

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Resumen de Vo. Bo.")
    st.subheader("75%")
    with st.container():
        labels = ["Pendientes","Auorizados"]
        sizes = [30,70]
        colors = ['#d3d3d3','#9c1c3c']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')

        st.pyplot(fig1)

    with st.container():
        st.write("---")
        st.button("Pendiente de Autorizar", use_container_width=True)
        
with col2:
    st.header("Proyectos en Proceso")
    st.subheader("Total: " + str(4))
    st.button("Nuevo")
    st.markdown("\n\n---")


with col3:
    st.header("Ultimas Notas en Bitacora")
    st.subheader("Total: " + str(7))
    mi_lista = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
    for element in mi_lista:
        st.write("Contratista"+" - "+"Fecha")
        st.caption("Texto de obra")
