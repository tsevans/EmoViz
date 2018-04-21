import filereader as fr
import graph_static_plotly as gsp
import platform


if __name__ == '__main__':
    pass
    # run_job()


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