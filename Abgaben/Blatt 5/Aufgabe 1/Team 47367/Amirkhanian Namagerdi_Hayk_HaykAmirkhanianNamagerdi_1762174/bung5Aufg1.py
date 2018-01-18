import calendar
def Tag(dd,mm,yyyy):
    g = calendar.weekday(yyyy,mm,dd)
    if g == 6:
        return "Sonntag"
    elif g == 0:
        return "Montag"
    elif g == 1:
        return "Dienstag"
    elif g == 2:
        return "Mittwoch"
    elif g == 3:
        return "Donnerstag"
    elif g == 4:
        return "Freitag"
    elif g == 5:
        return "Samstag"
print(Tag(24,12,2017))