from datetime import datetime
from pprint import pprint


def get_birthdays_per_week(users):
    birthday_boy = {}
    day_now = datetime.now()
    print(day_now)
    
    for b in users:
        for i, v in b.items():
           
            if v.month == day_now.month and v.day == day_now.day:
                print(v)
                birthday_boy.update({v.strftime("%A"): str(i) })
            
    pass


users = [{"Yehor": datetime(2023, 3, 15)},
         {"Katya": datetime(1991, 4, 6)},
         {"Stas": datetime(1991, 9, 20)},
         {"4ort": datetime(1995, 3, 17)},
         {"Loh": datetime(2000, 3, 15)},
         {"Popey": datetime(2020, 3, 18)},
         {"Hren": datetime(2018, 3, 20)},
         {"kozel": datetime(2016, 3, 21)}]

if __name__ == "__main__":
    get_birthdays_per_week(users)
# pprint(users)