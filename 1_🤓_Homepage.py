import streamlit as st
from PIL import Image
import base64
from pathlib import Path

st.set_page_config(
    page_title="Home",
    page_icon="👋", initial_sidebar_state="expanded", layout="wide"
)

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

st.markdown("# Home")
st.title("Main Page")
st.header("This is the header")
st.subheader("This is the subheader")
st.text("Hello this is a web page")

st.success("Executed succesfully")
st.info("This is an information")
st.warning("This is a warning")
st.error("An error occured")

st.write("I'm writing this sample code")
st.write(range(20))
channel = "Mike123coding"
st.write("Subscribe to", channel)

st.sidebar.success("Navega a traves del menú superior.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

code_body = '''for i range (10):
    print (i)'''    
st.code(code_body,language="python")

if(st.checkbox("Accept")):
    st.text("You aggreed the condition")

val = st.radio("Select a languaje", ('pthon','java'))
st.write(val," was selected")

img = Image.open("images/refresh.png")
st.image(img)

option = st.selectbox("Select an option",['python','java','react','node','sql'])
st.write("You have selected:",option)

options = st.multiselect("Select multiple options",['python','java','node','react','sql'])

sla = st.slider("Your Salary",1000,5000)
st.write("Your salary is ",sla)