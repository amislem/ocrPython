class PersonneOld(object):
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
        return self._address

    def _set_address(self, address):
        """setter for address"""
        self._address = address

    address = property(_get_address, _set_address)


class Counter:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Counter.objets_crees += 1

    def intervalle(self, borne_inf, borne_sup):
        """Générateur parcourant la série des entiers entre borne_inf et borne_sup.

        Note: borne_inf doit être inférieure à borne_sup"""

        borne_inf += 1
        while borne_inf < borne_sup:
            yield borne_inf
            borne_inf += 1


class Personne:
    """Classe représentant une personne"""

    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)


class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""

    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        self.nom = nom
        self.matricule = matricule

    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)
