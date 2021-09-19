'''
For the functions that relate to date & time

Types of Date Time Format
1) Datetime - Used for tracking the date/days
2) Int(Format: HHMM) - For the Timezone rate 
3) Str - the orginal format that it comes in
'''
from datetime import datetime


# Converting "%Y-%m-%dT%H:%M:%S" string to a datetime obj
def datetimestr_to_datetimeobj(date_time_str):
  return datetime.strptime(date_time_str,"%Y-%m-%dT%H:%M:%S")


# take 2 datetime objects and returns the min time delta
def time_difference_in_mins(time_one, time_two):
  time_diff = time_two - time_one
  days = time_diff.days if time_diff.days > 0 else 0
  days_in_mins = days * 24 * 60 

  minutes = divmod(time_diff.seconds, 60)
  
  if minutes[1] != 0:  
    return int(minutes[0]) + 1 + days_in_mins
  
  return int(minutes[0]) + days_in_mins


# Get the current day of the week
def day_of_week(current_date_time):
  return current_date_time.weekday()


# Get the time str and convert it to a HHMM integer
def timestr_to_int(time_str):
  # All input will come in the form of 'HH:MM:SS'
  # Splits time into ['HH', "MM", 'SS']
  time_components = time_str.split(':')
  time_str = time_components[0] + mins_to_time_int(time_components[1])
  return int(time_str)


def date_time_to_int(date_time_obj):
  return int(date_time_obj.strftime("%H%M"))


def is_weekend(day_int):
  if day_int >= 5:
    return True
  return False


def time_int_to_mins(time_int):
  return (time_int / 100) * 60

def mins_to_time_int(time_int): 
  calculate_time = int(float(time_int) / 60 * 100)  
  return str(calculate_time).ljust(2,'0')