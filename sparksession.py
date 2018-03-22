from pyspark.sql import SparkSession as SS
from pyspark.conf import SparkConf
import multiprocessing as mp


def create_local_spark_session():
    """
    Create a spark session that runs on local machine, using all available cores if possible.

    :return: Reference to local spark session.
    """
    try:
        num_cores = mp.cpu_count()
    except NotImplementedError:
        num_cores = None
    master = 'local' if num_cores is None else 'local[{0}]'.format(num_cores)
    return SS.builder.master(master).config(conf=SparkConf()).appName('EmoViz').getOrCreate()


class SparkSesh(object):

    def __init__(self):
        self.spark_sesh = create_local_spark_session()
