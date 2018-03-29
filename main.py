import filereader as fr
import graph_static_plotly as gsp
import color_utils as cu


if __name__ == '__main__':
# Tests for radarcharts
    # csv_list = [fr.find_file(1), fr.find_file(62), fr.find_file(63), fr.find_file(64), fr.find_file(65), fr.find_file(75)]
    # csv_list = [fr.find_file(1), fr.find_file(64), fr.find_file(65)]
    # df_list = []
    # for csv in csv_list:
    #     df_list.append(fr.csv_to_spark_dataframe(csv)[0])
    # gsp.RadarChart.generate(df_list)

# Tests for heatmaps
    # id = 1
    # hmp_test_csv = fr.find_file(id)
    # hmp_test_df, spark_session = fr.csv_to_spark_dataframe(hmp_test_csv)
    # gsp.HeatMap.generate(hmp_test_df, str(id))
    # spark_session.get_active_session().stop()

# Tests for ribbon plots
    id = 65
    rib_test_csv = fr.find_file(id)
    rib_test_df, spark_session = fr.csv_to_spark_dataframe(rib_test_csv)
    gsp.RibbonPlot.generate(rib_test_df, str(id))
    spark_session.get_active_session().stop()
