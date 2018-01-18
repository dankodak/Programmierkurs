import datetime

def get_weekday(day, month, year):
    d = datetime.date(year, month, day)
    day = d.weekday()
    if day == 6:
        w_day = 'sonntag'
    elif day == 0:
        w_day = 'Montag'
    elif day == 1:
        w_day = 'Dienstag'
    elif day == 2:
        w_day = 'Mittwoch'
    elif day == 3:
        w_day = 'Donnerstag'
    elif day == 4:
        w_day = 'Feitag'
    else:
        w_day = 'Samstag'
    return w_day
