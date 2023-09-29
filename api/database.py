import mysql.connector

class DatabaseConnection:
    _connection = None
    _config = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host=cls._config['DATABASE_HOST'],
                user=cls._config['DATABASE_USERNAME'],
                port=cls._config['DATABASE_PORT'],
                password=cls._config['DATABASE_PASSWORD']
            )

        return cls._connection

    @classmethod
    def set_config(cls, config):
        cls._config = config

    @classmethod
    def execute_query(cls, query, database_name=None, params=None):

        cursor = None
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            return cursor
        except Exception as e:
            raise e
        finally:
            if cursor:
                cursor.close()

    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = None
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as e:
            # Manejo de excepciones, puedes agregar un registro de errores o realizar otras acciones aquí.
            raise e  # Re-lanza la excepción para que sea manejada en otro lugar si es necesario
        finally:
            if cursor:
                cursor.close()

    @classmethod
    def fetch_one(cls, query, database_name=None, params=None):
        cursor = None
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except Exception as e:
            # Manejo de excepciones, puedes agregar un registro de errores o realizar otras acciones aquí.
            raise e  # Re-lanza la excepción para que sea manejada en otro lugar si es necesario
        finally:
            if cursor:
                cursor.close()

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
