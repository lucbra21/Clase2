# importar streamlit
import streamlit as st 
import pandas as pd
from PIL import Image

df = pd.read_csv('data/match_result.csv')

def main():
    st.title("Trabajando con componentes")

    posicion = st.selectbox('Seleccione una posición', 
                 ['Portero','Defensa','Mediocampista','Delante']
                 )
    st.write(f"La posición seleccionada es: {posicion}")

    opciones = st.multiselect('Seleccione una posición', 
                 ['Portero','Defensa','Mediocampista','Delante']
                 )
    st.write(f"Las opciones seleccionadas son: {opciones}")

    edad = st.slider('Seleccione su edad',
                min_value = 1,
                max_value = 100,
                value = 20,
                step = 1
                )
    st.write(f"Su edad es: {edad}")

    nivel = st.select_slider(
        'Seleccione su nivel',
        options = ['Muy bajo','Bajo','Medio','Alto','Muy alto'],
    )
    st.write(f"Su nivel es: {nivel}")

    opc = st.radio('seleccione una opcion',['Portero','Defensa','Mediocampista','Delante'])
    st.write(f"Su opción es: {opc}")

    check = st.checkbox("Acepto las condiciones")
    if check:
        st.write("Aceptaste las condiciones")
    else:
        st.write("No aceptaste las opciones")

    rta = st.button('Hola lucas')
    if rta:
        st.write("Que haces lucas?")
        st.write(rta)
    else:
        st.write("-")
        st.write(rta)
    
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


if __name__ == "__main__":
    main()