from datetime import datetime, timedelta

users = [{
    "Andrii": datetime(2002, 5, 29),
    "Valeriya": datetime(1998, 11, 19),
    "Oleksandr": datetime(1966, 6, 3)
}, {"Oksana": datetime(1977, 5, 31),
    "Vladislav": datetime(2002, 12, 21),
    "Valentin": datetime(2003, 5, 29),
    "Dmitro": datetime(2002, 8, 10)}]


def get_birthdays_per_week(users):

    result = []
    new_users_dict = {}
    new_users_list = []

    for j in users:
        for k, v in j.items():
            new_users_dict[k] = v
            new_users_list.append(k)

    birthday_dict = {}

    now = datetime.now()
    day_now = now.weekday()

    if day_now != 0:
        plus_day_to_zero_week = 7 - day_now
        weeks_interval = timedelta(days=plus_day_to_zero_week)
        now += weeks_interval

    for i in new_users_list:

        x = new_users_dict.get(i).replace(year=now.year)
        day_on_this_week_or_no = x.date() - now.date()

        if timedelta(days=0) <= day_on_this_week_or_no <= timedelta(days=6):

            if day_on_this_week_or_no == timedelta(days=0):
                day_on_this_week_or_no = "Monday"
            elif day_on_this_week_or_no == timedelta(days=1):
                day_on_this_week_or_no = "Tuesday"
            elif day_on_this_week_or_no == timedelta(days=2):
                day_on_this_week_or_no = "Wednesday"
            elif day_on_this_week_or_no == timedelta(days=3):
                day_on_this_week_or_no = "Thursday"
            elif day_on_this_week_or_no == timedelta(days=4):
                day_on_this_week_or_no = "Friday"
            elif day_on_this_week_or_no == timedelta(days=5):
                day_on_this_week_or_no = "Monday"
            elif day_on_this_week_or_no == timedelta(days=6):
                day_on_this_week_or_no = "Monday"

            if not birthday_dict.get(day_on_this_week_or_no):
                birthday_dict[day_on_this_week_or_no] = [i]
            else:
                birthday_dict[day_on_this_week_or_no].append(i)

    for k, v in birthday_dict.items():
        list_users_res = ", ".join(v)
        result.append(f"{k}: {list_users_res}")

    res_result = "\n".join(result)

    return res_result


print(get_birthdays_per_week(users))
