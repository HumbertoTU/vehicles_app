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
st.title('Aplicación de Análisis de Datos de Vehículos Usados Vendidos')

# Descripción breve del objetivo de la app
st.write("""
Esta aplicación permite explorar y analizar un conjunto de datos sobre anuncios de vehículos en venta. 
Puedes visualizar estadísticas descriptivas, crear gráficos interactivos y obtener información valiosa sobre los vehículos disponibles.
""")

# Título para la sección de visualización de los datos
st.subheader('Exploración de los Datos de Vehículos')

# Descripción de la sección
st.write("""
En esta sección puedes explorar una muestra de los datos de vehículos disponibles para la venta. El conjunto de datos 
contiene información sobre las características de los vehículos, como la marca, el modelo, el año, el precio, el kilometraje, 
y otros detalles importantes. Puedes interactuar con la tabla para visualizar los primeros 5000 registros y obtener una visión 
general de los datos.
""")


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
El histograma permite analizar la distribución de una variable numérica en el conjunto de datos, con la posibilidad de agrupar los valores por una categoría.
Selecciona dos columnas: una numérica para el eje X y otra categórica para agrupar los datos.
""")

# Checkbox para mostrar el histograma
show_histogram = st.checkbox('Mostrar histograma')

# Si el checkbox está seleccionado, mostrar las opciones y el gráfico
if show_histogram:
    # Filtrar las columnas numéricas y categóricas
    numeric_columns = car_data.select_dtypes(
        include=['int64', 'float64']).columns
    categorical_columns = car_data.select_dtypes(
        include=['object', 'category']).columns

    # Verificar si hay columnas disponibles
    if len(numeric_columns) > 0 and len(categorical_columns) > 0:
        # Selección de la columna numérica para el histograma
        hist_numeric_column = st.selectbox(
            'Selecciona la columna numérica para el histograma (eje X):',
            numeric_columns
        )

        # Selección de la columna categórica para agrupar
        hist_categorical_column = st.selectbox(
            'Selecciona la columna categórica para agrupar (opcional):',
            ['Ninguno'] + list(categorical_columns)
        )

        # Crear el histograma
        hist_fig = px.histogram(
            car_data,
            x=hist_numeric_column,
            color=hist_categorical_column if hist_categorical_column != 'Ninguno' else None,
            nbins=30,  # Número de barras en el histograma
            title=f'Histograma de: {hist_numeric_column}' + (
                f' agrupado por: {hist_categorical_column}' if hist_categorical_column != 'Ninguno' else ''),
            color_discrete_sequence=px.colors.qualitative.Set2,  # Paleta de colores
            template='plotly_white'
        )

        # Mostrar el gráfico
        st.plotly_chart(hist_fig)
    else:
        st.write(
            "No hay suficientes columnas numéricas o categóricas disponibles para crear un histograma.")

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

# Título para la sección de gráfico de relación entre marcas y tipos de vehículo
st.subheader('Distribución de Vehículos por Marca y Tipo')

# Descripción de la sección
st.write("""
Este gráfico muestra la cantidad total de vehículos disponibles para cada marca. Las barras están segmentadas por colores para 
representar los diferentes tipos de vehículos (sedán, SUV, pickup, etc.), lo que permite visualizar cómo se distribuyen 
los tipos de vehículos dentro de cada marca.
""")


# Checkbox para mostrar el gráfico
show_brand_vehicle_chart = st.checkbox(
    'Mostrar gráfico de relación entre marcas y tipos de vehículo')

# Si el checkbox está seleccionado, mostrar las opciones y el gráfico
if show_brand_vehicle_chart:
    # Verificar si las columnas necesarias existen en el DataFrame
    if 'brand' in car_data.columns and 'type' in car_data.columns:
        # Filtrar filas con valores no nulos en las columnas necesarias
        filtered_data = car_data.dropna(subset=['brand', 'type'])

        # Agrupar datos por marca y tipo, y contar la cantidad de vehículos
        grouped_data = filtered_data.groupby(
            ['brand', 'type']).size().reset_index(name='count')

        # Crear el gráfico de barras apiladas
        brand_vehicle_fig = px.bar(
            grouped_data,
            x='brand',
            y='count',
            color='type',
            title='Distribución Total de Vehículos por Marca y Tipo',
            labels={'brand': 'Marca', 'count': 'Cantidad de Vehículos',
                    'type': 'Tipo de Vehículo'},
            color_discrete_sequence=px.colors.qualitative.Set2,  # Paleta de colores
            template='plotly_white'
        )

        # Ajustar diseño del gráfico
        brand_vehicle_fig.update_layout(
            xaxis_title='Marca',
            yaxis_title='Cantidad Total de Vehículos',
            legend_title='Tipo de Vehículo',
            bargap=0.2,  # Espaciado entre barras
            height=600
        )

        # Mostrar el gráfico
        st.plotly_chart(brand_vehicle_fig)
    else:
        st.write(
            "El DataFrame no contiene las columnas necesarias ('brand' y 'type').")
