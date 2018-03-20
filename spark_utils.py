from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
import multiprocessing as mp


def create_local_spark_session():
    try:
        num_cores = mp.cpu_count()
    except NotImplementedError:
        num_cores = None
    master = 'local' if num_cores is None else 'local[{0}]'.format(num_cores)
    session = SparkSession.builder.master(master).config(conf=SparkConf()).appName('EmoViz').getOrCreate()
    return session
