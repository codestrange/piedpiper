
from os import makedirs
from os.path import exists
from glob import glob
from shutil import rmtree


def mkdir(path):
    try:
        if exists(path):
            rmtree(path)
        if not exists(path):
            makedirs(path)
    except OSError:
        print('Error: Creating directory of data')


def jpgcount(path):
    return len(glob(path + '/*.jpg'))


def prt(path, frame):
    name = path + '/frame' + str(frame) + '.jpg'
    print('Creating... ' + name)
    return name
