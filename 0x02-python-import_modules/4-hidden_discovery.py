#!/usr/bin/python3

"""Prog to print names defined by the compiled module hidden_4.pyc"""

if __name__ == "__main__":

    from hidden_4 import *
    name_list = dir()
    for name in (name_list):
        if name[0] != '_' and name[1] != '_':
            print(name)
