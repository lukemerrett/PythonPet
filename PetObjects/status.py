__author__ = 'Luke Merrett'

class PetStatus:
    has_reached_its_lifespan = None
    is_hungry = None
    name = None

    def __init__(self, has_reached_its_lifespan, is_hungry, name):
        self.has_reached_its_lifespan = has_reached_its_lifespan
        self.is_hungry = is_hungry
        self.name = name
