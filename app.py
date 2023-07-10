import streamlit as st

import datetime
import requests

'''
# Bienvenido a SIVICO y felicidades por querer ser unx Mexicanx más informadx 🤓

Nuestra herramienta es sencilla...cuéntanos en unas palabras qué es lo que te importa/preocupa/interesa, 
nosotros revisamos miles y miles de tweets, iniciativas, etc y te damos una lista de lxs senadorxs más alineados con tus intereses.

'''

with st.form(key='params_for_api'):

    user_input = st.text_area('En unas palabras, cuéntanos qué te interesa/preocupa/importa:', '''
    Para mí, lo más importante es la educación. Sin ella, creo que México tiene un futuro muy retador.
    Además de esto, también creo que la corrupción es un cáncer grave que tiene nuestro sistema político., (...)
    ''')

    st.form_submit_button('Analizar')

params = dict(
    user_input=user_input)

sivico_api_url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(sivico_api_url, params=params)

matches = response.json()

st.header(f'Estos son los senadores más parecidos a ti!')
