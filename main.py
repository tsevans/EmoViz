from pyspark.sql import SparkSession

def startSparkSession():
    spark = SparkSession \
        .builder \
        .appName("EmoViz") \
        .getOrCreate()

if __name__ == '__main__':
    print('Running main function...')