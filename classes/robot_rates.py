'''
Robot Rates is an class to store the rates data


Time Zone refers to the zone of the different rate that 
the robot user will have to pay
'''

from modules.date_time_func import timestr_to_int, date_time_to_int, time_difference_in_mins, time_int_to_mins


class RobotRates():
  def __init__(self, standard_day, standard_night, extra_day, extra_night):
    self.standard_day = TimeZone(
                                 standard_day['start'], 
                                 standard_day['end'], 
                                 standard_day['value']
                                )
    self.standard_night = TimeZone(
                                 standard_night['start'], 
                                 standard_night['end'], 
                                 standard_night['value']
                                )
    self.extra_day = TimeZone(
                                extra_day['start'], 
                                extra_day['end'], 
                                extra_day['value']
                              )
    self.extra_night = TimeZone(
                                  extra_night['start'], 
                                  extra_night['end'], 
                                  extra_night['value']
                                )
  
  
  def find_current_timezone(self, current_time, standard=True):
    # Check to see if it is a standard or extra day rate
    current_date_time = date_time_to_int(current_time)
    # Check if standard or extra rate
    if standard:
      # Check if it is Day rate
      if current_date_time >= self.standard_day.start_time and current_date_time < self.standard_day.end_time:
        # Return Time zone obj
        return self.standard_day
      # night rate
      else:
        return self.standard_night
    else:
      # Check if it is Day rate
      if current_date_time >= self.extra_day.start_time and current_date_time <= self.extra_day.end_time:
        return self.extra_day
      else:
        return self.extra_night


  # checking if this is the last 'timezone' that the robot ends 
  def last_timezone_before_end(self,current_time, end_time,time_left):
    time_diff = time_difference_in_mins(current_time, end_time)
    if time_diff <= time_left:
      return True
    return False


class TimeZone():
  def __init__(self, start_time, end_time, rate):
    self.start_time = timestr_to_int(start_time) 
    self.end_time = timestr_to_int(end_time)
    self.weekday_rate = rate
    self.weekend_rate = rate + 10
    self.cross_to_next_day = self._cross_to_next_day()
    self.timezone_len = self._timezone_len()
    

  def mins_to_change_rate(self, current_time):
    current_time_int = timestr_to_int(current_time.strftime('%H:%M'))
    time_diff = 0
    if self.cross_to_next_day:
      if current_time_int >= self.start_time and current_time_int < 2400: 
        time_diff = 2400 - current_time_int
      else:
        time_diff = self.end_time - current_time_int 
    else:
      time_diff = self.end_time - current_time_int
    return time_int_to_mins(time_diff)


  def _timezone_len(self):
    time_diff = self.end_time - self.start_time
    if self.cross_to_next_day:
      time_diff += 2400
    # convert time diff to mins
    time_diff_min = time_int_to_mins(time_diff)
    return time_diff_min

  
  def _cross_to_next_day(self):
    if self.start_time > self.end_time:
      return True
    
    return False