__author__ = 'Luke Merrett'


class Bladder:
    __bladder_level = None
    __bursting_level = 5
    __environment = None

    def __init__(self, environment):
        self.__bladder_level = 0
        self.__environment = environment

    def has_been_fed(self):
        self.__bladder_level += 1

    def needs_the_toilet(self):
        return self.__bladder_level >= self.__bursting_level

    def go_to_toilet(self):
        self.__bladder_level = 0
        self.__environment.pet_has_pooped()
