# Ingestión y Procesamiento de Datos Climáticos

## Descripción
Este proyecto tiene como objetivo la ingesta de datos climáticos de una API pública (OpenWeatherMap), su procesamiento, y almacenamiento en dos formatos de archivo: **CSV** y **Parquet**. Se diseñó para ser utilizado como un ejemplo práctico en tareas comunes de ingeniería de datos, donde es necesario automatizar la obtención y transformación de datos antes de ser almacenados de manera eficiente.

## Funcionamiento del Código
El código realiza las siguientes acciones:

1. **Obtención de datos:** Se conecta a la API de OpenWeatherMap para obtener los datos climáticos de una ciudad específica.
2. **Procesamiento de datos:** Los datos obtenidos son transformados y estructurados en un formato de tabla (DataFrame de pandas), extrayendo la información más relevante como la temperatura, humedad, presión, velocidad del viento, y descripción del clima.
3. **Almacenamiento de datos:** El DataFrame procesado se guarda en dos formatos:
    - **CSV:** Un formato de archivo de texto simple que es ampliamente utilizado para compartir datos.
    - **Parquet:** Un formato de almacenamiento columnar altamente eficiente en términos de espacio y velocidad de lectura, utilizado comúnmente en proyectos de Big Data.

## Ejemplo de Uso
Para ejecutar este código, asegúrate de tener Python instalado junto con las dependencias necesarias. Sigue estos pasos:

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu_usuario/ingestion-y-procesamiento-datos-climaticos.git
    ```

2. Instala las librerías necesarias (si aún no las tienes):
    ```bash
    pip install pandas requests pyarrow
    ```

3. Modifica el archivo `ingestion_datos_climaticos.py` para agregar tu clave de API en la variable `api_key` y cambiar la ciudad si lo deseas.

4. Ejecuta el script desde tu terminal:
    ```bash
    python ingestion_datos_climaticos.py
    ```

5. Los archivos resultantes se guardarán en la carpeta `output` en formato CSV y Parquet.

## Consideraciones
- Necesitas una **clave de API** válida de [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) para poder realizar las solicitudes de datos climáticos.
- Puedes cambiar la ciudad consultada modificando la variable `ciudad` en el código.
- Asegúrate de tener conexión a internet al ejecutar el script, ya que se realiza una solicitud a la API externa.

## **Utilidad en Ingeniería de Datos**
Este proyecto es una excelente representación de las tareas que un **Data Engineer** realiza a diario. El código implementa un flujo básico de ingesta y procesamiento de datos, que incluye la conexión a una fuente externa (API), la transformación de los datos en un formato tabular y su almacenamiento en diferentes formatos de archivo. **Este tipo de procesos es fundamental en la automatización de pipelines de datos**, donde se debe manejar grandes volúmenes de información y garantizar que los datos se almacenen de manera eficiente para su posterior análisis o procesamiento.

Además, **el uso de formatos como Parquet** es particularmente útil en entornos de Big Data, donde se prioriza la optimización del espacio de almacenamiento y la velocidad de acceso a los datos. Este ejemplo puede ampliarse fácilmente para ser integrado en proyectos más complejos de ETL (Extract, Transform, Load), donde la calidad y eficiencia del manejo de datos es crítica.
