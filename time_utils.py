import time


def convert_timestamp(time_string):
    """
    Convert a string timestamp to a python time object.
    :param time_string: Timestamp from 'time' column in data_raw sheet.
    :return: Time object representing provided timestamp.
    """
    return time.strptime(time_string, '%H:%M:%S.%f')


def compose_timestamp(min, sec, millis):
    """
    Create a timestamp from the minute, second, and millisecond columns of a csv.
    :param min: Minute to add to the timestamp.
    :param sec: Second to add to the timestamp
    :param millis: Millisecond to add to the timestamp.
    :return: Timestamp formatted to reflect the 'time' column of provided CSV files.
    """
    stamp = ('00:0%s:' % min) if int(min) <= 9 else ('00:%s:' % min) # Add minute
    stamp += ('0%s' % sec) if int(sec) <=9 else str(sec)  # Add second
    stamp += '.'
    for s in range(3-len(str(millis).strip())):
        stamp += '0'
    stamp += str(millis).strip()  # Add millisecond
    return stamp
