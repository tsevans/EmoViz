import filereader as fr
import graph_static_plotly as gsp
import graph_animated_plotly as gap

# def startSparkSession():
#     spark = SparkSession \
#         .builder \
#         .appName("EmoViz") \
#         .getOrCreate()

if __name__ == '__main__':
    csv = fr.find_file(1)
    df = fr.csv_to_spark_dataframe(csv)
