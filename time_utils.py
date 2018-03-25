import time


def convert_timestamp(time_string):
    """
    Convert a string timestamp to a python time object.

    :param time_string: Timestamp from 'time' column in datasheet.
    :return: Time object representing provided timestamp.
    """
    return time.strptime(time_string, '%H:%M:%S.%f')
