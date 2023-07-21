import streamlit as st

import datetime
import requests

'''
# Bienvenido a SIVICO y felicidades por querer ser unx Mexicanx más informadx 🤓

Nuestra herramienta es sencilla...cuéntanos en unas palabras qué es lo que te importa/preocupa/interesa,
nosotros revisamos miles y miles de tweets, iniciativas, etc y te damos una lista de lxs senadorxs más alineados con tus intereses.

'''

with st.form(key='params_for_api'):
    user_input = st.text_area('En unas palabras, cuéntanos qué te interesa/preocupa/importa:',
    '''Para mí, lo más importante es la educación. Sin ella, creo que México tiene un futuro muy retador. Además de esto, también creo que la corrupción es un cáncer grave que tiene nuestro sistema político., (...)''')

    if st.form_submit_button('Analizar'):
        params = dict(user_input=user_input)

        sivico_api_url = 'https://sivico-api-prod-vbgljmfjoa-ew.a.run.app/senators'

        try:
            response = requests.get(sivico_api_url, params=params)
            response.raise_for_status()
            matches = response.json()
            st.header(f'Estos son los senadores más parecidos a ti!')

            for senator in matches:
                full_name = f"{senator['Nombre']} {senator['Apellidos']}"
                fraction = senator['Fraccion']
                similarity = senator['similarity_score']

                st.write(f"**Nombre:** {full_name}")
                st.write(f"**Partido:** {fraction}")
                st.write(f"**Puntaje de similitud:** {similarity:.2f}")
                st.write("---")
        except requests.RequestException as e:
            st.error(f"Error fetching data: {e}")

