import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Ajustar el directorio de trabajo al directorio donde está el script
# Obtiene la ruta completa del archivo
script_dir = os.path.dirname(os.path.abspath(__file__))
# Cambia el directorio de trabajo al directorio del script
os.chdir(script_dir)

# Ahora el script siempre usará rutas relativas desde la carpeta `vehicles_app`
car_data = pd.read_csv('notebooks/vehicles_us.csv')  # leer los datos

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
