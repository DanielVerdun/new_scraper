# new_scraper
Estructura del proyecto:

    .
    ├── Dockerfile
    ├── README.md
    ├── deploy.sh
    ├── estructura_web.html
    ├── extraer_html.py
    ├── main.py
    ├── main_test_localhost.py
    └── requirements.txt

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
        git checkout main   
   
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

5. Verificación de resultados
Si todo funciona correctamente, deberías ver el procesamiento de las noticias en la terminal y los datos insertados en CSV o en BigQuery (si configuraste las credenciales de Google Cloud).

Además, el script también puede generar un archivo CSV con los resultados del scraping con el nombre de "noticias_yogonet_postprocesado.csv"

Desactivación del entorno virtual
Cuando termines de trabajar, puedes desactivar el entorno virtual:

        deactivate

# Pasos para ejecutar en GCP BigQuery:

Para ejecutar la automatizacion en GCP es necesario tener una cuenta en Google Cloud Platform.
La automatizacion se genera automaticamente configurando los parametros de tu proyecto en el archivo : deploy.sh

Luego de configurar los parametros de tu proyecto debemos modificar el main.py el cual tambien requiere los parametros de tu proyecto. 
En el main.py necesitamos: 
# Definir el dataset y la tabla en BigQuery
    dataset_id = 'your_project_id.your_dataset_id'

Una vez hechas estas configuraciones ejeutamos el deploy.sh:
Haz que el script sea ejecutable:

    chmod +x deploy.sh
Ejecuta el script:

    ./deploy.sh

# Verificación de resultados
Si todo funciona correctamente, deberías ver el procesamiento de las noticias en la terminal y los datos insertados en BigQuery (si configuraste las credenciales de Google Cloud).

Además, el script también puede generar un archivo CSV con los resultados del scraping, dependiendo de cómo esté configurado el código.

# Adicional:
Adicionalmente se desarrolla un script llamado extraer_html.py Este archivo contendrá el código HTML de la página objetivo, permitiéndonos identificar las etiquetas, clases y atributos relevantes para la implementación del scraping.  
