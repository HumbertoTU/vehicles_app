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
st.title("Análisis de Vehículos en Venta")

# Botón para graficar
if st.button('Construir Histograma'):
    st.write("Histograma de kilometraje de los vehículos en venta")
    fig = px.histogram(car_data, x="odometer",
                       title="Kilometraje de Vehículos")
    st.plotly_chart(fig, use_container_width=True)
