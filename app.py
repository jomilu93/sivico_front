import streamlit as st
from bs4 import BeautifulSoup
from lxml import etree
import time
import nltk
from PIL import Image

from nltk.corpus import stopwords

import requests

nltk.download('stopwords')
st.set_page_config(layout="wide")
extra_stop_words = ['México', 'sistema', 'senadores', 'aumentar', 'acceso', 'manera', 'mejorar']
stop_words = set(stopwords.words('spanish'))
stop_words.update(extra_stop_words)

logo =  Image.open('assets/Sivico_Logo.png')

col1, col2 = st.columns([0.2, 0.8])
with col1:
    st.image(logo)
with col2:
    st.markdown("<h1 style='text-align: center; color: black;'>Bienvenidx a SÍVICO y felicidades por querer <br> ser unx mexicanx más informadx y participativx <br> en nuestra democracia 🇲🇽🤓</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: left; color: black;'>¿Qué es SÍVICO? </h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left; color: black;'>SÍVICO es una herramienta de inteligencia artifical de ciudadanos para ciudadanos. Nuestro sueño es que, usando la tecnología, podamos hacer que nuestra democracia se democratice — es decir, que sea mucho más fácil de lo que es hoy ser unx ciudadanx informado y participativo. Hoy se necesitarían días de investigación sólo para saber qué hace tu senadorx...<br>\
            <br>Con Sívico, sólo necesitas unos segundos 😎 Tú nos cuentas en unas palabras qué es lo que te importa/preocupa/interesa, y nosotros revisamos miles y miles de iniciativas, propuestas, Tweets, videos de Youtube, etc y te damos una lista de lxs senadorxs más alineados con tus intereses. También, te damos información de quiénes son, qué han hecho y cómo contactarlos.\
            Hoy solamente tenemos información de Senadorxs, pero estamos trabajando duro para tener a todxs nuestrxs funcionarixs públicxs por acá muy pronto 😉</p>", unsafe_allow_html=True)
"""


"""

