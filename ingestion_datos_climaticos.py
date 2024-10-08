# Importamos las librerías necesarias
import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

# Función para obtener datos de una API pública de clima
def obtener_datos_climaticos(api_url, ciudad, api_key):
    # Construimos la URL completa con la ciudad y la clave de API
    url = f"{api_url}?q={ciudad}&appid={api_key}&units=metric"
    # Hacemos una petición GET a la API
    respuesta = requests.get(url)
    
    # Si la petición fue exitosa
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        print(f"Error: {respuesta.status_code}")
        return None

# Función para procesar y transformar los datos a un DataFrame
def procesar_datos_climaticos(datos):
    if datos is None:
        return None
    
    # Extraemos la información relevante
    data_procesada = {
        "ciudad": datos["name"],
        "temperatura": datos["main"]["temp"],
        "humedad": datos["main"]["humidity"],
        "presion": datos["main"]["pressure"],
        "viento_velocidad": datos["wind"]["speed"],
        "descripcion_clima": datos["weather"][0]["description"]
    }
    
    # Creamos un DataFrame con los datos extraídos
    df = pd.DataFrame([data_procesada])
    return df

# Función para guardar los datos en formato CSV
def guardar_en_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en CSV: {nombre_archivo}")

# Función para guardar los datos en formato Parquet
def guardar_en_parquet(df, nombre_archivo):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, nombre_archivo)
    print(f"Datos guardados en Parquet: {nombre_archivo}")

# Función principal que coordina todo
def main():
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    ciudad = "Paris"  # Puedes cambiar esto a cualquier ciudad
    api_key = "tu_api_key"  # Reemplaza con tu propia clave de API
    
    # Obtener los datos climáticos
    datos = obtener_datos_climaticos(api_url, ciudad, api_key)
    
    # Procesar los datos
    df_clima = procesar_datos_climaticos(datos)
    
    if df_clima is not None:
        # Crear las carpetas de destino si no existen
        os.makedirs("output", exist_ok=True)
        
        # Guardar los datos en CSV
        guardar_en_csv(df_clima, "output/datos_clima.csv")
        
        # Guardar los datos en Parquet
        guardar_en_parquet(df_clima, "output/datos_clima.parquet")
    else:
        print("No se pudieron procesar los datos.")

if __name__ == "__main__":
    main()
