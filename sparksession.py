from pyspark.sql import SparkSession as SS
from pyspark.conf import SparkConf
from pyspark.sql import SQLContext
import multiprocessing as mp


def csv_to_spark_dataframe(file_path, sesh):
    """
    Convert a csv file to a spark dataframe.
    :param file_path: File path object of the csv to convert.
    :param sesh: Spark session created for all conversions.
    :return: Spark dataframe created from the file.
    """
    spark = sesh.get_active_session()
    sql_context = SQLContext(sparkContext=spark.sparkContext, sparkSession=spark)
    spark_df = sql_context.read.format('com.databricks.spark.csv').options(header='true').load(file_path.path)
    return spark_df


def create_local_spark_session():
    """
    Create a spark session that runs on local machine, using all available cores if possible.

    :return: Reference to local spark session.
    """
    try:
        num_cores = mp.cpu_count()
    except NotImplementedError:
        num_cores = None
    print('Using ' + str(num_cores) + ' cores')
    master = 'local' if num_cores is None else 'local[{0}]'.format(num_cores)
    return SS.builder.master(master).config(conf=SparkConf()).appName('EmoViz').getOrCreate()


class SparkSesh(object):

    def __init__(self):
        self.spark_sesh = create_local_spark_session()

    def get_active_session(self):
        return self.spark_sesh
