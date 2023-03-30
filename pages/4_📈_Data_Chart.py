import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import base64
from pathlib import Path

st.set_page_config(page_title="Data Frame", page_icon="📈", layout="wide")

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

st.title("Data Chart")
st.sidebar.header("Data Chart")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Columna 1")
    st.write("Contenido de la columna 1")

with col2:
    st.header("Columna 2")
    st.write("Contnido de la columna 2")

with col3:
    st.header("Columna 3")
    st.write("Contenido de la columna 3")



@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Gross Agricultural Production ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )