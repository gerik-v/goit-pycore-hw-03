from datetime import datetime

def get_days_from_today(date):
    today = datetime.now().date() # get today
    input_date = datetime.strptime(date, '%Y-%m-%d').date() # convert to datetime object
    interval = today - input_date
    return interval.days

input_date = input("Введіть дату в форматі YYYY-MM-DD")
print(get_days_from_today(input_date))