from modules.date_time_func import day_of_week, datetimestr_to_datetimeobj, time_difference_in_mins, is_weekend

class Counter():
  def __init__(self, start_time, end_time):
    self.current_time = datetimestr_to_datetimeobj(start_time)
    self.end_time = datetimestr_to_datetimeobj(end_time)
    self.current_day = day_of_week(self.current_time)
    self.total_shift_mins = time_difference_in_mins(
                                                    self.current_time, 
                                                    self.end_time
                                                  )
    # This variables will be modifided
    self.total_rate = 0
    self.time_left = time_difference_in_mins(
                                              self.current_time, 
                                              self.end_time
                                            )
    self.time_since_break = 0
    self.unused_break = 0

  def update_counter(self, current_time, total_rate, total_mins):
    self.total_rate += total_rate
    self.time_left -= total_mins
    self.current_time = current_time
    self.current_day = day_of_week(current_time)


  # checks if there is a break time due & will provide it
  def include_break_time(self, time_worked):
    # time since last break
    # unused break
    # time worked
    self.time_since_break += time_worked
    time_worked
    # Check if there is any unused break
    if self.unused_break > 0: 
      time_worked -=self.unused_break
      self.unused_break = 0
      self.time_since_break = 0
    
    # is there a break?
    # how much break time
  
    if self.time_since_break >= 480:
      break_used_now = min(self.time_since_break - 480, 60)
      self.unused_break = 60 - break_used_now

      self.time_since_break = self.time_since_break - break_used_now - 480

      return time_worked - break_used_now      
    return time_worked


  def shift_less_than_24hr(self):
    # Convert from mins to days
    time_diff = self.time_left/60/24

    if time_diff.days > 1:
      return False
      
    return True


  def extra_rate(self):
    total_time_mins = self.total_shift_mins - self.time_left
    total_time_days = total_time_mins/60/24
    if total_time_days > 1:
      return True
    
    return False


  def find_current_rate(self, current_timezone, current_day):
    return current_timezone.weekend_rate if is_weekend(current_day) else current_timezone.weekday_rate
  