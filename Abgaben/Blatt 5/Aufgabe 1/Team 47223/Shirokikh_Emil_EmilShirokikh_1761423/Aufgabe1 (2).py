#Aufgabe 1               Emil Shirokikh
# kannst du mir bitte in den Kommentaren schreiben ob ich Computermathematik bereits bestanden habe?

import calendar
def get_weekday(date):

    weekdays = {0: "Montag", 1: "Dienstag", 2: "Mittwoch", 3: "Donerstag", 4: "Freitag", 5: "Samstag", 6: "Sonntag"}

    dateList = list(map(int, date.split(".")))

    print(weekdays[calendar.weekday(dateList[2], dateList[1], dateList[0])])


get_weekday("31.12.1999")





