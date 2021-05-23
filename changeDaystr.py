'''
    'date' =>'date - n days'
     type : str => str
'''

import time
import calendar


def getDaysBefore(date, dds):
    import datetime
    datetime_dt = str_to_datetime(date)
    time_delta = datetime.timedelta(days = dds) 
    new_dt = datetime_dt - time_delta 
    datetime_format = new_dt.strftime("%Y%m%d") 
    return datetime_format

def str_to_datetime(date):
    from datetime import datetime
    date_new_format = datetime.strptime(date, "%Y%m%d")
    return date_new_format

#-----------------------------------------------------1232211
'''
print(type(time_delta))
print(type(datetime_dt))
print(type(datetime_format))
'''

if __name__ == '__main__':
    #today1 = datetime.datetime.today()
    #today1 = datetime.strptime('20210520', "%Y%m%d")
    today1 = '20210520'
    print(today1)
    final = getDaysBefore(today1, 8) # 8 days before
    print(final)
