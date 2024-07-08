from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user['name']
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        
        # set upcoming_birthdays
        
        birthday_this_year = birthday.replace(year=today.year) # check if birthday this year
        
        if birthday_this_year < today: # check if birthday was already, add it to next year
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days # calculate days
        
        if 0 <= days_until_birthday <= 7: # check if this week
            congrat_date = birthday_this_year
            
            # check if Sat or Sun, add to next week
            if congrat_date.weekday() >= 5:  
                congrat_date += timedelta(days=(7 - congrat_date.weekday()))
            
            # append results
            upcoming_birthdays.append({
                "name": name,
                "congrat_date": congrat_date
            })
    
    return upcoming_birthdays

# Run
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Sam Porter Bridges", "birthday": "1992.07.09"},
    {"name": "Luke Skywalker", "birthday": "1988.07.13"},
]

def print_upcoming_birthdays(upcoming_birthdays):
    days_of_week = ["в Понеділок", "у Вівторок", "в Середу", "в Четвер", "в П'ятницю", "Субота", "Неділя"] # "Субота", "Неділя" are not used, just to easy things up
    months = ["січня", "лютого", "березня", "квітня", "травня", "червня", 
              "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]

    for birthday in upcoming_birthdays:
        name = birthday['name']
        date = birthday['congrat_date']
        day_of_week = days_of_week[date.weekday()]
        day = date.day
        month = months[date.month - 1]
        print(f"Привітати {name} {day_of_week}, {day} {month}")

upcoming_birthdays = get_upcoming_birthdays(users)
print_upcoming_birthdays(upcoming_birthdays)
