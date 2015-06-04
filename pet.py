__author__ = 'Luke Merrett'

from datetime import datetime
from dateutil.relativedelta import relativedelta

class Pet:
    birthDate = None

    def __init__(self):
        pass

    def hatch(self):
        self.birthDate = self.__todays_date()
        pass

    def current_age(self):
        return (self.__todays_date() - self.birthDate).total_seconds()

    def current_age_string(self):
        current_age = relativedelta(self.__todays_date(), self.birthDate)
        return "Your pet is currently %d years %d months %d days %d hours %d minutes old" % (
            current_age.years,
            current_age.months,
            current_age.days,
            current_age.hours,
            current_age.minutes)

    @staticmethod
    def __todays_date():
        return datetime.now()
