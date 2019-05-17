import cv2
import numpy as np
from .utils import mkdir,jpgcount

fps = 30

def Read_Images(photos_path, video_path):
    global fps
    
    #Reproducir video para realizar la captura por frames
    cap = cv2.VideoCapture(video_path)
    #optener los fps del video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f'fps: {fps}')
    
    mkdir(photos_path)
    
    currentFrame = 0
    while(True):
        # Obtener 1 frame
        ret, frame = cap.read()
        
        try:
            len(frame)
        except:
            break

        # Salvar la catura
        name =  photos_path + '/frame' + str(currentFrame) + '.jpg'
        print ('Creating... ' + name)
        cv2.imwrite(name, frame)

        # Indice de la imagen
        currentFrame += 1

    # Cerrar el video
    cap.release()
    cv2.destroyAllWindows() 
    
def Make_Video(photos_path, video_path, video_name):
    global fps
    
    mkdir(video_path)
    
    images_cnt = jpgcount(photos_path)
    
    print(f'{images_cnt} imagenes')
    
    img=[]
    #Cargar las imágenes
    for i in range(0,images_cnt):
        img.append(cv2.imread(photos_path + '/frame' + str(i) + '.jpg'))

    height,width,layers=img[1].shape
    #Inicializar el video
    video=cv2.VideoWriter(video_path + '/' + video_name + '.mp4',cv2.VideoWriter_fourcc(*'MP4V'), fps, (width,height))

    print('Codificando video')
    #Insertar cada imagen
    for j in range(0,images_cnt):
        video.write(img[j])
    
    #Cerrar proceso
    cv2.destroyAllWindows()
    video.release() 
    
    print('Video Codificado')
    
def Get_Numpy_Array(photos_path):
    result = []
    
    images_cnt = jpgcount(photos_path)
    
    for i in range(0,images_cnt):
        img = cv2.imread(photos_path + '/frame' + str(i) + '.jpg', 0)
        result.append(img)
    print(result[-1])    
    return result

def Convert_To_Gray(photos_path, output_path):
    mkdir(output_path)
    
    cant = jpgcount(photos_path)
    
    for i in range(0,cant):
        image = cv2.imread(photos_path + '/frame' + str(i) + '.jpg')
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray_image,(1024,512))
        cv2.imwrite(output_path + '/frame' + str(i) + '.jpg', resized)
    
