# Logic-1: Exercise 6: alarm_clock
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
# Solved. Mistake(s) made: none. Improvement(s): instead of repeating 1 <= day <= 5, set it as a variable

def alarm_clock(day, vacation):
   is_weekday = 1 <= day <= 5
   if vacation:
       if is_weekday:
           return '10:00'
       return 'Off'
   if is_weekday:
       return '7:00'
   return '10:00'


if __name__ == "__main__":
    assert alarm_clock(1, False) == '7:00', "alarm_clock(1, False) should be '7:00'"
    assert alarm_clock(5, False) == '7:00', "alarm_clock(5, False) should be '7:00'"
    assert alarm_clock(0, False) == '10:00', "alarm_clock(0, False) should be '10:00'"
    print("All tests passed")
