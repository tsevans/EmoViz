import os
from pyspark.sql import SQLContext
import fnmatch as fn
from spark_utils import create_local_spark_session
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


def csv_to_spark_dataframe(filepath):
    spark_context = create_local_spark_session()
    sql_context = SQLContext(spark_context)
    spark_df = sql_context.read.format('com.databricks.spark.csv').options(header='true').load(filepath.path)
    return spark_df


def csv_to_pandas_dataframe(filepath):
    pandas_df = pd.read_csv(filepath.path)
    return pandas_df


def pandas_to_spark(dataframe):
    spark_context = create_local_spark_session()
    return spark_context.createDataFrame(dataframe)


if __name__ == '__main__':
    path = get_path_from_id(1)
    print(csv_to_pandas_dataframe(path).head())
    #df = csv_to_spark_dataframe(path)
    #print('Dataframe Schema:')
    #df.printSchema()