import os
from pyspark.sql import SQLContext
import fnmatch as fn


def get_path_from_id(student_id):
    """
    Get the relative path for a specific student's csv.

    :param student_id: ID number of the csv file.
    :return: The path object for the csv file, None if file doesn't exist.
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
    if path is not None:
        if "Adjusted" in path:
            return FilePath(path, True)
        return FilePath(path)


def get_path_from_filename(filename):
    """
    Get the relative path for a specific student's csv.

    :param filename: Full name of the csv file.
    :return: The path object for the csv file, None if file doesn't exist.
    """
    full_path = 'data/'+filename
    if "Adjusted" in filename:
        return FilePath(full_path, True)
    return FilePath(full_path)


class FilePath:
    """ Class to represent path for student data file"""
    def __init__(self, path, adjusted=False):
        self.path = path
        self.is_adjusted = adjusted


def convert_to_dataframe(filepath):
    #Check if file is adjusted, if so do extra processing to normalize the adjustments for time
    #If not adjusted, continue


if __name__ == '__main__':
    print(get_path_from_id(1).path)
    print(get_path_from_id(22).path)
    print(get_path_from_id(99))
    print(get_path_from_filename('P01_Emotion.csv').is_adjusted)