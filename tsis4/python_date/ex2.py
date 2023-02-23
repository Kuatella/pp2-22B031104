import datetime as dt

def yesterdayToTomorrow():
    yesterday = dt.datetime.now() - dt.timedelta(days = 1)
    today = dt.datetime.now()
    tommorow = dt.datetime.now() + dt.timedelta(days = 1)
    
    return [yesterday, today, tommorow]

a, b, c = yesterdayToTomorrow()

print(a, b, c)