__author__ = 'Luke Merrett'

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def add_seconds_to_date(date, seconds):
    return date + timedelta(seconds=seconds)

def is_date_earlier_than_today(date):
    return date <= todays_date()

def get_difference_as_relative_delta(latest_date, earliest_date):
    return relativedelta(latest_date, earliest_date)

def get_total_seconds_difference(latest_date, earliest_date):
    return (latest_date - earliest_date).total_seconds()

def todays_date():
    return datetime.now()
