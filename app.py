# importar streamlit
import streamlit as st 
import pandas as pd
from PIL import Image
import plotly.express as px

img = Image.open('assets/imagen.png')
st.set_page_config('MPAD M8', 
                   page_icon=img, 
                   layout='wide',
                   initial_sidebar_state='collapsed')

def main():
    st.title("Personalizando mi aplicacion")
    st.sidebar.header('Mi menú')

    df = pd.read_csv('data/match_result.csv')

    st.dataframe(df)

    df_count = df.groupby('tournament').count().reset_index()

    fig = px.pie(df_count, values='country', title='paises por torneos')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()