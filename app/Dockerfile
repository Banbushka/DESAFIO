# Utiliza una imagen base de Python con Flask instalado1
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo chatpi.py al directorio de trabajo
COPY . .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8501

# Define el comando para iniciar la aplicación
CMD ["streamlit", "run", "visualizacion_negocio.py"]