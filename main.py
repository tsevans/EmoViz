import filereader as fr
import graph_static_plotly as gsp
import graph_animated_plotly as gap

# def startSparkSession():
#     spark = SparkSession \
#         .builder \
#         .appName("EmoViz") \
#         .getOrCreate()

if __name__ == '__main__':
    # csv_list = [fr.find_file(1), fr.find_file(62), fr.find_file(63), fr.find_file(64), fr.find_file(65), fr.find_file(75)]
    # df_list = []
    # for csv in csv_list:
    #     df_list.append(fr.csv_to_spark_dataframe(csv))
    # gsp.RadarChart.generate(df_list)

    hmp_test_csv = fr.find_file(65)
    hmp_test_df, spark_session = fr.csv_to_spark_dataframe(hmp_test_csv)
    gsp.HeatMap.generate(hmp_test_df)


