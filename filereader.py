import os
from pyspark import SparkContext
import fnmatch as fn

# Get the file path for a csv using the ID number of the student
def getPathFromID(studentID):
    fileID = 'P'
    if studentID < 10:
        fileID += '0'
    fileID = fileID + str(studentID) + '_Emotion'
    path = None
    for file in os.listdir('data/'):
        if fn.fnmatch(file, fileID+'*.csv'):
            path = 'data/'+file
            break
    return path

if __name__ == '__main__':
    print(getPathFromID(1))
    print(getPathFromID(22))
    print(getPathFromID(99))
