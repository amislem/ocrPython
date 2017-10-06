from os import listdir
from os.path import join, isfile
from chap3.Roboc.Const import CART_PEACES


class Maps:
    """ Class for reading map io"""
    _walls = []
    _ports = []

    def __init__(self, dir_maps):
        """Read the list of the maps"""
        self._maps = [f for f in listdir(dir_maps) if isfile(join(dir_maps, f)) and f.endswith(".txt")]

    def _get_maps(self):
        """Return the list name of the maps"""
        return self._maps

    list_map = property(_get_maps)

    def get_map(self, map_name):
        """ Read the file of the map and return all x y of any piace of the map
                return 2 list of tuples of x and y walls and ports
                return 2 tuple of xy of exit port and the bot xy
        """

        # ports = []
        # exit_ports = []
        # bot = []
        # print("hello")
        y = 0
        with open("cartes/" + map_name + ".txt") as f:
            for line in f:
                x = 0
                for char in line:
                    if char == CART_PEACES["wall"]:
                        self._walls.append((x, y))
                    elif char == CART_PEACES["port"]:
                        self._ports.append((x, y))
                    elif char == CART_PEACES["exit"]:
                        self._exit = (x, y)
                    elif char == CART_PEACES["bot"]:
                        self._bot = (x, y)
                    x += 1
                print(line, end="")
            y += 1
        return 1, 1, 1, 1


class Map:
    """Chosen map methodes"""

    def __init__(self, map_name):
        self._walls, self._ports, self._exit_port, self._bot = Maps.get_map(map_name=map_name)



class Bot:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _get_x(self):
        return self._x

    def _set_x(self, x):
        self._x = x

    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._y

    def _set_y(self, y):
        self._y = y

    y = property(_get_y, _set_y)


class Port:
    pass


class ExitPort:
    pass


class wall:
    pass