with st.form(key='params_for_api'):
    user_input = st.text_area('En unas palabras, cuéntanos qué te interesa/preocupa/importa:',
    '''Para mí, lo más importante es la educación. Creo que es necesario mejorar el acceso a educación de calidad.''')

    if st.form_submit_button('Analizar'):

        params = dict(user_input=user_input)

        sivico_api_url = 'https://sivico-api-prod-vbgljmfjoa-ew.a.run.app/senators'

        try:
            response = requests.get(sivico_api_url, params=params)
            response.raise_for_status()
            matches = response.json()[:3]

            with st.spinner('Revisando miles de iniciativas, propuestas, videos y Tweets publicados...'):

                time.sleep(5)

                st.header(f'Estxs son lxs senadxres que más han velado por tus intereses:')

                for senator in matches:

                    senator_id = senator['senator_id']
                    full_name = senator['senadores']
                    nombre = senator['Nombre']
                    apellidos = senator['Apellidos']
                    fraction = senator['Fraccion']
                    estado = senator['Estado']
                    email = senator["correo"]
                    telefono = senator["telefono"]
                    attendance_score = senator['attendance_score']
                    summary = senator['beto_preprocessed_summary']
                    url = f'https://www.senado.gob.mx/65/senador/{senator_id}'
                    html = requests.get(url)
                    content = BeautifulSoup(html.text, 'html.parser')
                    images = content.findAll("img")

                    if [image.attrs['src'] for image in images if "intervenciones" in image.attrs['src']]:
                        image_url = [image.attrs['src'] for image in images if "intervenciones" in image.attrs['src']][0]
                    else:
                        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Senate_Seal_%28Mexico%29.svg/1200px-Senate_Seal_%28Mexico%29.svg.png"

                    # image = f"https://www.senado.gob.mx/65/images/senadores/64/{senator_id}-{str(apellido)+'_' for apellido in appellidos.split(' ')}jose_ramon-20230307-125301.jpg"

                    #create dictionary with number of initiatives per topics
                    topics = {}
                    topics["Salud"] = len(senator['Salud_initiative_list'].split(".'")) if not senator['Salud_initiative_list'] is None or senator['Salud_initiative_list'] == "[]" else 0
                    topics["Educacion"] = len(senator['Educacion_initiative_list'].split(".'")) if not senator['Educacion_initiative_list'] is None or senator['Educacion_initiative_list'] == "[]" else 0
                    topics["Justicia"] = len(senator['Justicia_initiative_list'].split(".'")) if not senator['Justicia_initiative_list'] is None or senator['Justicia_initiative_list'] == "[]" else 0
                    topics["Gobernacion"] = len(senator['Gobernacion_initiative_list'].split(".'")) if not senator['Gobernacion_initiative_list'] is None or senator['Gobernacion_initiative_list'] == "[]" else 0
                    topics["Igualdad de genero"] = len(senator['Para_la_Igualdad_de_Genero_initiative_list'].split(".'")) if not senator['Para_la_Igualdad_de_Genero_initiative_list'] is None or senator['Para_la_Igualdad_de_Genero_initiative_list'] == "[]" else 0
                    topics["Anticorrupcion y Transparencia"] = len(senator['Anticorrupcion__Transparencia_y_Participacion_Ciudadana_initiative_list'].split(".'")) if not senator['Anticorrupcion__Transparencia_y_Participacion_Ciudadana_initiative_list'] is None or senator['Anticorrupcion__Transparencia_y_Participacion_Ciudadana_initiative_list'] == "[]" else 0
                    topics["Desarrollo urbano y vivienda"] = len(senator['Desarrollo_Urbano__Ordenamiento_Territorial_y_Vivienda_initiative_list'].split(".'")) if not senator['Desarrollo_Urbano__Ordenamiento_Territorial_y_Vivienda_initiative_list'] is None or senator['Desarrollo_Urbano__Ordenamiento_Territorial_y_Vivienda_initiative_list'] == "[]" else 0
                    topics["Defensa Nacional"] = len(senator['Defensa_Nacional_initiative_list'].split(".'")) if not senator['Defensa_Nacional_initiative_list'] is None or senator['Defensa_Nacional_initiative_list'] == "[]" else 0
                    topics["Seguridad Social"] = len(senator['Seguridad_Social_initiative_list'].split(".'")) if not senator['Seguridad_Social_initiative_list'] is None or senator['Seguridad_Social_initiative_list'] == "[]" else 0
                    topics["Derechos de Jovenes"] = len(senator['Derechos_de_la_Ninez_y_de_la_Adolescencia_initiative_list'].split(".'")) if not senator['Derechos_de_la_Ninez_y_de_la_Adolescencia_initiative_list'] is None or senator['Derechos_de_la_Ninez_y_de_la_Adolescencia_initiative_list'] == "[]" else 0
                    topics["Comunicaciones y Transporte"] = len(senator['Comunicaciones_y_Transportes_initiative_list'].split(".'")) if not senator['Comunicaciones_y_Transportes_initiative_list'] is None or senator['Comunicaciones_y_Transportes_initiative_list'] == "[]" else 0
                    topics["Economia"] = len(senator['Economia_initiative_list'].split(".'")) if not senator['Economia_initiative_list'] is None or senator['Economia_initiative_list'] == "[]" else 0
                    topics["Medio ambiente"] = len(senator['Medio_Ambiente__Recursos_Naturales_y_Cambio_Climatico_initiative_list'].split(".'")) if not senator['Medio_Ambiente__Recursos_Naturales_y_Cambio_Climatico_initiative_list'] is None or senator['Medio_Ambiente__Recursos_Naturales_y_Cambio_Climatico_initiative_list'] == "[]" else 0
                    topics["Hacienda y Credito Publico"] = len(senator['Hacienda_y_Credito_Publico_initiative_list'].split(".'")) if not senator['Hacienda_y_Credito_Publico_initiative_list'] is None or senator['Hacienda_y_Credito_Publico_initiative_list'] == "[]" else 0
                    topics["Relaciones Exteriores"] = len(senator['Relaciones_Exteriores_initiative_list'].split(".'")) if not senator['Relaciones_Exteriores_initiative_list'] is None or senator['Relaciones_Exteriores_initiative_list'] == "[]" else 0
                    topics["Agricultura, Ganaderia y Pesca"] = len(senator['Agricultura__Ganaderia__Pesca_y_Desarrollo_Rural_initiative_list'].split(".'")) if not senator['Agricultura__Ganaderia__Pesca_y_Desarrollo_Rural_initiative_list'] is None or senator['Agricultura__Ganaderia__Pesca_y_Desarrollo_Rural_initiative_list'] == "[]" else 0
                    topics["Seguridad Publica"] = len(senator['Seguridad_Publica_initiative_list'].split(".'")) if not senator['Seguridad_Publica_initiative_list'] is None or senator['Seguridad_Publica_initiative_list'] == "[]" else 0
                    topics["Reglamentos Parlamentarios"] = len(senator['Reglamentos_y_Practicas_Parlamentarias_initiative_list'].split(".'")) if not senator['Reglamentos_y_Practicas_Parlamentarias_initiative_list'] is None or senator['Reglamentos_y_Practicas_Parlamentarias_initiative_list'] == "[]" else 0
                    topics["Derechos Humanos"] = len(senator['Derechos_Humanos_initiative_list'].split(".'")) if not senator['Derechos_Humanos_initiative_list'] is None or senator['Derechos_Humanos_initiative_list'] == "[]" else 0
                    topics["Migracion"] = len(senator['Asuntos_Fronterizos_y_Migratorios_initiative_list'].split(".'")) if not senator['Asuntos_Fronterizos_y_Migratorios_initiative_list'] is None or senator['Asuntos_Fronterizos_y_Migratorios_initiative_list'] == "[]" else 0
                    topics["Ciencia y tecnologia"] = len(senator['Ciencia_y_Tecnologia_initiative_list'].split(".'")) if not senator['Ciencia_y_Tecnologia_initiative_list'] is None or senator['Ciencia_y_Tecnologia_initiative_list'] == "[]" else 0
                    topics["Energia"] = len(senator['Energia_initiative_list'].split(".'")) if not senator['Energia_initiative_list'] is None or senator['Energia_initiative_list'] == "[]" else 0
                    topics["Juventud y deporte"] = len(senator['Juventud_y_Deporte_initiative_list'].split(".'")) if not senator['Juventud_y_Deporte_initiative_list'] is None or senator['Juventud_y_Deporte_initiative_list'] == "[]" else 0
                    topics["Radio, television y cine"] = len(senator['Radio__Television_y_Cinematografia_initiative_list'].split(".'")) if not senator['Radio__Television_y_Cinematografia_initiative_list'] is None or senator['Radio__Television_y_Cinematografia_initiative_list'] == "[]" else 0
                    topics["Cultura"] = len(senator['Cultura_initiative_list'].split(".'")) if not senator['Cultura_initiative_list'] is None or senator['Cultura_initiative_list'] == "[]" else 0
                    topics["Mineria"] = len(senator['Mineria_y_Desarrollo_Regional_initiative_list'].split(".'")) if not senator['Mineria_y_Desarrollo_Regional_initiative_list'] is None or senator['Mineria_y_Desarrollo_Regional_initiative_list'] == "[]" else 0
                    topics["Obras publicas"] = len(senator['Comunicaciones_y_Obras_Publicas_initiative_list'].split(".'")) if not senator['Comunicaciones_y_Obras_Publicas_initiative_list'] is None or senator['Comunicaciones_y_Obras_Publicas_initiative_list'] == "[]" else 0
                    topics["Turismo"] = len(senator['Turismo_initiative_list'].split(".'")) if not senator['Turismo_initiative_list'] is None or senator['Turismo_initiative_list'] == "[]" else 0
                    topics["Asuntos indigenas"] = len(senator['Asuntos_Indigenas_initiative_list'].split(".'")) if not senator['Asuntos_Indigenas_initiative_list'] is None or senator['Asuntos_Indigenas_initiative_list'] == "[]" else 0
                    topics["Movilidad y zonas urbanas"] = len(senator['Zonas_Metropolitanas_y_Movilidad_initiative_list'].split(".'")) if not senator['Zonas_Metropolitanas_y_Movilidad_initiative_list'] is None or senator['Zonas_Metropolitanas_y_Movilidad_initiative_list'] == "[]" else 0
                    topics["Derecho de consumidor"] = len(senator['Defensa_de_los_Consumidores_initiative_list'].split(".'")) if not senator['Defensa_de_los_Consumidores_initiative_list'] is None or senator['Defensa_de_los_Consumidores_initiative_list'] == "[]" else 0

                    sorted_topics = sorted(topics.items(), key=lambda x:x[1], reverse=True)[:5]
                    top_5 = dict(sorted_topics)


                    with st.container():

                        col1, col2, col3, col4 = st.columns(4)

                        with col2:
                            st.subheader("Detalles de Senadorx")

                        with col3:
                            st.subheader("Top 5 temas por # de iniciativas")

                        with col4:
                            st.subheader("Contacta a tu senadorx")

                        col1.image(image_url)

                        col2.write(f"**Nombre:** {full_name}")
                        col2.write(f"**Partido:** {fraction}")
                        col2.write(f"**Estado:** {estado}")
                        col2.write(f"**% de asistencia:** {float(attendance_score)*100:.0f}%")

                        for value in top_5:
                            col3.write(f"**{value}:** {topics[value]}")

                        col4.write("**Email:**")
                        col4.write(f"{email}")
                        col4.write(f"**Telefono:** {telefono}")
                        col4.write(f"**Pagina web:**")
                        col4.write(f"https://www.senado.gob.mx/65/senador/{senator_id}")

                    with st.container():
                        with st.expander(f"Ver iniciativas propuestas por {full_name}:"):
                            for line in summary.split(". "):
                                line_words = line.split(" ")
                                user_input_words = params["user_input"].split(" ")
                                filtered_user_input = [word for word in user_input_words if word not in stop_words]
                                if len(set(line_words).intersection(filtered_user_input)) != 0:
                                    st.markdown(f'- {line}.')

        except requests.RequestException as e:
            st.error(f"Error fetching data: {e}")

