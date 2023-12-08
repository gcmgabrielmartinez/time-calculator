import math

def add_time(start, duration, start_day = "Not given" ):

  #split start into time and period of the day
  start_time, start_period = start.split()
  
  #split the start time into hours and minutes
  start_hour, start_minute = start_time.split(":")

  #split duration into hours and minutes
  duration_hour, duration_minute = duration.split(":")

  #convert start_hour and start_minute to float
  start_hour = float(start_hour) 
  start_minute = float(start_minute)
  duration_hour = float(duration_hour)
  duration_minute = float(duration_minute)

  if start_period == "PM":
    start_hour += 12

  #convert minutes to hour
  start_minute = start_minute/60
  duration_minute = duration_minute/60

  #sum everything
  start_to_finish = start_hour + duration_hour + start_minute + duration_minute

  #format hours
  finish_hour = int(start_to_finish % 24)
  finish_period = "AM"
  
  if finish_hour >= 12:
    finish_period = "PM"
    if finish_hour > 12:
      finish_hour -= 12
      
  elif finish_hour < 1:
    finish_hour += 12
  
  finish_minute = round(start_to_finish % 1 * 60)

  #get days later
  days = math.ceil(start_to_finish/24 - 1)
  
  if start_day == "Not given":
    days_str = ""
  else:
    start_day = start_day.capitalize()
    #get day of week
    week_dict = dict()
    week_dict["Monday"] = 0
    week_dict["Tuesday"] = 1
    week_dict["Wednesday"] = 2
    week_dict["Thursday"] = 3
    week_dict["Friday"] = 4
    week_dict["Saturday"] = 5
    week_dict["Sunday"] = 6
    
    start_day_num = week_dict[start_day]

    finish_week_day = (start_day_num + days) % 7

    for week_day, value in week_dict.items():
      if value == finish_week_day:
        days_str = ", "+ week_day 
        break
  
  if days == 1:
    days_str += " (next day)"
  elif days > 1:
    days_str += f" ({days} days later)"
  else:
    days_str += ""


  new_time = f"{finish_hour}:{finish_minute:02} {finish_period}" + days_str

  
  
  return new_time