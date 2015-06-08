__author__ = 'Luke Merrett'

from Helpers import datehelper

class HungerLevel:
    __seconds_until_hungry = 120  # 2 minutes
    __last_fed = None
    __bladder = None

    def __init__(self, bladder):
        self.__last_fed = datehelper.todays_date()
        self.__bladder = bladder

    def is_hungry(self):
        date_pet_is_hungry = datehelper.add_seconds_to_date(self.__last_fed, self.__seconds_until_hungry)
        return datehelper.is_date_earlier_than_today(date_pet_is_hungry)

    def feed_pet(self):
        self.__last_fed = datehelper.todays_date()
        self.__bladder.has_been_fed()
        print("Your pet has been fed")