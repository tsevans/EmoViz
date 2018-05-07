import filereader as fr
import sys
import graph_static_plotly as gsp


def delegate_visualization(viz_type):
    if viz_type == 'RAD':
        pass
    elif viz_type == 'HMP':
        pass
    elif viz_type == 'RIB':
        pass
    elif viz_type == 'LNG':
        pass
    else:
        print('Error: Vizualization type not recognized.')
        sys.exit(2)


def run_job(keys, viz_type):
    dataframes, spark_session = fr.load_dataframes(keys)

    pass


if __name__ == '__main__':
    viz_code = sys.argv[1]
    files = sys.argv[2:]
    wf = open('out.txt', 'wb')
    wf.write('Viz type -> ' + viz_code)
    for f in files:
        wf.write(('File: ' + f))
    wf.close()
    run_job()
    sys.exit(0)
