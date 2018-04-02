import time


def convert_timestamp(time_string):
    """
    Convert a string timestamp to a python time object.
    :param time_string: Timestamp from 'time' column in data sheet.
    :return: Time object representing provided timestamp.
    """
    return time.strptime(time_string, '%H:%M:%S.%f')


def compose_timestamp(min, sec, millis):
    """
    Create a timestamp from the minute, second, and millisecond columns of a csv.
    :param min:
    :param sec:
    :param millis:
    :return: Timestamp formatted to reflect the 'time' column of provided CSV files.
    """
    # Minute formatting
    if min > 9:
        # Handle double-digit stuff here
    else:
        # Just format single digit stuff


    stamp = '00:00:00.000'