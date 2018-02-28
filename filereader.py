import os

def getFile( filename ):
    script_dir = os.path.dirname(__file__)
    relative_path = 'data/' + filename
    absolute_path = os.path.join(script_dir, relative_path)

    filehandle = open(absolute_path)
    print(filehandle.read())
    filehandle.close()

if __name__ == '__main__':
    getFile('P01_Emotion.csv')
