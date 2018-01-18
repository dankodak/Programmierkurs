# Aufgabe 1 Wochentag ermitteln
import calendar
# get_weekday estimates the weekday of a certain date
# INPUT: date - string of format DD.MM.YYYY
# OUTPUT: day - weekday of date as string "Monday", "Tuesday", ...
###

def get_weekday(date):
    d = date.split(".")
    dday = int(d [0])
    dmonth = int(d [1])
    dyear = int(d [2])
    weekday_number = calendar.weekday(dyear,dmonth,dday)
    day = weekdays[weekday_number]
    return day

weekdays = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3: "Thursday", 4:"Friday", 5: "Saturday", 6: "Sunday"}

date = "24.12.2017"
day = get_weekday(date)
print(day)