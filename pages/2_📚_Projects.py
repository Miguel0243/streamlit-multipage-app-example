import streamlit as st
import time
import numpy as np
import base64
from pathlib import Path

st.set_page_config(page_title="Projects", page_icon="📚")

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

st.header("TEST PAGINA WEB PROJECTS")
st.title("Projects")
st.sidebar.header("Projects")
st.write("You have entered", st.session_state["my_input"])

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()