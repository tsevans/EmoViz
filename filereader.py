import os
from pyspark.sql import SQLContext
import fnmatch as fn
from sparksession import *
import pandas as pd


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
    return None


def get_path_from_filename(filename):
    """
    Get the relative path for a specific student's csv.
    :param filename: Full name of the csv file.
    :return: The path object for the csv file, None if file doesn't exist.
    """
    full_path = 'data/'+filename
    if os.path.exists(full_path):
        if "Adjusted" in filename:
            return FilePath(full_path, True)
        return FilePath(full_path)
    return None


def find_file(identifier):
    """
    Wrapper to find a csv file by either id number or full name of file.
    :param identifier: Numerical ID of file or full name of file.
    :return: File path object corresponding to identifier.
    """
    if type(identifier) is int:
        path = get_path_from_id(identifier)
    else:
        path = get_path_from_filename(identifier)

    if path is None:
        raise ValueError('File not found: %s' % identifier)
    return path


class FilePath(object):
    """ Class to represent path for student data file"""
    def __init__(self, path, adjusted=False):
        self.path = path
        self.is_adjusted = adjusted


def csv_to_spark_dataframe(filepath):
    """
    Convert a csv file to a spark dataframe.
    :param filepath: File path object of the csv to convert.
    :return: Spark dataframe and the active spark session which was created.
    """
    sesh = SparkSesh()
    spark = sesh.get_active_session()
    sql_context = SQLContext(sparkContext=spark.sparkContext, sparkSession=spark)
    spark_df = sql_context.read.format('com.databricks.spark.csv').options(header='true').load(filepath.path)
    return spark_df, sesh


def csv_to_pandas_dataframe(filepath):
    """
    Convert a csv file to a pandas dataframe.
    :param filepath: File path object of the csv file to convert.
    :return: Pandas dataframe.
    """
    pandas_df = pd.read_csv(filepath.path)
    return pandas_df


# def pandas_to_spark(dataframe):
#     """
#     Convert a pandas dataframe to a spark dataframe.
#
#     :param dataframe: Pandas dataframe instance.
#     :return: Converted spark dataframe.
#     """
#     return spark_context.createDataFrame(dataframe)
