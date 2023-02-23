import datetime as dt

def dropMs(date):
    new_date = date.replace(microsecond = 0)
    return new_date

def dif_in_Sec(f_date, s_date):
    delta = dropMs(f_date) - dropMs(s_date)
    return abs(delta.total_seconds())


date = dt.datetime(year= 2004, month= 5, day= 13, minute= 49, second= 1, microsecond= 6666)

print(dif_in_Sec(date, dt.datetime.now()))