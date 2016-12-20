# coding=utf8

"""
time util.
"""

__author__ = 'didicout <i@julin.me>'


import time
import datetime


def date_str_2_stamp(date_str, millisecond=False):
    if millisecond:
        return int(time.mktime(time.strptime(date_str, '%Y-%m-%d'))) * 1000
    else:
        return int(time.mktime(time.strptime(date_str, '%Y-%m-%d')))


def time_str_2_stamp(time_str, millisecond=False):
    if millisecond:
        return int(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))) * 1000
    else:
        return int(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')))


def datetime_var_2_stamp(datetime_var, millisecond=False):
    if millisecond:
        return int(time.mktime(datetime_var.timetuple())) * 1000
    else:
        return int(time.mktime(datetime_var.timetuple()))


def time_var_2_stamp(time_var, millisecond=False):
    time_var = standardize_time(time_var)
    if millisecond:
        return int(time_var) * 1000
    else:
        return int(time_var)


def stamp_2_date_str(stamp, millisecond=False):
    if millisecond:
        stamp /= 1000
    return time.strftime('%Y-%m-%d', time.localtime(stamp))


def stamp_2_datetime_str(stamp, millisecond=False):
    if millisecond:
        stamp /= 1000
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))


def time_str_2_date_str(time_str):
    return stamp_2_date_str(time_str_2_stamp(time_str))


def datetime_2_date_str(datetime_var):
    return stamp_2_date_str(datetime_var_2_stamp(datetime_var))


def time_2_date_str(time_var):
    return stamp_2_date_str(time_var_2_stamp(time_var))


def time_2_datetime_str(time_var):
    return stamp_2_datetime_str(time_var_2_stamp(time_var))


def time_minus_by_str(time_str1, time_str2):
    return int(time.mktime(standardize_time(time_str1)) - time.mktime(standardize_time(time_str2)))


def date_range(date_str1, date_str2, step=1):
    ret = []
    step_seconds = 3600 * 24 * step
    for i in range(date_str_2_stamp(date_str1), date_str_2_stamp(date_str2) + 1, step_seconds):
        ret.append(stamp_2_date_str(i))
    return ret


def get_monday_str(date_str):
    datetime_var = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    monday = datetime_var - datetime.timedelta(days=datetime_var.weekday())
    return datetime_2_date_str(monday)


def get_month_first_day_str(date_str):
    datetime_var = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    first_day = datetime_var - datetime.timedelta(days=datetime_var.day - 1)
    return datetime_2_date_str(first_day)


def get_today_str():
    return datetime.date.today().strftime('%Y-%m-%d')


def get_yesterday_str():
    return (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')


def get_yesterday_str_by_date_str(date_str):
    stamp = date_str_2_stamp(date_str) - 24 * 3600
    return stamp_2_date_str(stamp)


def get_tomorrow_str():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')


def day_minus_by_date_str(date_str1, date_str2):
    tmp = date_str1.split('-')
    a = datetime.datetime(int(tmp[0]), int(tmp[1]), int(tmp[2]))
    tmp = date_str2.split('-')
    b = datetime.datetime(int(tmp[0]), int(tmp[1]), int(tmp[2]))
    return (a-b).days


def get_stamp_of_week(stamp, millisecond=False):
    """
        get the stamp of monday morning of the week
        取时间戳stamp所在周周一00：00：00的时间戳
    """
    date_str = stamp_2_date_str(stamp, millisecond)
    monday_str = get_monday_str(date_str)
    return date_str_2_stamp(monday_str, millisecond)


def get_stamp_of_month(stamp, millisecond=False):
    """
        get the stamp of the first day morning of the month
        取时间戳stamp所在月1号0点的时间戳
    """
    date_str = stamp_2_date_str(stamp, millisecond)
    first_day = get_month_first_day_str(date_str)
    return date_str_2_stamp(first_day, millisecond)


def standardize_time(time_var):
    """
        avoid error when time has a time zone.
    """
    return time.strptime(datetime.datetime.strftime(time_var, '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print get_yesterday_str_by_date_str('2014-05-01')