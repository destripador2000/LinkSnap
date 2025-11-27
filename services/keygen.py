import string # -> Importamos la librería string
from secrets import choice # -> choice nos permite devolver un elemento
# Elegido aleatoriamente de una secuencia no vacía

# Creamos función para generar una llave random
# Instanceamos que la cadena (length) solo sea de 5 digitos-letras
def create_random_key(length: int = 5) -> str:
    # La cadena tendrá números y letras
    letters = string.ascii_letters + string.digits

    # Devolvemos la cadena
    return ''.join(choice(letters) for _ in range(length))