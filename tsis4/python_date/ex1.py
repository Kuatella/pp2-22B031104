import datetime as dt

def fiveDayBefore():
    return dt.datetime.now() - dt.timedelta(days = 5)

print(fiveDayBefore())