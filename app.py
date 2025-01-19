import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Configurar directorio de trabajo
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'notebooks', 'vehicles_us.csv')

# Cargar los datos
car_data = pd.read_csv(data_path)

# Título de la app
st.title('Aplicación de Análisis de Datos de Vehículos')

# Descripción breve del objetivo de la app
st.write("""
Esta aplicación permite explorar y analizar un conjunto de datos sobre anuncios de vehículos en venta. 
Puedes visualizar estadísticas descriptivas, crear gráficos interactivos y obtener información valiosa sobre los vehículos disponibles.
""")

# Título para la sección de visualización de datos
st.subheader('Visualización de los Datos de Vehículos')


# Checkbox para decidir si mostrar el DataFrame
show_data = st.checkbox('Mostrar datos de vehículos')

# Mostrar texto pequeño con la aclaración
st.markdown(
    "Se muestra solo una muestra de la base de datos (primeros 5000 registros).",
    unsafe_allow_html=True
)

# Si el checkbox está seleccionado, mostrar el DataFrame
if show_data:
    # Mostrar todo el DataFrame con barras de desplazamiento
    # Ajusta 'height' según lo necesites para reducir el tamaño
    st.dataframe(car_data.head(5000), height=200)
