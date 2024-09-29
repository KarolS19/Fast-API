from datetime import date, timedelta

def get_next_7_days():
    today = date.today()
    next_week = today + timedelta(days=7)
    return today, next_week
