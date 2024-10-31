# importar streamlit
import streamlit as st 
import pandas as pd
from PIL import Image

def main():
    st.title("Trabajando con multimedia")

    # img = Image.open("assets/imagen.png")
    # img="https://sportsdatacampus.com/wp-content/uploads/2021/07/Sports-Data-Campus-Logo-e1625734322671.png"
    # st.image(img, use_column_width=False)
    # with open('assets/video.mp4','rb') as video_file:
    #     st.video(video_file, start_time=0)
    # with open('assets/audio.mp3','rb') as audio_file:
    #      st.audio(audio_file, start_time=0)

    st.html(
        "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
    )

if __name__ == "__main__":
    main()