import streamlit as st
import streamlit.components.v1 as components
from lib import render_tone, initial_text, hide_streamlit_style, tonality_style

st.set_page_config(page_title="Tonality")
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Tonality")
st.info("ℹ️ A web app that takes in textual input and detects the tone of the composite sentences. Shades of red predict casual text, while shades of blue predict formal.")
st.markdown("---")


text = st.sidebar.text_area(
    "Input text", help="Specify the input in order for the classifer to detect tonality", value=initial_text)

output = ""
with st.spinner("processing text..."):
    output = render_tone(text)

content = tonality_style + '<main>' + output + '</main>'
st.markdown(content, unsafe_allow_html=True)
# components.html(output, scrolling=True, height=700)
