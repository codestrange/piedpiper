import cv2
import numpy as np
import os
import glob

fps = 30

def Read_Images(photos_path = './muestras',video_path='./example.mp4'):
    global fps
    # Playing video from file:
    cap = cv2.VideoCapture(video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f'fps: {fps}')

    try:
        if not os.path.exists(photos_path):
            os.makedirs(photos_path)
    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        try:
            len(frame)
        except:
            break

        # Saves image of the current frame in jpg file
        name =  photos_path + '/frame' + str(currentFrame) + '.jpg'
        print ('Creating... ' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows() 

def Make_Video(photos_path = './muestras', video_path = './video/video.avi'):
    try:
        if not os.path.exists('./video'):
            os.makedirs('./video')
    except OSError:
        print ('Error: Creating directory of data')
    
    images_cnt = len(glob.glob(photos_path + '/*.jpg'))
    print(f'{images_cnt} imagenes')
    
    img=[]
    for i in range(0,images_cnt):
        img.append(cv2.imread(photos_path + '/frame' + str(i) + '.jpg'))

    height,width,layers=img[1].shape

    #cv2.VideoWriter_fourcc('M','J','P','G')
    #video=cv2.VideoWriter('./video.avi',-1,1,(width,height))
    video=cv2.VideoWriter(video_path,cv2.VideoWriter_fourcc(*'DIVX'), fps, (width,height))

    print('Enzamblando video')
    
    for j in range(0,images_cnt):
        video.write(img[j])

    cv2.destroyAllWindows()
    video.release() 
