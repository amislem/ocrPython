import time


def my_decorator(function):
    def return_function():
        print("we will call function {}".format(function))
        return function()

    return return_function


@my_decorator
def my_function():
    print("hello from my function")


def controler_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""

    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appelé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""

        def fonction_modifiee(*args,**kwargs):
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""

            tps_avant = time.time()  # Avant d'exécuter la fonction
            valeur_renvoyee = fonction_a_executer(*args,**kwargs)  # On exécute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format( \
                    fonction_a_executer, tps_execution))
            return valeur_renvoyee

        return fonction_modifiee

    return decorateur


@controler_temps(5)
def read_input(name="---------"):
    print(name)
    return input("whats you name : ")


if __name__ == "__main__":
    # print(type(my_function))
    read_input("islem")
    # pass
