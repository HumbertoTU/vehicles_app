import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Configurar directorio de trabajo
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'notebooks', 'vehicles_us.csv')

# Cargar los datos
car_data = pd.read_csv(data_path)

# Crear el encabezado
st.header('Aplicación de Visualización de Datos de Vehículos')

# Crear las casillas de verificación para seleccionar los gráficos
show_histogram = st.checkbox('Mostrar histograma de odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Si el usuario selecciona mostrar el histograma
if show_histogram:
    st.write('Creando un histograma para el odómetro de los vehículos')

    # Crear el histograma
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Histograma de Odómetro")

    # Mostrar el histograma interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Si el usuario selecciona mostrar el gráfico de dispersión
if show_scatter:
    st.write(
        'Creando un gráfico de dispersión entre el precio y el odómetro de los vehículos')

    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Gráfico de Dispersión: Precio vs Odómetro")

    # Mostrar el gráfico de dispersión interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
