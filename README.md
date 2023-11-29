[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/TiZcQ-cx)
# hlc-python-exam-simulation

Simulación de prueba python en base a test unitarios

## Prerequisitos
Instalar pip3 (si no está instalado)
```
sudo apt intall pip3 
```

Instalar pytest
```
pip3 install pytest 
```

## Instrucciones 

### Indice masa corporal (IMC)

Dentro del directorio assignment crea un archivo llamado **imc.py** que contenga una función con la siguiente estructura:

```
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.

    Returns:
    float: El IMC calculado.

    Raises:
    ValueError: Si el peso o la altura son menores o iguales a cero.
    """
```

### Gestión de Contactos

Dentro del directorio assignment crea un archivo llamado **contact.py** que contenga el código para la siguiente estructura:
```
class Contact:
    """Representa un contacto con nombre, teléfono y email."""

    def __init__(self, nombre, telefono, email):
        """
        Inicializa un nuevo contacto.

        Args:
            nombre (str): Nombre del contacto.
            telefono (str): Número de teléfono del contacto.
            email (str): Dirección de email del contacto.
        """
       

    def __str__(self):
        """Devuelve la representación en cadena del contacto en formato CSV."""
        

    def __eq__(self, other):
        """Compara dos contactos por su contenido."""
        
```
Dentro del directorio assignment crea un archivo llamado **contact_manager.py** que contenga el código para la siguiente estructura:
```
import os
from assignment.contact import Contact

class ContactManager:
    """Gestiona una lista de contactos y su almacenamiento en un archivo."""

    def __init__(self, filename):
        """
        Inicializa el gestor de contactos con un archivo especificado.

        Args:
            filename (str): Ruta del archivo donde se guardarán los contactos.
        """

    def add_contact(self, contact):
        """Agrega un nuevo contacto a la lista de contactos."""


    def find_contact(self, name):
        """
        Busca un contacto por nombre.

        Args:
            name (str): Nombre del contacto a buscar.

        Returns:
            Contact: El contacto encontrado, o None si no se encuentra.
        """


    def save_contacts(self):
        """Guarda los contactos en el archivo especificado."""


    def load_contacts(self):
        """Carga los contactos desde el archivo especificado."""

```

### Probar el código generado

Para probar que el código está correcto lanza este comando en el directorio principal del proyecto:

```
python3 -m pytest tests/test_imc.py

python3 -m pytest tests/test_contacts.py
```

Si todo está correcto deberías ver en la consola lo siguiente:
```
collected 11 items                                                                                                        

tests/test_contacts.py ..... [ 45%]
tests/test_imc.py ......     [100%]

=================================================== 11 passed in 0.21s ====================================================
```