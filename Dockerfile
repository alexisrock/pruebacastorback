# Usa la imagen base de Python 3.10 slim
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema y el driver de Microsoft ODBC 18
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg \
    unixodbc \
    unixodbc-dev \
    g++ \
    python3-dev \
    build-essential && \
    # Descargar la clave y guardarla en /usr/share/keyrings
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-prod.gpg && \
    # Agregar el repositorio usando la clave
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python necesarias para tu proyecto
RUN pip install --no-cache-dir \
    fastapi \
    httpx \
    pytest \
    requests \
    uvicorn \
    python-dotenv \
    pyodbc \
    bcrypt

# Copiar el proyecto al contenedor, incluido el .env
COPY . .

# Comando para ejecutar la aplicación
CMD ["uvicorn", "presentation.main:app", "--host", "0.0.0.0", "--port", "443"]
