import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from google.cloud import bigquery

def setup_driver():
    options = Options()
    options.add_argument('--headless')  # Modo sin interfaz gráfica
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service("/usr/bin/chromedriver")  # Ajusta según tu sistema
    driver = webdriver.Chrome(service=service, options=options)

    return driver


def scrape_yogonet():
    driver = setup_driver()
    url = "https://www.yogonet.com/international/"
    driver.get(url)

    # Esperar a que el contenedor principal cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]"))
    )

    # Obtener todas las noticias dentro del contenedor
    noticias = driver.find_elements(By.CSS_SELECTOR, "div.slot")

    datos_noticias = []

    for noticia in noticias:
        try:
            # Extraer título y enlace
            titulo_element = noticia.find_elements(By.CSS_SELECTOR, "h2 a")
            titulo = titulo_element[0].text.strip() if titulo_element else "Título no disponible"
            enlace = titulo_element[0].get_attribute("href") if titulo_element else "Enlace no disponible"

            # Extraer kicker de forma más flexible
            kicker_element = noticia.find_elements(By.CSS_SELECTOR, ".volanta.fuente_roboto_slab")
            kicker = kicker_element[0].text.strip() if kicker_element and kicker_element[0].text.strip() else None

            # Extraer imagen
            imagen_element = noticia.find_elements(By.CSS_SELECTOR, "div.imagen img")
            imagen = imagen_element[0].get_attribute("src") if imagen_element else "Imagen no disponible"

            # Guardar en la lista solo si tiene un título válido y kicker presente
            if titulo != "Título no disponible" and kicker:
                datos_noticias.append({
                    "Título": titulo,
                    "Kicker": kicker,
                    "Enlace": enlace,
                    "Imagen": imagen
                })

        except Exception as e:
            print(f"Error al procesar una noticia: {e}")

    # Crear DataFrame
    df = pd.DataFrame(datos_noticias)

    # Agregar métricas de post-procesamiento
    df['Palabras en Título'] = df['Título'].apply(lambda x: len(x.split()))  # Contar palabras
    df['Caracteres en Título'] = df['Título'].apply(lambda x: len(x))  # Contar caracteres
    df['Palabras Mayúsculas en Título'] = df['Título'].apply(lambda x: [word for word in x.split() if word[0].isupper()])  # Palabras con mayúsculas

    # Mostrar el DataFrame procesado
    print(df)

    # Guardar en un CSV
    df.to_csv("noticias_yogonet_postprocesado.csv", index=False, encoding="utf-8")

    # Insertar datos en BigQuery
    insert_data_to_bigquery(df)

    driver.quit()


def insert_data_to_bigquery(df):
    # Configuración de BigQuery
    client = bigquery.Client()  # Usará las credenciales predeterminadas del entorno

    # Definir el dataset y la tabla en BigQuery
    dataset_id = 'your_project_id.your_dataset_id'
    table_id = f'{dataset_id}.noticias_yogonet'

    # Convertir el DataFrame a una lista de diccionarios
    rows_to_insert = df.to_dict(orient='records')

    # Insertar los datos en BigQuery
    try:
        errors = client.insert_rows_json(table_id, rows_to_insert)  # Inserta datos en BigQuery
        if errors == []:
            print("Datos insertados exitosamente en BigQuery.")
        else:
            print(f"Se produjo un error al insertar los datos: {errors}")
    except Exception as e:
        print(f"Error al insertar los datos en BigQuery: {e}")


scrape_yogonet()
