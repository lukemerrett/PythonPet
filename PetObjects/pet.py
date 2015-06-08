__author__ = 'Luke Merrett'

from PetObjects.status import PetStatus
from PetObjects.age import Age
from PetObjects.bladder import Bladder
from PetObjects.hunger import HungerLevel

class Pet:
    Age = None
    HungerLevel = None
    Name = None
    Bladder = None

    def __init__(self):
        pass

    def hatch(self, name):
        """
        Sets the original details for the pet
        """
        self.Age = Age()
        self.Bladder = Bladder()
        self.HungerLevel = HungerLevel(self.Bladder)
        self.Name = name

    def get_pets_status(self):
        """
        Returns an object outlining the status of the pet
        :return: An object showing the status of the pet
        """
        return PetStatus(
            self.Age.has_pet_reached_its_lifespan(),
            self.HungerLevel.is_hungry(),
            self.Bladder.needs_the_toilet(),
            self.Name)