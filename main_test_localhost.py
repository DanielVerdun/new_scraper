import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

            # Depuración: Ver si realmente hay kickers en el HTML
            print(f"Título: {titulo}")
            print(f"Kicker: {kicker if kicker else 'No Kicker'}")
            print(f"Enlace: {enlace}")
            print(f"Imagen: {imagen}")
            print("-" * 40)

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

    driver.quit()


scrape_yogonet()
