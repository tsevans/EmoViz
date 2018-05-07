import filereader as fr
import sys
import graph_static_plotly as gsp
import re


def run_job(keys, viz_type):
    dataframes, spark_session = fr.load_dataframes(keys)

    nums = []
    for k in keys:
        nums.append(re.findall(r'\d+', k))

    if viz_type == 'RAD':
        gsp.RadarChart.generate(dataframes, nums)
    elif viz_type == 'HMP':
        pass
    elif viz_type == 'RIB':
        pass
    elif viz_type == 'LNG':
        pass
    else:
        print('Error: Vizualization type not recognized.')
        sys.exit(2)


if __name__ == '__main__':
    viz_code = sys.argv[1]
    files = sys.argv[2:]
    run_job(files, viz_code)
    sys.exit(0)
