import filereader as fr
import graph_static_plotly as gsp
import platform


if __name__ == '__main__':
# Tests for radarcharts
#     csv_list = [fr.find_file(1), fr.find_file(64), fr.find_file(65)]
#     df_list = []
#     for csv in csv_list:
#         df_list.append(fr.csv_to_spark_dataframe(csv)[0])
#     gsp.RadarChart.generate(df_list)

# Tests for heatmaps
    id = 1
    hmp_test_csv = fr.find_file(id)
    hmp_test_df, spark_session = fr.csv_to_spark_dataframe(hmp_test_csv)
    gsp.HeatMap.generate(hmp_test_df, str(id))
    spark_session.get_active_session().stop()

# # Tests for ribbon plots
#     id = 65
#     rib_test_csv = fr.find_file(id)
#     rib_test_df, spark_session = fr.csv_to_spark_dataframe(rib_test_csv)
#     gsp.RibbonPlot.generate(rib_test_df, str(id))
#     spark_session.get_active_session().stop()


def run_job(keys, viz_type):
    """
    Run an emoviz job, main execution point of script.
    :param keys: Single file or list of file keys to
    :param viz_type:
    :return:
    """
    plat = platform.system()
    if plat is 'Linux':
        # Run linux methods
        pass
    elif plat is 'Windows':
        # Run windows methods
        pass
    else:
        print('Error, operating system not recognized')


def acquire_files_linux(keys):
    dataframes = fr.load_dataframes(keys)