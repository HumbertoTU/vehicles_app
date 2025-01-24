Configuración de los Gráficos


Este apartado explica las funcionalidades y configuraciones disponibles para cada gráfico 
interactivo en la aplicación:

1. Exploración de Datos

    *Función: 
        -Muestra los primeros 5000 registros del conjunto de datos para facilitar una vista general.

    *Interacción:
        -El usuario puede habilitar la visualización seleccionando la casilla "Mostrar datos de vehículos".
        -Se muestra una tabla con barra de desplazamiento para explorar los datos.


2. Visualización de Histogramas

    *Función: 
        -Permite analizar la distribución de una variable numérica, con la opción de agrupar los datos por una categoría.
    *Configuración:
        -El usuario debe seleccionar:
            -Una columna numérica para el eje X.
            -Una columna categórica para agrupar (opcional).
        -El histograma utiliza una paleta de colores Set2 y divide los datos en 30 intervalos (bins) por defecto.
    *Interacción:
        -Los usuarios pueden alternar la casilla "Mostrar histograma" para habilitar esta funcionalidad.

3. Diagrama de Dispersión


    *Función: 
        -Explora las relaciones entre dos variables numéricas para identificar patrones o posibles correlaciones.
    *Configuración:
    	-El usuario debe seleccionar:
            -Una columna para el eje X.
            -Otra columna para el eje Y.
        -El gráfico utiliza la escala de colores Viridis y el diseño visual Plotly White.
    *Interacción:
        -Habilita el diagrama seleccionando la casilla "Mostrar diagrama de dispersión".

4. Distribución de Vehículos por Marca y Tipo

    *Función: 
        -Visualiza la cantidad total de vehículos por marca, agrupados por tipo de vehículo en un gráfico de barras apiladas.
    *Configuración:
        -Agrupa los datos utilizando las columnas "brand" (marca) y "type" (tipo de vehículo).
        -Aplica una paleta de colores Set2 para representar los diferentes tipos de vehículos.
        -Configura un diseño con barras apiladas, espaciado de 0.2 entre las barras y una altura personalizada de 600px.
    *Interacción:
        -Selecciona la casilla "Mostrar gráfico de relación entre marcas y tipos de vehículo" para habilitar esta sección.
        -Edición de elementos visibles:
            -En el lado derecho del gráfico, aparece una columna que lista las marcas y tipos de vehículos disponibles.
            -Los usuarios pueden seleccionar o deseleccionar elementos específicos haciendo clic en ellos para ajustar dinámicamente los datos visibles en el gráfico.
