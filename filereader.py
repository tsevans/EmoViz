import os
from pyspark import SparkContext
import fnmatch as fn


def get_path_from_id(student_id):
    """
    Get the relative path for a specific student's csv.

    :param student_id: ID number of the csv file.
    :return: The relative path of the csv file, None if file doesn't exist.
    """
    file_id = 'P'
    if student_id < 10:
        file_id += '0'
    file_id = file_id + str(student_id) + '_Emotion'
    path = None
    for file in os.listdir('data/'):
        if fn.fnmatch(file, file_id + '*.csv'):
            path = 'data/' + file
            break
    return path


if __name__ == '__main__':
    print(get_path_from_id(1))
    print(get_path_from_id(22))
    print(get_path_from_id(99))
