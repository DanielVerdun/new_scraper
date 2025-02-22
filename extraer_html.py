from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service

def extraer_y_guardar_html(url, nombre_archivo="estructura_web.html"):
    """
    Extrae la estructura HTML de un sitio web y la guarda en un archivo.

    Args:
        url (str): La URL del sitio web.
        nombre_archivo (str): El nombre del archivo donde se guardará el HTML.
    """

    try:
        # Configuración de las opciones de Chrome para modo headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo sin cabeza (sin interfaz gráfica)
        chrome_options.add_argument("--disable-gpu")  # Deshabilita la aceleración por GPU (útil en algunos entornos)
        chrome_options.add_argument("--no-sandbox")  # Deshabilita el sandbox de seguridad (necesario en algunos entornos)
        chrome_options.add_argument("--disable-dev-shm-usage")  # Deshabilita el uso de /dev/shm (útil en contenedores)

        # Inicialización del controlador de Chrome
        #driver = webdriver.Chrome(options=chrome_options)
        
        service = Service("/usr/bin/chromedriver")    # Ruta al chromedriver
        driver = webdriver.Chrome(service=service, options=chrome_options)
            
        # Navegación a la URL especificada
        driver.get(url)

        # Espera para que la página cargue completamente (ajusta el tiempo si es necesario)
        time.sleep(5)

        # Extracción del código HTML de la página
        html = driver.page_source

        # Guardado del código HTML en un archivo
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)

        print(f"Estructura HTML guardada en '{nombre_archivo}'")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

    finally:
        # Cierre del controlador de Chrome
        if "driver" in locals():
            driver.quit()

if __name__ == "__main__":
    url_sitio = "https://www.yogonet.com/international/"  # Reemplaza con la URL que desees
    extraer_y_guardar_html(url_sitio)