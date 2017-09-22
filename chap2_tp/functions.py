import pickle
import random

from donee import FILE_NAME
from donee import LIST_MOT
import os.path

# function nead for file manage
# return the score of given name

def get_score(name):
    scores_dict = dict()
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'rb') as fichier:
            mon_deckle = pickle.Unpickler(fichier)
            try:
                scores_dict = mon_deckle.load()
            except:
                #TODO:fix it
                pass
        return scores_dict.get(name, 0)
    else:
        f = open(FILE_NAME, "wb")
        f.close()
        return 0


def set_score(name, score=0):
    scores_dict = dict()
    old_score = get_score(name)
    if old_score <= score or old_score == 0:
        with open(FILE_NAME, 'rb') as f:
            mon_deckle = pickle.Unpickler(f)
            try:
                scores_dict = mon_deckle.load()
            except:
                # TODO:fix it
                pass
        scores_dict[name] = score
        with open(FILE_NAME, 'wb') as f:
            mon_pickler = pickle.Pickler(f)
            mon_pickler.dump(scores_dict)


def clean_score():
    scores_dict = dict()
    with open(FILE_NAME, 'wb') as f:
        mon_pickler = pickle.Pickler(f)
        mon_pickler.dump(scores_dict)


# function of game


def get_world():
    return random.choice(LIST_MOT)


def play_letter(word, letter):
        res = ["*"] * len(word)
        for l in letter:
            positions = [pos for pos, char in enumerate(word) if char == l]
            for p in positions:
                res[p] = l
        return "".join(res)


def play_intro():
    print("*******hello and welcome to pendu game *********")
    name = input("pleas enter your name  ")
    return name
