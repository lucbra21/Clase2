# importar streamlit
import streamlit as st 
import pandas as pd
from PIL import Image

img = Image.open('assets/imagen.png')
st.set_page_config('MPAD M8', 
                   page_icon=img, 
                   layout='wide',
                   initial_sidebar_state='collapsed')

def main():
    st.title("Personalizando mi aplicacion")
    st.sidebar.header('Mi menú')
    

if __name__ == "__main__":
    main()