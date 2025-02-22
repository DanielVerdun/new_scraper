#!/bin/bash

# Configuración de la cuenta y proyecto de Google Cloud
PROJECT_ID="tu-proyecto-id"  # Reemplaza con tu ID de proyecto de Google Cloud
REGION="us-central1"         # Cambia la región si es necesario
IMAGE_NAME="noticias-scraper"  # Nombre de la imagen Docker
IMAGE_TAG="latest"            # Etiqueta de la imagen
SERVICE_NAME="noticias-scraper-service"  # Nombre del servicio de Cloud Run

# Paso 1: Autenticación con Google Cloud (asegúrate de que gcloud esté configurado)
echo "Autenticando en Google Cloud..."
gcloud auth login

# Paso 2: Seleccionar el proyecto adecuado
echo "Configurando el proyecto: $PROJECT_ID..."
gcloud config set project $PROJECT_ID

# Paso 3: Construir la imagen Docker
echo "Construyendo la imagen Docker..."
docker build -t gcr.io/$PROJECT_ID/$IMAGE_NAME:$IMAGE_TAG .

# Paso 4: Subir la imagen Docker a Google Container Registry
echo "Subiendo la imagen Docker a Google Container Registry..."
docker push gcr.io/$PROJECT_ID/$IMAGE_NAME:$IMAGE_TAG

# Paso 5: Desplegar la imagen en Google Cloud Run
echo "Desplegando en Google Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$IMAGE_NAME:$IMAGE_TAG \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --timeout 15m

# Fin
echo "Despliegue completado en Cloud Run."
