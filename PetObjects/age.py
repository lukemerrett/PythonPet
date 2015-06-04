__author__ = 'Luke Merrett'

from random import randint
from Helpers import datehelper

class Age:
    __minimum_potential_lifespan_in_seconds = 86400  # 1 day
    __total_potential_lifespan_in_seconds = 31536000  # 1 year
    __birth_date = None
    __lifespan_in_seconds = None

    def __init__(self):
        self.__birth_date = datehelper.todays_date()

        self.__lifespan_in_seconds = randint(
            self.__minimum_potential_lifespan_in_seconds,
            self.__total_potential_lifespan_in_seconds)

    def current_age_in_seconds(self):
        """
        Gets the current age of the pet in seconds
        :return: The total age of the pet in seconds
        """
        return datehelper.get_total_seconds_difference(datehelper.todays_date(),self.__birth_date)

    def current_age_string(self):
        """
        Gets the age of the pet in a human readable string
        :return: A human readable form of the pets age
        """
        current_age = datehelper.get_difference_as_relative_delta(datehelper.todays_date(), self.__birth_date)
        return "Your pet is currently %d years %d months %d days %d hours %d minutes old" % (
            current_age.years,
            current_age.months,
            current_age.days,
            current_age.hours,
            current_age.minutes)

    def has_pet_reached_its_lifespan(self):
        """
        Returns a value indicating whether the pet has reached it's current lifespan
        :return: True if the pet is dead, false if the pet is still kicking around.
        """
        time_of_death = datehelper.add_seconds_to_date(self.__birth_date, self.__lifespan_in_seconds)
        return datehelper.is_date_earlier_than_today(time_of_death)