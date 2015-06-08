__author__ = 'Luke Merrett'

class PetStatus:
    has_reached_its_lifespan = None
    is_hungry = None
    needs_the_toilet = None
    name = None

    def __init__(self, has_reached_its_lifespan, is_hungry, needs_the_toilet, name):
        self.has_reached_its_lifespan = has_reached_its_lifespan
        self.is_hungry = is_hungry
        self.needs_the_toilet = needs_the_toilet
        self.name = name
