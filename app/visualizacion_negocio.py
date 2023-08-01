import streamlit as st
import pandas as pd
import numpy as np
import pickle

PORT = 8504
st.set_option("server.port", PORT)
def main():
    # Ajustamos la página con un icono en el buscador y el título
    st.set_page_config(page_title="Healty", page_icon=":thermometer:", layout="wide")

    # Ponemos una imagen 
    imagen = "../docs/images/HeatyLogo.jpg"
    imagen_cargada = st.image(imagen)

    # Ponemos un titulo a nuestra aplicación
    st.title("Descubre el Poder de HEATLY: ¡Sin Temor al Calor!")

    texto = """

    Bienvenido a HEATLY, la aplicación web diseñada para brindarte información educativa y esencial sobre las olas de calor. Descubre el poder de HEATLY y prepárate para enfrentar el calor extremo sin temor.

    Nuestra misión es empoderarte con datos precisos y valiosos sobre las olas de calor, ayudándote a entender su impacto en tu entorno y en tu salud. Con HEATLY, podrás acceder a una amplia gama de recursos educativos y realizar cuestionarios personalizados para evaluar tus conocimientos sobre el tema.

    """
    st.write(texto)

    if st.checkbox('¿Cómo funciona HEATLY?'):
            texto= '''
    Información Educativa: Descubre el poder de HEATLY y adquiere conocimientos sobre las olas de calor. Aprende sobre sus causas, consecuencias y medidas de prevención. Con esta información, estarás preparado para enfrentar el calor sin miedo.

    Cuestionarios Personalizados: ¿Cuánto sabes realmente sobre las olas de calor? Con nuestros cuestionarios interactivos, podrás evaluar tus conocimientos y obtener retroalimentación para mejorar tu comprensión del tema. ¡Conviértete en un experto en el calor!

    Pronóstico de Temperaturas: Descubre el poder de HEATLY para mantenerte informado sobre las temperaturas venideras en tu área. Con esta anticipación, podrás planificar tus actividades y tomar las medidas necesarias para evitar el impacto del calor extremo.

    Consejos Prácticos: Además de la información educativa, descubre el poder de HEATLY para recibir consejos prácticos y recomendaciones para mantenerte fresco y seguro durante las olas de calor. ¡Sin temor al calor, estarás preparado!

    En HEATLY, creemos que estar informado y preparado es la clave para enfrentar el calor de manera segura y responsable. Descubre el poder de HEATLY y únete a nuestra comunidad de personas que enfrentan el calor sin temor.

    ¡Explora HEATLY y descubre cómo puedes convertirte en un defensor de tu bienestar en tiempos de altas temperaturas! Tu seguridad y comodidad son nuestra prioridad, y estamos aquí para acompañarte en cada paso del camino.

    Recuerda, el conocimiento es poder, y con HEATLY, estarás listo para abrazar el calor y disfrutar de cada temporada, sin preocupaciones. ¡Bienvenido a la experiencia HEATLY: Descubre el Poder de ¡Sin Temor al Calor!


    '''
            texto
    else:
            st.markdown('El texto permanece oculto')



    menu = st.sidebar.selectbox("Selecciona la Página", ['PRINCIPAL','DATOS USUARIOS','DATOS QUIZ', 'PREDICCIÓN'])


    if menu == 'DATOS USUARIOS':

        st.header('Datos Usuarios') # Nombramos el título
    
        if st.checkbox('Mostrar el DataFrame '):
            df= pd.read_csv("../data/users_login/users.csv")
            df
        else:
            st.markdown('El dataset esta oculto')

        texto2 = """
    
    """

        st.write(texto2)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(['Fecha de Registro', 'Sexo','Fecha de Nacimiento', 'Código Postal', 'Número de Hijos Menores'])


        with tab1:

            st.subheader('Visualización de la Fecha de Registro')
            texto_tab2 = '''
            En ambas visualizaciones podemos obervar la evolución de los usuarios registrados por mes
                    '''
            st.write(texto_tab2)
            
            imagen = "../docs/images/eda_users/usuarios_por_mes_barras.png"
            imagen_cargada = st.image(imagen)

            
            imagen = "../docs/images/eda_users/usuarios_por_mes_lineas.png"
            imagen_cargada = st.image(imagen)
            
            

        with tab2:

            st.subheader('Visualización de la variable de Sexo')
            texto_tab2 = '''
            Podemos observar la distribución de los usuarios que son hombres y de los usuarios que son mujeres
                    '''
            st.write(texto_tab2)
            
            imagen = "../docs/images/eda_users/pie_plot_sexo.png"
            imagen_cargada = st.image(imagen)

            texto_tab2 = '''
            
            '''
            st.write(texto_tab2)


        with tab3:

            st.subheader('Visualización de la variable Fecha de Nacimiento')
            texto_tab2 = '''
            Se aprecia cual es la franja de edad predominante de los usuarios y la evolución del resto.
                    '''
            st.write(texto_tab2)
            
            imagen = "../docs/images/eda_users/pie_plot_franja_edad_espaciado.png"
            imagen_cargada = st.image(imagen)



        with tab4:

            st.subheader('Visualización de la variable Código Postal')
            texto_tab3 = '''
        
            '''
            st.write(texto_tab3)
        
            imagen = "../docs/images/eda_users/grafico_barras_cp_top_15.png"
            imagen_cargada = st.image(imagen)

            imagen = "../docs/images/eda_users/pie_plot_zona_cp.png"
            imagen_cargada = st.image(imagen)
            texto_tab3 = '''
        
            '''
            st.write(texto_tab3)


        with tab5:

            st.subheader('Visualización de la variable Número de Hijos Menores')

            imagen = "../docs/images/eda_users/cantidad_hijos_menores.png"
            imagen_cargada = st.image(imagen)

            imagen = "../docs/images/eda_users/box_plot_cantidad_hijos_menores.png"
            imagen_cargada = st.image(imagen)

            imagen = "../docs/images/eda_users/hijos_menores_si_no.png"
            imagen_cargada = st.image(imagen)

            texto_tab3 = '''
        
            '''
            st.write(texto_tab3)

    elif menu == 'DATOS QUIZ':

        # Procesamos los datos
        st.header('Procesado de los datos del cuestionario: ')

        if st.checkbox('Mostrar el DataFrame procesado'):
            df_procesado= pd.read_csv("../data/quiz/answers.csv")
            df_procesado
        else:
            st.markdown('El dataset esta oculto')

        tab1, tab2, tab3 = st.tabs(['Porcentage sexos aptos', 'Porcentage aptos por edades', 'Porcentage total'])

        with tab1:

            st.subheader('Visualización de Porcentage de aptos por Sexo')

            
            imagen = "../docs/images/eda_quiz/porc_sexos_aptos.png"
            imagen_cargada = st.image(imagen)

        with tab2:

            st.subheader('Visualización de Porcentage de aptos por Edades')

            
            imagen = "../docs/images/eda_quiz/porcentaje_aptos_hm_edades.png"
            imagen_cargada = st.image(imagen)

            texto_tab2 = ''' '''
            
            st.write(texto_tab2)


        with tab3:

            st.subheader('Visualización del Porcentage Total')

            
            imagen = "../docs/images/eda_quiz/porc_total_aptos.png"
            imagen_cargada = st.image(imagen)

            texto_tab3 = '''
            
            '''
            st.write(texto_tab3)

        

    elif menu == 'PREDICCIÓN':
        # Procesamos los datos
        st.header('Descripción de Machine Learning: ')
    
        if st.checkbox('Mostrar el DataFrame procesado'):
            df_procesado= pd.read_csv("../data/processed/users_processed.csv")
            df_procesado
        else:
            st.markdown('El dataset esta oculto')

        st.header('Prediction Model')


        ruta_mod = "../models/trained_model.pkl"

        with open(ruta_mod, 'rb') as file:
            loaded_model = pickle.load(file)

        st.header('Input desired parameters:')

        sexo = st.slider('gender', 0, 1)
        valor_franja_edad = st.slider('age range', 0, 3)
        tiene_hijos = st.slider('has children', 0, 1)
        zona = st.slider('zone in madrid', 0, 2)


        input = np.array([sexo,	valor_franja_edad, tiene_hijos, zona]).reshape(1, -1)
        pred = loaded_model.predict(input)[0]



        #sexo	valor_franja_edad	tiene_hijos	zona	target

        if st.button('TEST!'):
            if pred == 0:
                st.header('Lo más probable es que este usuario necesite apoyo e información adicionales')
            if pred == 1:
                st.header('Lo más probable es que este usuario obtenga una puntuación de 7 o superior en el cuestionario.  No requiere avisos adicionales en este momento')

if __name__ == '__main__':
    main()