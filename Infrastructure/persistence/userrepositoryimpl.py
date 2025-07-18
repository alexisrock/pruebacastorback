from Infrastructure.configuration.database import DatabaseConnection
from domain.entities.user import Users
from domain.interfaces.userrepository import UserRepository



class UserRepositoryImpl(UserRepository):
     def create(self, user: Users) -> bool:
        db = DatabaseConnection()
        connection = db.connect()   
        try:
            # Obtener conexión a la base de datos
            
            cursor = connection.cursor()
            
            # Preparar la consulta SQL con parámetros
            query = """
                INSERT INTO usuario (name, email, password)
                VALUES (?, ?, ?)
            """
            
            # Ejecutar la consulta con los valores del usuario
            cursor.execute(query, (user.name, user.email, user.password))
            
            # Confirmar la transacción
            connection.commit()
            return True
            
        except Exception as e:
            cursor.rollback()
            print(f"Error al crear usuario: {str(e)}")
            return False
            
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()
            
    
     def login(self, email: str) -> Users:      
        db = DatabaseConnection()
        connection = db.connect()   
        try:
            # Obtener conexión a la base de datos
            
            cursor = connection.cursor()
            
            # Preparar la consulta SQL con parámetros
            query = "SELECT id, name, email, password FROM usuario where email= ?"
            
            # Ejecutar la consulta con los valores del usuario
            cursor.execute(query, (email))
            row = cursor.fetchone()
                        # Confirmar la transacción
            user_id, user_name, user_email, hashed_password_from_db = row


            return Users(user_name, user_email, hashed_password_from_db)

       
            
        except Exception as e:
            cursor.rollback()
            print(f"Error al loguear usuario: {str(e)}")
            return None
            
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()
    
