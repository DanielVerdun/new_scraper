# Usamos una imagen base de Python
FROM python:3.9-slim

# Establecemos variables de entorno para evitar el uso de caché
ENV PYTHONUNBUFFERED=1

# Instalamos dependencias del sistema para Selenium y Chromium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    ca-certificates \
    chromium \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo requirements.txt y lo instalamos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación al contenedor
COPY . /app/

# Si el contenedor necesita una conexión con la red de Google Cloud (como BigQuery),
# aseguramos que las credenciales por defecto estén disponibles.

# Configuramos Google Cloud para utilizar las credenciales predeterminadas (ADC).
# Cuando se ejecuta en Google Cloud (por ejemplo, en GKE o Compute Engine), las credenciales
# por defecto de la cuenta de servicio se utilizarán automáticamente.
# Si no se está en Google Cloud, el contenedor intentará usar ADC de la máquina host.

# Exponemos el puerto (si es necesario para el contenedor)
# EXPOSE 8080

# Establecemos el comando para ejecutar el script
CMD ["python", "main.py"]
