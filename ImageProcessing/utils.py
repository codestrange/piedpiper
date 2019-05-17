import os
import pygame
from glob import glob

def mkdir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print ('Error: Creating directory of data')
        
def jpgcount(path):
    return len(glob(path + '/*.jpg'))

def play_music(path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    #while pygame.mixer.music.get_busy(): 
        #pygame.time.Clock().tick(10)
