# importar streamlit
import streamlit as st 
import pandas as pd
from PIL import Image

df = pd.read_csv('data/match_result.csv')

def main():
    st.title("Trabajando con datos en Streamlit")
    st.header("Usando dataframe")
    st.dataframe(df)
    st.header("Usando table")
    st.table(df)

    st.header("Visualizando json")
    st.json({"clave":"valor"})

    codigo = """
    def saludando(nombre):
        print("Hola " + nombre)

    """
    st.code(codigo, language="python")

if __name__ == "__main__":
    main()