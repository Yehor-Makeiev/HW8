from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):
    birthday_boy = defaultdict(list)
    
    day_now = datetime.now()
    print(day_now)
    
    for d in users:
        for name, bd in dict(d).items():
                print(name, bd)

        
           
            
    


users = [{"name": "Yehor", "birthday": "1991, 3, 15"},
         {"name": "Vasyl", "birthday": "1992, 3, 16"},
         {"name": "Petya", "birthday": "1993, 3, 15"},
         {"name": "Kolya", "birthday": "1994, 3, 15"},
         {"name": "Stepan", "birthday": "1995, 3, 15"},
         {"name": "Petro", "birthday": "1996, 3, 15"},
         {"name": "Stas", "birthday": "1997, 3, 15"},
         {"name": "Ivan", "birthday": "1998, 3, 15"}]

if __name__ == "__main__":
    get_birthdays_per_week(users)
# pprint(users)