# def singleton(class_single):
#     instances = {}
#
#     def get_instance():
#         if class_single not in instances:
#             instances[class_single] = class_single()
#         return instances[class_single]
#
#     return get_instance

def singleton(classe_definie):
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance


@singleton
class TestSing:
    pass
