from ImageProcessing import *
from Fourier import *
import os
import pygame

#modulo principal de la aplicación

#lee el video y lo separa en frames, por defecto asume que el video esta en la misma carpeta que este py y tiene nombre example.py
#los frames se locaclizan en la carpeta /muestras
#Read_Images()


#toma las imagenes de la carpeta muestra y las comprime
#Make_Video()

def Generate_FFT_Images(photos_path = './muestras', output_path = './procesadas'):
    
    images = Get_Numpy_Array(photos_path)
    
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    except OSError:
        print ('Error: Creating directory of data')
    
    for i,image in enumerate(images):
        comp = full_compress(image,qratio=5)
        cv2.imwrite(output_path + '/frame' + str(i) + '.jpg', comp)
    
    print('Done!!')
    
#Generate_FFT_Images(photos_path = './gray')


#Convert_To_Gray()
    
Make_Video(photos_path = './gray', video_path = './video/video3.avi')

#Read_Images(photos_path = './procesadas',video_path='./example.mp4')


file1 = 'alarma.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file1)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
