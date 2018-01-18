import calendar


def get_weekday(date):
    the_weekday = calendar.weekday(int(date[-4:]), int(date[3:5]), int(date[:2]))
    if the_weekday == 0:
        return "Monday"
    elif the_weekday == 1:
        return "Tuesday"
    elif the_weekday == 2:
        return "Wednesday"
    elif the_weekday == 3:
        return "Thursday"
    elif the_weekday == 4:
        return "friday"
    elif the_weekday == 5:
        return "Saturday"
    elif the_weekday == 6:
        return "Sunday"


d = "06.11.1988"
print("Year: {}".format(int(d[-4:])))
print("Month: {}".format(int(d[3:5])))
print("Day: {}".format(int(d[:2])))
print("The corresponding weekday is: {}".format(get_weekday(d)))

