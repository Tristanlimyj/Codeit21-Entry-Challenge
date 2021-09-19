import unittest
from datetime import datetime
from modules.date_time_func import *


class TestDateTimeFunc(unittest.TestCase):

  def test_datetimestr_to_datetimeobj(self):
    date_time_obj = datetimestr_to_datetimeobj("2038-01-01T20:15:00")
    correct_date_time_obj = datetime(2038,1,1,20,15,00)

    self.assertEqual(date_time_obj, correct_date_time_obj)


  def test_time_difference_in_mins(self):
    time_one = datetime(2038,1,1,10,00,00)
    time_two = datetime(2038,1,1,10,10,10)
    time_diff = time_difference_in_mins(time_one, time_two)
    # Answer is 11 cause i round up all the seconds
    self.assertEqual(time_diff, 11)


  def test_day_of_week(self):
    test_date = datetime(2021,9,12,10,10,10)
    
    test_day_of_week = day_of_week(test_date)  

    # Sunday so 6
    self.assertEqual(test_day_of_week, 6)


  def test_date_time_to_int(self):
    date_time_test_obj = datetime(2038,1,1,10,00,00)
    date_time_int = date_time_to_int(date_time_test_obj)

    self.assertEqual(date_time_int, 1000)

if __name__ == "__main__":
  unittest()