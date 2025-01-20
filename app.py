import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Configurar directorio de trabajo
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'notebooks', 'info_clean.csv')

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

# Título para la sección de histograma
st.subheader('Visualización de Histograma')

# Descripción de la sección
st.write("""
El histograma permite analizar la distribución de una variable numérica en el conjunto de datos. 
Selecciona una columna para visualizar cómo se distribuyen sus valores.
""")

# Checkbox para mostrar el histograma
show_histogram = st.checkbox('Mostrar histograma')

# Si el checkbox está seleccionado, mostrar el histograma
if show_histogram:
    # Filtrar las columnas numéricas
    numeric_columns = car_data.select_dtypes(
        include=['int64', 'float64']).columns

    # Verificar si hay columnas numéricas disponibles
    if len(numeric_columns) > 0:
        # Selección de la columna para el histograma
        column = st.selectbox(
            'Selecciona una columna para el histograma:', numeric_columns)

        # Crear histograma interactivo
        fig = px.histogram(car_data, x=column,
                           title=f'Histograma de {column}', nbins=30)

        # Mostrar el gráfico
        st.plotly_chart(fig)
    else:
        st.write("No hay columnas numéricas disponibles en los datos.")

# Título para la sección de diagrama de dispersión
st.subheader('Visualización de Diagrama de Dispersión')

# Descripción de la sección
st.write("""
El diagrama de dispersión permite explorar la relación entre dos variables numéricas. 
Selecciona las columnas que deseas analizar para generar un gráfico interactivo.
""")

# Checkbox para mostrar el diagrama de dispersión
show_scatter = st.checkbox('Mostrar diagrama de dispersión')

# Si el checkbox está seleccionado, mostrar las opciones y el gráfico
if show_scatter:
    # Filtrar las columnas numéricas
    numeric_columns = car_data.select_dtypes(
        include=['int64', 'float64']).columns

    # Verificar si hay suficientes columnas numéricas disponibles
    if len(numeric_columns) > 1:
        # Selección de las columnas para el eje X e Y
        x_column = st.selectbox(
            'Selecciona la columna para el eje X:', numeric_columns)
        y_column = st.selectbox(
            'Selecciona la columna para el eje Y:', numeric_columns)

        # Crear el diagrama de dispersión
        scatter_fig = px.scatter(
            car_data,
            x=x_column,
            y=y_column,
            title=f'Diagrama de dispersión: {x_column} vs {y_column}',
            color_continuous_scale='Viridis',
            template='plotly_white'
        )

        # Mostrar el gráfico
        st.plotly_chart(scatter_fig)
    else:
        st.write(
            "No hay suficientes columnas numéricas disponibles para crear un diagrama de dispersión.")
