import os
import shutil
from glob import glob

def mkdir(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)
        
    except OSError:
        print ('Error: Creating directory of data')
        
def jpgcount(path):
    return len(glob(path + '/*.jpg'))

def prt(path,frame):
    name =  path + '/frame' + str(frame) + '.jpg'
    print ('Creating... ' + name)
    return name
