from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):

    birthday_boy = defaultdict(list)
    day_now = datetime.now()
    d_n_w = day_now.strftime('%A')
    delta = timedelta(days=1)

    print(f"\nToday is: {d_n_w}\n")

    for d in users:
        date_b = datetime.strptime(d["birthday"], "%d, %m, %Y")

        if date_b.day == day_now.day:
            birthday_boy[d_n_w].append(d["name"])

    for _ in range(6):
        day_now = day_now + delta
        wek = day_now.strftime('%A')

        for d in users:
            date_b = datetime.strptime(d["birthday"], "%d, %m, %Y")

            if date_b.day == day_now.day:

                if day_now.weekday() == 5 or day_now.weekday() == 6:
                    wek = "Monday"
                    birthday_boy[wek].append(d["name"])

                else:
                    birthday_boy[wek].append(d["name"])

    print(" Please don't forget to say happy birthday")
    for i, v in birthday_boy.items():
        print(f"{i}: {str(', '.join(v))}")
    pass


users = [{"name": "Yehor", "birthday": "15, 3, 1991"},
         {"name": "Vasyl", "birthday": "16, 3, 1992"},
         {"name": "Petya", "birthday": "17, 3, 1993"},
         {"name": "Kolya", "birthday": "18, 3, 1994"},
         {"name": "Stepan", "birthday": "19, 3, 1995"},
         {"name": "Petro", "birthday": "20, 3, 1996"},
         {"name": "Stas", "birthday": "21, 3, 1997"},
         {"name": "Ivan", "birthday": "22, 3, 1998"}]

if __name__ == "__main__":
    get_birthdays_per_week(users)
# pprint(users)
