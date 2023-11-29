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
        self.filename = filename
        self.contacts = []

    def add_contact(self, contact):
        """Agrega un nuevo contacto a la lista de contactos."""
        self.contacts.append(contact)

    def find_contact(self, name):
        """
        Busca un contacto por nombre.

        Args:
            name (str): Nombre del contacto a buscar.

        Returns:
            Contact: El contacto encontrado, o None si no se encuentra.
        """
        for contact in self.contacts:
            if contact.nombre == name:
                return contact
        return None

    def save_contacts(self):
        """Guarda los contactos en el archivo especificado."""
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(str(contact) + "\n")

    def load_contacts(self):
        """Carga los contactos desde el archivo especificado."""
        with open(self.filename, 'r') as file:
            for line in file:
                nombre, telefono, email = line.strip().split(',')
                self.contacts.append(Contact(nombre, telefono, email))

