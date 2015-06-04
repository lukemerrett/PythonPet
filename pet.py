__author__ = 'Luke Merrett'

from datetime import datetime
from dateutil.relativedelta import relativedelta
from random import random

class Pet:
    minimum_potential_lifespan_in_seconds = 86400  # 1 day
    total_potential_lifespan_in_seconds = 31536000  # 1 year
    birth_date = None
    lifespan_in_seconds = None

    def __init__(self):
        pass

    def hatch(self):
        self.birth_date = self.__todays_date()

        self.lifespan_in_seconds = random.randint(
            self.minimum_potential_lifespan_in_seconds,
            self.total_potential_lifespan_in_seconds)

    def current_age(self):
        return (self.__todays_date() - self.birth_date).total_seconds()

    def current_age_string(self):
        current_age = relativedelta(self.__todays_date(), self.birth_date)
        return "Your pet is currently %d years %d months %d days %d hours %d minutes old" % (
            current_age.years,
            current_age.months,
            current_age.days,
            current_age.hours,
            current_age.minutes)

    @staticmethod
    def __todays_date():
        return datetime.now()
