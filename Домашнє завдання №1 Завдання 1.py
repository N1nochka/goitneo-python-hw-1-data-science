from collections import defaultdict
from datetime import datetime, timedelta
def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year.weekday() >= 5:
                weekday = 0
            else:
                weekday = birthday_this_year.weekday()
            birthdays_per_week[weekday].append(name)
    for weekday, names in birthdays_per_week.items():
        weekday_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][weekday] + ":"
        print(weekday_name, ", ".join(names))

users = [
    {"name": "Ivan Ivanov", "birthday": datetime(1980, 1, 1)},
    {"name": "Petr Petrov", "birthday": datetime(1983, 3, 5)},
    {"name": "Vasiliy Vasilev", "birthday": datetime(1985, 4, 10)},
    {"name": "Anton Antonov", "birthday": datetime(1987, 12, 10)},
    {"name": "Andrey Andreev", "birthday": datetime(1990, 7, 20)},
    {"name": "Bogdan Bogdanov", "birthday": datetime(1993, 9, 25)},
    {"name": "Ruslan Ruslanov", "birthday": datetime(1995, 10, 30)},
    {"name": "Myhail Myhailov", "birthday": datetime(2000, 12, 8)},
]
get_birthdays_per_week(users)