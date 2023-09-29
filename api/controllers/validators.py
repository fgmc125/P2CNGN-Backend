from ..database import DatabaseConnection
from ..models.exceptions import InvalidDataError




def exists(table_name, id_column, id_value):
    """Devuelve True si el ID existe en la tabla, o False en caso contrario."""

    query = "SELECT COUNT(*) FROM {} WHERE {} = %s".format(
        table_name, id_column
    )
    params = (id_value,)
    result = DatabaseConnection.fetch_one(query, params)

    return result[0] > 0

def validate_user_data(data):
    """
    Valida los datos de entrada para crear un nuevo usuario.

    Args:
        data: Los datos de entrada del usuario.

    Returns:
        Los datos de entrada validados.

    Raises:
        InvalidDataError: Si los datos no son válidos.
    """

    # Validar el nombre de usuario
    if not data['username'] or len(data['username']) < 3:
        raise InvalidDataError('El nombre de usuario debe tener al menos 3 caracteres')

    # Validar la contraseña
    if not data['password'] or len(data['password']) < 8:
        raise InvalidDataError('La contraseña debe tener al menos 8 caracteres')

    return data

def validate_unique_username(username, id = None):
    return validate_unique('Users', 'username', username, id)

def validate_unique_email(email, id = None):
    return validate_unique('Users', 'email', email, id)

def validate_unique_server_name(server_name):
    return validate_unique('Servers', 'name', server_name)

def validate_unique_channel_name(channel_name):
    return validate_unique('Channels', 'name', channel_name)


def validate_unique(table, column, value, id):
    """
    Valida si un valor es único en una columna de una tabla.

    Args:
        table: La tabla a validar.
        column: La columna a validar.
        value: El valor a validar.

    Returns:
        True si el valor es único, False en caso contrario.

    Raises:
        InvalidDataError: Si la tabla o la columna no existen.
    """
    
    if id:
        query = f'SELECT COUNT(*) FROM bk9kjvgo2gjf3qeyk1dt.Users WHERE column = %s AND id != %s'
        params = (column,id,)

        #query = f'SELECT COUNT(*) AS total FROM bk9kjvgo2gjf3qeyk1dt.{table} WHERE {table}.{column} = {value})'
    
        result = DatabaseConnection.fetch_one(query, params=params)
        count  = result[0]
        return count == 0
    
    else:      
    
        query = f'SELECT COUNT(*) FROM bk9kjvgo2gjf3qeyk1dt.{table} WHERE LOWER({column}) = LOWER(%s)'
        params = (value,)

        result = DatabaseConnection.fetch_one(query, params=params)
    
        count = result[0]
    
        return count == 0
    
        
