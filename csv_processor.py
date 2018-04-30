import pandas as pd
import time_utils as tm
import filereader as fr


class CsvRecord(object):
    """Class to represent a CSV record in the user's filesystem"""

    def __init__(self, name, is_processed=False):
        self.id_number = int(filter(str.isdigit, name))
        self.name = name
        self.path_unprocessed = 'data_raw/' + name
        self.path_processed = None
        self.is_processed = is_processed

    def rename(self):
        self.name = 'Student_' + str(self.id_number) + '.csv'
        prefix = 'data_proc/' if self.is_processed else ''
        self.path_processed = prefix + self.name

    def get_path(self):
        if self.is_processed:
            return self.path_processed
        else:
            return self.path_unprocessed

    def fix_adjustments(self):
        """
        Fix adjusted file such that timestamps start at 0 time.
        """
        def make_timestamps():
            """
            Build a list of new timestamps to based on adjusted columns.
            :return: List of normalized timestamps.
            """
            f = open(self.path_unprocessed, 'r')
            header = False
            stamps = []
            for ln in f.readlines():
                if not header:
                    header = True
                    continue
                row_vals = ln.split(',')
                stamps.append(tm.compose_timestamp(row_vals[13], row_vals[14], row_vals[15]))
            f.close()
            return stamps

        if self.is_processed:
            return

        stamps = make_timestamps()
        f = pd.read_csv(self.get_path())
        # TODO: actually do the adjustements of the file (need to read and write lines, and use time utils)

        self.is_processed = True


if __name__ == '__main__':
    pass