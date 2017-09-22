
from functions import *


def afficher(*values, sep=" ", end="\n"):
    ch_list = list(values)
    for v in enumerate(ch_list):
        ch_list[v[0]] = str(v[1])
    ch = sep.join(ch_list)
    print(ch, end=end)


def main():
    name = play_intro()
    world = get_world()
    letters = list()
    i = 8
    while i >= 0:
        letters.append(input("pleas enter a letter "))
        played = play_letter(world, letters)
        print(played)
        if played == world:
            break
        i -= 1
    set_score(name, get_score(name)+i)
    print("now {0} you have {1} and the letter was {2}".format(name, get_score(name), world))


if __name__ == "__main__":
    main()
