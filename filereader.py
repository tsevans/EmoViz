import os
import fnmatch as fn
from sparksession import *
import database as db


def get_path_from_id(student_id, location=None):
    """
    Get the relative path for a specific student's csv.
    :param student_id: ID number of the csv file.
    :param location: Directory to search for file in, data_raw/ by default.
    :return: The path object for the csv file, None if file doesn't exist.
    """
    file_id = 'P'
    if student_id < 10:
        file_id += '0'
    file_id = file_id + str(student_id) + '_Emotion'
    dir_name = 'data_raw/' if location is None else location
    path = None
    for curr_file in os.listdir(dir_name):
        if fn.fnmatch(curr_file, file_id + '*.csv'):
            path = dir_name + curr_file
            break
    if path is not None:
        if "Adjusted" in path:
            return FilePath(path, True)
        return FilePath(path)
    return None


def get_path_from_filename(filename, location=None):
    """
    Get the relative path for a specific student's csv.
    :param filename: Full name of the csv file.
    :param location: Directory to search for file in, data_raw/ by default.
    :return: The path object for the csv file, None if file doesn't exist.
    """
    dir_name = 'data_raw/' if location is None else location
    full_path = dir_name+filename
    if os.path.exists(full_path):
        if 'Adjusted' in filename:
            return FilePath(full_path, True)
        return FilePath(full_path)
    return None


def find_file(identifier, dir_name=None):
    """
    Wrapper to find a csv file by either id number or full name of file
    stored in a local directory.
    :param identifier: Numerical ID of file or full name of file.
    :param dir_name: Name of directory to find file. Default location is data_raw/.
    :return: File path object corresponding to identifier.
    """
    if type(identifier) is int:
        if dir_name is None:
            path = get_path_from_id(identifier)
        else:
            path = get_path_from_id()
    else:
        path = get_path_from_filename(identifier)

    if path is None:
        raise ValueError('File not found: %s' % identifier)

    return path


class FilePath(object):
    """ Class to represent path for student data_raw file"""
    def __init__(self, path, adjusted=False):
        self.path = path
        self.is_adjusted = adjusted


def check_fast_path(key):
    """
    Checks shelf database for already processed CsvRecord object.
    :param key: Key to access file,
    :return:
    """
    print('Checking fast path for file ' + str(key) + ' in local processed index.')
    if type(key) is not int:
        # Parse int from filename if provided key was file name (and not number)
        key = int(filter(str.isdigit, key))
    if db.contains(key):
        print('File was found in fast path!')
        return db.read(key)
    print('File not found in fast path.')
    return None


def check_slow_path(key):
    """
    Checks data_raw/ directory for path to unprocessed file.
    :param key: Key to find file.
    :return:
    """
    print('Checking slow path for file ' + str(key) + ' in unprocessed directory.')
    file_path = find_file(key)


def load_dataframes(file_id):
    """
    Loads csv file(s) as spark dataframe(s).
    :param file_id: Single file reference or list of file references - either name or number.
    :return: Spark dataframe(s) from provided files and session that created them.
    """
    # Create single instance of spark session used to process all files.
    sesh = SparkSesh()

    frames = []

    # Loop over each file that will be included in the visualization
    for ref in file_id:
        # record = check_fast_path(ref)
        # if record is None:
        #     record = check_slow_path(ref)
        record = 'data_proc/' + ref
        curr_frame = csv_to_spark_dataframe(record, sesh)
        frames.append(curr_frame)
    return frames, sesh
