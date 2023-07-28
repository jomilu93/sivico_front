import streamlit as st

import datetime
import requests

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>Bienvenido a SIVICO y felicidades por querer <br> ser unx Mexicanx más informadx 🇲🇽🤓</h1>", unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: white;'>¡Nuestra herramienta es muy fácil de usar!<br>Cuéntanos en unas palabras qué es lo que te importa/preocupa/interesa,\
<br>nosotros revisamos miles y miles de iniciativas, videos de Youtube, etc <br> y te damos una lista de lxs senadorxs más alineados con tus intereses.</h3>", unsafe_allow_html=True)

"""



"""

with st.form(key='params_for_api'):
    user_input = st.text_area('En unas palabras, cuéntanos qué te interesa/preocupa/importa:',
    '''Para mí, lo más importante es la educación. Sin ella, creo que México tiene un futuro muy retador. Además de esto, también creo que la corrupción es un cáncer grave que tiene nuestro sistema político. (...)''')

    if st.form_submit_button('Analizar'):
        params = dict(user_input=user_input)

        sivico_api_url = 'http://127.0.0.1:8000/senators'

        try:
            response = requests.get(sivico_api_url, params=params)
            response.raise_for_status()
            matches = response.json()['beto']
            st.header(f'Estos son los senadores más parecidos a ti!')
            
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("Detalles de Senadorx")

            with col2:
                st.subheader("Top 5 temas por # de iniciativas")

            with col3:
                st.subheader("Contacta a tu senadorx")
            
            # st.write("---")

            for senator in matches:
                                                
                senator_id = senator['senator_id']
                full_name = senator['senadores']
                fraction = senator['Fraccion']
                estado = senator['Estado']
                email = senator["correo"]
                telefono = senator["telefono"]
                similarity = senator['similarity_score']
                attendance_score = senator['attendance_score']
                
                #create dictionary with number of initiatives per topic
                topics = {}
                topics["Salud"] = len(senator['Salud_initiative_list'].split("', '")) if not senator['Salud_initiative_list'] is None or senator['Salud_initiative_list'] == "set()" else 0           
                topics["Educacion"] = len(senator['Educación_initiative_list'].split("', '")) if not senator['Educación_initiative_list'] is None or senator['Educación_initiative_list'] == "set()" else 0
                topics["Justicia"] = len(senator['Justicia_initiative_list'].split("', '")) if not senator['Justicia_initiative_list'] is None or senator['Justicia_initiative_list'] == "set()" else 0
                topics["Gobernacion"] = len(senator['Gobernación_initiative_list'].split("', '")) if not senator['Gobernación_initiative_list'] is None or senator['Gobernación_initiative_list'] == "set()" else 0
                topics["Igualdad de genero"] = len(senator['Para_la_Igualdad_de_Género_initiative_list'].split("', '")) if not senator['Para_la_Igualdad_de_Género_initiative_list'] is None or senator['Para_la_Igualdad_de_Género_initiative_list'] == "set()" else 0
                topics["Anticorrupcion y Transparencia"] = len(senator['Anticorrupción__Transparencia_y_Participación_Ciudadana_initiative_list'].split("', '")) if not senator['Anticorrupción__Transparencia_y_Participación_Ciudadana_initiative_list'] is None or senator['Anticorrupción__Transparencia_y_Participación_Ciudadana_initiative_list'] == "set()" else 0
                topics["Desarrollo urbano y vivienda"] = len(senator['Desarrollo_Urbano__Ordenamiento_Territorial_y_Vivienda_initiative_list'].split("', '")) if not senator['Desarrollo_Urbano__Ordenamiento_Territorial_y_Vivienda_initiative_list'] is None or senator['Desarrollo_Urbano__Ordenamiento_Territorial_y_Vivienda_initiative_list'] == "set()" else 0
                topics["Defensa Nacional"] = len(senator['Defensa_Nacional_initiative_list'].split("', '")) if not senator['Defensa_Nacional_initiative_list'] is None or senator['Defensa_Nacional_initiative_list'] == "set()" else 0
                topics["Seguridad Social"] = len(senator['Seguridad_Social_initiative_list'].split("', '")) if not senator['Seguridad_Social_initiative_list'] is None or senator['Seguridad_Social_initiative_list'] == "set()" else 0
                topics["Derechos de Jovenes"] = len(senator['Derechos_de_la_Niñez_y_de_la_Adolescencia_initiative_list'].split("', '")) if not senator['Derechos_de_la_Niñez_y_de_la_Adolescencia_initiative_list'] is None or senator['Derechos_de_la_Niñez_y_de_la_Adolescencia_initiative_list'] == "set()" else 0
                topics["Comunicaciones y Transporte"] = len(senator['Comunicaciones_y_Transportes_initiative_list'].split("', '")) if not senator['Comunicaciones_y_Transportes_initiative_list'] is None or senator['Comunicaciones_y_Transportes_initiative_list'] == "set()" else 0
                topics["Economia"] = len(senator['Economía_initiative_list'].split("', '")) if not senator['Economía_initiative_list'] is None or senator['Economía_initiative_list'] == "set()" else 0         
                topics["Medio ambiente"] = len(senator['Medio_Ambiente__Recursos_Naturales_y_Cambio_Climático_initiative_list'].split("', '")) if not senator['Medio_Ambiente__Recursos_Naturales_y_Cambio_Climático_initiative_list'] is None or senator['Medio_Ambiente__Recursos_Naturales_y_Cambio_Climático_initiative_list'] == "set()" else 0
                topics["Hacienda y Credito Publico"] = len(senator['Hacienda_y_Crédito_Público_initiative_list'].split("', '")) if not senator['Hacienda_y_Crédito_Público_initiative_list'] is None or senator['Hacienda_y_Crédito_Público_initiative_list'] == "set()" else 0
                topics["Relaciones Exteriores"] = len(senator['Relaciones_Exteriores_initiative_list'].split("', '")) if not senator['Relaciones_Exteriores_initiative_list'] is None or senator['Relaciones_Exteriores_initiative_list'] == "set()" else 0
                topics["Agricultura, Ganaderia y Pesca"] = len(senator['Agricultura__Ganadería__Pesca_y_Desarrollo_Rural_initiative_list'].split("', '")) if not senator['Agricultura__Ganadería__Pesca_y_Desarrollo_Rural_initiative_list'] is None or senator['Agricultura__Ganadería__Pesca_y_Desarrollo_Rural_initiative_list'] == "set()" else 0
                topics["Seguridad Publica"] = len(senator['Seguridad_Pública_initiative_list'].split("', '")) if not senator['Seguridad_Pública_initiative_list'] is None or senator['Seguridad_Pública_initiative_list'] == "set()" else 0
                topics["Reglamentos Parlamentarios"] = len(senator['Reglamentos_y_Prácticas_Parlamentarias_initiative_list'].split("', '")) if not senator['Reglamentos_y_Prácticas_Parlamentarias_initiative_list'] is None or senator['Reglamentos_y_Prácticas_Parlamentarias_initiative_list'] == "set()" else 0
                topics["Derechos Humanos"] = len(senator['Derechos_Humanos_initiative_list'].split("', '")) if not senator['Derechos_Humanos_initiative_list'] is None or senator['Derechos_Humanos_initiative_list'] == "set()" else 0
                topics["Migracion"] = len(senator['Asuntos_Fronterizos_y_Migratorios_initiative_list'].split("', '")) if not senator['Asuntos_Fronterizos_y_Migratorios_initiative_list'] is None or senator['Asuntos_Fronterizos_y_Migratorios_initiative_list'] == "set()" else 0
                topics["Ciencia y tecnologia"] = len(senator['Ciencia_y_Tecnología_initiative_list'].split("', '")) if not senator['Ciencia_y_Tecnología_initiative_list'] is None or senator['Ciencia_y_Tecnología_initiative_list'] == "set()" else 0
                topics["Energia"] = len(senator['Energía_initiative_list'].split("', '")) if not senator['Energía_initiative_list'] is None or senator['Energía_initiative_list'] == "set()" else 0
                topics["Juventud y deporte"] = len(senator['Juventud_y_Deporte_initiative_list'].split("', '")) if not senator['Juventud_y_Deporte_initiative_list'] is None or senator['Juventud_y_Deporte_initiative_list'] == "set()" else 0
                topics["Radio, television y cine"] = len(senator['Radio__Televisión_y_Cinematografía_initiative_list'].split("', '")) if not senator['Radio__Televisión_y_Cinematografía_initiative_list'] is None or senator['Radio__Televisión_y_Cinematografía_initiative_list'] == "set()" else 0
                topics["Cultura"] = len(senator['Cultura_initiative_list'].split("', '")) if not senator['Cultura_initiative_list'] is None or senator['Cultura_initiative_list'] == "set()" else 0
                topics["Mineria"] = len(senator['Minería_y_Desarrollo_Regional_initiative_list'].split("', '")) if not senator['Minería_y_Desarrollo_Regional_initiative_list'] is None or senator['Minería_y_Desarrollo_Regional_initiative_list'] == "set()" else 0
                topics["Obras publicas"] = len(senator['Comunicaciones_y_Obras_Públicas_initiative_list'].split("', '")) if not senator['Comunicaciones_y_Obras_Públicas_initiative_list'] is None or senator['Comunicaciones_y_Obras_Públicas_initiative_list'] == "set()" else 0
                topics["Turismo"] = len(senator['Turismo_initiative_list'].split("', '")) if not senator['Turismo_initiative_list'] is None or senator['Turismo_initiative_list'] == "set()" else 0
                topics["Asuntos indigenas"] = len(senator['Asuntos_Indígenas_initiative_list'].split("', '")) if not senator['Asuntos_Indígenas_initiative_list'] is None or senator['Asuntos_Indígenas_initiative_list'] == "set()" else 0
                topics["Movilidad y zonas urbanas"] = len(senator['Zonas_Metropolitanas_y_Movilidad_initiative_list'].split("', '")) if not senator['Zonas_Metropolitanas_y_Movilidad_initiative_list'] is None or senator['Zonas_Metropolitanas_y_Movilidad_initiative_list'] == "set()" else 0
                topics["Derecho de consumidor"] = len(senator['Defensa_de_los_Consumidores_initiative_list'].split("', '")) if not senator['Defensa_de_los_Consumidores_initiative_list'] is None or senator['Defensa_de_los_Consumidores_initiative_list'] == "set()" else 0
                
                sorted_topics = sorted(topics.items(), key=lambda x:x[1], reverse=True)[:5]
                top_5 = dict(sorted_topics)
                
                col1.write(f"**Nombre:** {full_name}")
                col1.write(f"**Partido:** {fraction}")
                col1.write(f"**Estado:** {estado}")
                col1.write(f"**Score de similaridad:** {float(similarity)*100:.0f}")
                col1.write(f"**% de asistencia:** {float(attendance_score)*100:.0f}%")
                
                for value in top_5:
                    col2.write(f"**{value}:** {topics[value]}")
                
                col3.write("**Email:**")
                col3.write(f"{email}")
                col3.write(f"**Telefono:** {telefono}")
                col3.write(f"**Pagina web:**")
                col3.write(f"https://www.senado.gob.mx/65/senador/{senator_id}")
                
                col1.write("---")
                col2.write("---")
                col3.write("---")
        
        except requests.RequestException as e:
            st.error(f"Error fetching data: {e}")

