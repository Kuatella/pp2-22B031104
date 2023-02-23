import datetime as dt

def dropMs(date):
    new_date = date.replace(microsecond = 0)
    return new_date

date = dt.datetime(year= 2004, month= 5, day= 13, minute= 49, second= 1, microsecond= 6666)

print(dropMs(date))