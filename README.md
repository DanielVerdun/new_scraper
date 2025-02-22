# new_scraper
# Instrucciones para ejecutar el proyecto en Localhost
Este proyecto permite realizar scraping de noticias desde Yogonet y procesarlas para ser almacenadas en BigQuery. A continuación, se describen los pasos necesarios para ejecutar el proyecto en tu entorno local.(Localhost no almacena en bigquery)

Requisitos previos
Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu sistema:

Python 3.8 o superior: Para verificar tu versión de Python, ejecuta:

    python --version
    
# Pasos para la ejecución en localhost

1. Clonar el repositorio
Primero, debes clonar el repositorio del proyecto en tu máquina local:

        git clone https://github.com/DanielVerdun/new_scraper.git
        cd new_scraper
   
3. Crear un entorno virtual
Es altamente recomendable crear un entorno virtual para evitar conflictos con otras dependencias de proyectos:

        python -m venv venv
   
Esto creará un entorno virtual en el directorio venv.

3. Activar el entorno virtual
Dependiendo de tu sistema operativo, activa el entorno virtual:

En Linux/MacOS:

        source venv/bin/activate

En Windows:

        .\venv\Scripts\activate
Verás que el nombre de tu entorno virtual (generalmente venv) aparece al principio de la línea de comandos.

4. Instalar dependencias
Una vez que el entorno virtual esté activado, instala todas las dependencias necesarias utilizando el archivo requirements.txt:

        pip install -r requirements.txt

Esto instalará todos los paquetes necesarios para ejecutar el proyecto, incluidos aquellos para el scraping, procesamiento de datos, y la integración con Google Cloud.

Luego puede ejecutar el scritp main_test_localhost.py

        python main_test_localhost.py

El script realizará las siguientes acciones:

Scrapea las noticias desde Yogonet.
Realiza el procesamiento de datos (cuenta de palabras, caracteres, etc.).
Inserta los datos procesados en BigQuery si está configurado.

6. Verificación de resultados
Si todo funciona correctamente, deberías ver el procesamiento de las noticias en la terminal y los datos insertados en BigQuery (si configuraste las credenciales de Google Cloud).

Además, el script también puede generar un archivo CSV con los resultados del scraping, dependiendo de cómo esté configurado el código.

Desactivación del entorno virtual
Cuando termines de trabajar, puedes desactivar el entorno virtual:

        deactivate

