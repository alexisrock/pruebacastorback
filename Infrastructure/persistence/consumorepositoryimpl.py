from Infrastructure.configuration.database import DatabaseConnection
from domain.interfaces.consumorepository import ConsumoRepository
from domain.entities.consumos import Consumo

class ConsumoRepositoryImpl(ConsumoRepository):
    def insert_consumo(self, artistname: str, respuestajson: str) -> bool:
        db = DatabaseConnection()
        connection = db.connect()
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO Consumos (ArtistaName, RespuestaJson)
                VALUES (?, ?)
            """
            cursor.execute(query, (artistname, respuestajson))
            connection.commit()
            return True
        except Exception as e:
            cursor.rollback()
            print(f"Error al insertar consumo: {str(e)}")
            return False
        finally:
            cursor.close()
            connection.close()

    def get_consumo_by_artistname(self, artistname: str):
        db = DatabaseConnection()
        connection = db.connect()
        try:
            cursor = connection.cursor()
            query = """
                SELECT ArtistaName, RespuestaJson FROM Consumos WHERE ArtistaName = ?
            """
            cursor.execute(query, (artistname))
            row = cursor.fetchone()
            if row:
                return Consumo(artistaname=row[0], respuestajson=row[1])
            return None
        except Exception as e:
            cursor.rollback()
            print(f"Error al consultar consumo: {str(e)}")
            return None
        finally:
            cursor.close()
            connection.close()
