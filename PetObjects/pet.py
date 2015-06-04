__author__ = 'Luke Merrett'

from PetObjects.status import PetStatus
from PetObjects.age import Age

class Pet:
    Age = None

    def __init__(self):
        pass

    def hatch(self):
        """
        Sets the birth date and total potential age of the pet
        """
        self.Age = Age()

    def get_pets_status(self):
        """
        Returns an object outlining the status of the pet
        :return: An object showing the status of the pet
        """
        return PetStatus(self.Age.has_pet_reached_its_lifespan())