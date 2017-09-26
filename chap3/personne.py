class Personne(object):
    """" Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self):
        """ this is simple init for personne """
        self.nom = "Tony"
        self.prenom = "Spart"
        self.age = 32
        self._address = "any ware"

    def _get_address(self):
        """Return the address of the person"""
        print("hello from getter")
        return self._address

    def _set_address(self, address):
        """setter for address"""
        print("hello from setter")
        self._address = address

    address = property(_get_address, _set_address)


class Counter:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Counter.objets_crees += 1
