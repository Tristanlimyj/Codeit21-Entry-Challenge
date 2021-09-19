'''
Assumptions
  - Weekends have a $10 per min surcharge
  - if more than 24hrs it will be considered an extra day
  -  Seconds will be round up to the nearest min
'''
from classes.robot_rates import RobotRates
from classes.counter import Counter
from datetime import timedelta
from tests.input_test import *

def rate_calculator(robot_work_data) -> dict:
  # get the rate & shift details
  rates_data, shift_data = robot_work_data['roboRate'], robot_work_data['shift']
  # Create Shift Robo Rates & Counter Obj
  robot_rates = RobotRates(
                            rates_data['standardDay'],
                            rates_data['standardNight'],
                            rates_data['extraDay'],
                            rates_data['extraNight']
                          )
  counter = Counter(shift_data['start'],shift_data['end'])

  # Check if it counter is 0
  while counter.time_left != 0:
    # Get current rate obj
    current_timezone = robot_rates.find_current_timezone(counter.current_time)
    # Weekday or weekend
    current_rate = counter.find_current_rate(current_timezone, counter.current_day)
    # Change Rate Time
    mins_to_change_rate = current_timezone.mins_to_change_rate(counter.current_time)
    # time diff counter time left and change rate hr
    time_worked = mins_to_change_rate
    if counter.time_left <= mins_to_change_rate:
      time_worked = counter.time_left
    # use time_worked from above
    time_worked_including_break = counter.include_break_time(time_worked)

    total_rate = time_worked_including_break * current_rate
    total_mins = time_worked
    total_seconds = total_mins * 60

    current_time = counter.current_time + timedelta(0, seconds=total_seconds)
    # update counter
    counter.update_counter(current_time, total_rate, total_mins)
  return {"value" : int(counter.total_rate)}



if __name__ == "__main__":
  '''print('Input Set 1:', rate_calculator(input_set_1))
  print('Input Set 2:', rate_calculator(input_set_2))
  print('Input Set 3:', rate_calculator(input_set_3))
  print('Input Set 4:', rate_calculator(input_set_4))'''
  print('Input Set 5:', rate_calculator(input_set_5))