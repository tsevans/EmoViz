from pyspark.sql import SparkSession
import multiprocessing as mp

def create_spark_session():
    try:
        num_cores = mp.cpu_count()
    except NotImplementedError:
        num_cores = None

    master = 'local' if num_cores is None else 'local[{0}]'.format(num_cores)
    session = SparkSession.builder.master(master).config().appName('EmoViz').getOrCreate()


if __name__ == '__main__':
    create_spark_session()