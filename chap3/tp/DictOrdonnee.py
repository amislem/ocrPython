class DictOrdonnee:
    def __init__(self, base={}, **kwargs):
        self._keys = list()
        self._values = list()

        if type(base) not in type(dict, DictOrdonnee):
            raise TypeError("the type of the based dictionary unsupported")

        for cle in base:
            self[cle] = base[cle]

        for cle in kwargs:
            self[cle] = kwargs[cle]

    def __del__(self):
        pass

    def __delitem__(self, key):

        return self[key]

    def __repr__(self):
        ch = "{"
        for key, value in self._keys, self._values:
            ch += '{0} : {1}, '.format(key, value)
        ch += "}"
        return ch

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, item):
        pass

    def __contains__(self, item):
        pass

    def __len__(self):
        """ Return the length of the dicionary Ordonnee"""
        return len(self._keys)

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        pass

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        pass
