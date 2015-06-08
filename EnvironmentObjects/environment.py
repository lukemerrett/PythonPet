__author__ = 'Luke Merrett'

class Environment:
    __poop_level = None

    def __init__(self):
        self.__poop_level = 0

    def current_poop_level(self):
        return self.__poop_level

    def pet_has_pooped(self):
        self.__poop_level += 1

    def clean_up_poop(self):
        self.__poop_level = 0
