# importar streamlit
import streamlit as st 
import pandas as pd
from PIL import Image

def main():
    st.title("Mi primera app en Streamlit")
    st.header("este es el header")
    st.subheader("este es el subheader")
    st.text("esto es un texto")
    nombre = 'mundo'
    st.text(f"hola {nombre}")
    nombre = 'lucas'
    st.text("hola " + nombre)
    st.markdown("# Esto es un markdown 1")
    st.markdown("## Esto es un markdown 2")
    st.markdown("### Esto es un markdow 3")
    st.markdown("#### Esto es un markdown 4")
    st.markdown("Esto es un markdown 0")
    st.success("mensaje de éxito")
    st.error("mensaje de error")
    st.warning("mensaje de advertencia")
    st.info("informacion")
    st.exception("mensaje control de excepciones")
    st.text("esto es un texto")

    st.write("el texto que queremos")
    st.write("### el texto que queremos")
    st.write(1 + 3)

if __name__ == "__main__":
    main()