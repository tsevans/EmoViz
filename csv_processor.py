import csv
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
        csv_file = fr.get_path_from_filename(self.name)

        # TODO: actually do the adjustements of the file (need to read and write lines, and use time utils)

        self.is_processed = True
