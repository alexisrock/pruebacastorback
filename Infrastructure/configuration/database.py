from dotenv import load_dotenv
import os
import pyodbc

class DatabaseConnection:
    def __init__(self):
        # Cargar variables de entorno
        load_dotenv()
        
        # Obtener variables de entorno
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.database = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        
     
    def connect(self):
        """
        Establece la conexión a la base de datos usando pyodbc directamente
        """
        try:
            conn_str = (
                f"DRIVER={{ODBC Driver 18 for SQL Server}};"
                f"SERVER={self.host};"
                f"DATABASE={self.database};"
                f"UID={self.user};"
                f"PWD={self.password};"
                f"TrustServerCertificate=yes;"
            )
            self.connection = pyodbc.connect(conn_str)           
            return self.connection
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")
            raise    