import calendar
from datetime import datetime


class Period():
    def __init__(self):
        pass


actual_year = datetime.now().year
actual_month = datetime.now().month
actual_day = datetime.now().day

day_name = calendar.day_name
month_name = calendar.month_name

# print(calendar.month(actual_year, actual_month))
print(f"day: {day_name},\nmonth: {month_name}")
#print(calendar.week(5, 5))
