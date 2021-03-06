import os
import shelve
import csv_processor as cp


def read(key):
    """
    Retrieve record from database corresponding to key.
    CsvRecord should already be checked using contains method.
    :param key: Record key for database, should be name of file.
    :return: Copy of CsvRecord object stored at key.
    """
    db = shelve.open('csv_index.dat')
    record = db[str(key)]
    db.close()
    print('Record '+str(key)+' was read from database.')
    return record


def contains(key):
    """
    Check if a record is in the database.
    :param key: Key for the record to check.
    :return: True if record is in database, False if not in database.
    """
    db = shelve.open('csv_index.dat')
    contains = str(key) in db
    db.close()
    return contains


def write(csv_rec):
    """
    Write CsvRecord to database, using its name as the key.
    :param csv_rec: CsvRecord object to write to database.
    """
    csv_rec.rename()

    # Save file to data_proc/ directory
    with open(csv_rec.path_unprocessed) as f:
        lines = f.readlines()
        lines = [l for l in lines]
        with open(csv_rec.path_processed, "w") as f1:
            f1.writelines(lines)
    # temp_file = open(csv_rec.name, 'w+')
    # temp_file.close()

    db = shelve.open('csv_index.dat')
    key = str(csv_rec.id_number)
    db[key] = csv_rec
    db.close()
    print('Record '+key+' was written to database.')


def wipe():
    """
    Delete all records in the database and delete file on disk.
    Mainly used for benchmarking differences in execution time when record
    has already been processed vs when it must be processed and written beforehand.
    """
    db = shelve.open('csv_index.dat')
    db.clear()
    db.close()
    os.remove('csv_index.dat')
    print('Wiped all records from csv_index.dat')


def fill():
    """
    Process all records from data_raw/ directory and write them to data_proc/ directory.
    """
    # Wipe database before refilling it in order to avoid collisions.
    wipe()
    for filename in os.listdir('data_raw/'):
        if 'Adjusted' in filename:
            processed = cp.CsvRecord(filename)
            processed.fix_adjustments()
            # TODO: Need to actually process file with adjustments, this also means writing it to data_proc/
        else:
            processed = cp.CsvRecord(filename, True)
        write(processed)


if __name__ == '__main__':
    wipe()
    rec = cp.CsvRecord("P01_Emotion.csv", True)
    write(rec)
    copy = read(1)
    print(copy.name)
    print(copy.id_number)
    print(copy.is_processed)