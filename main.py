from ImageProcessing import *
from Fourier import *
from Wavelets import *

#modulo principal de la aplicación

#descomentar las secciones a ejecutar (solo ejecutar un bloque a la vez)

def Generate_FFT_Images(qratio):
    images = Get_Numpy_Array(gray_photos)
    
    mkdir(fft_photos_umbral)
    mkdir(fft_photos_quantification)
    
    for i,image in enumerate(images):
        blocks = compress_image(image)
        blocks_quantification2 = [[quntification(block, Q, qratio) for block in row] for row in blocks]
        comp1 = decompress_image(blocks_quantification2)
        std = np.std(image)
        blocks_umbral = [[umbral(block, std) for block in row] for row in blocks]
        comp = decompress_image(blocks_umbral)
        cv2.imwrite(fft_photos_quantification + '/frame' + str(i) + '.jpg', comp1)
        cv2.imwrite(fft_photos_umbral + '/frame' + str(i) + '.jpg', comp)
        prt(fft_photos_quantification,i)
        prt(fft_photos_umbral,i)
    
    print('FFT Done!!')

def Generate_FFT_Unmbral():
    images = Get_Numpy_Array(gray_photos)
    mkdir(fft_photos_umbral)
    blocks = compress_image(image)
    std = np.std(image)
    blocks_umbral = [[umbral(block, std) for block in row] for row in blocks]
    data = decompress_image(blocks_umbral)
    cv2.imwrite(fft_photos_umbral + '/frame' + str(i) + '.jpg', data)
    prt(fft_photos_umbral,i)
    
def Generate_FFT_Qratio(qratio):
    images = Get_Numpy_Array(gray_photos)
    blocks = compress_image(image)
    mkdir(fft_photos_quantification)
    blocks_quantification = [[quntification(block, Q, qratio) for block in row] for row in blocks]
    data = decompress_image(blocks_quantification)
    
    cv2.imwrite(fft_photos_quantification + '/frame' + str(i) + '.jpg', data)
    prt(fft_photos_quantification,i)

def Generate_Wavelet_Images(rows, columns):
    Generate_Wavelet_Temp(rows,columns)
    Generate_Wave_Esp()
    
    print('Wavelets Done!!')
    
def Generate_Wavelet_Temp(rows, columns):
    images = Get_Numpy_Array(gray_photos)
    
    result = []
    
    mkdir(wave_photos_temp)
    
    for j in range(0,rows):
        temp = []
        for i in range(0,columns):
            temp.append(images[j*columns + i])
        reuslt = time_compression(temp,3000000)
        for i in range(0,len(reuslt)):
            result.append(full_compress_wavelets(reuslt[i]))
    
    for i,image in enumerate(result):
        cv2.imwrite(wave_photos_temp + '/frame' + str(i) + '.jpg', image)     
        prt(wave_photos_temp,i)
        
def Generate_Wave_Esp():
    images = Get_Numpy_Array(gray_photos)
    
    mkdir(wave_photos_esp)
    
    for i,image in enumerate(images):
        comp = full_compress_wavelets(image)
        cv2.imwrite(wave_photos_esp + '/frame' + str(i) + '.jpg', comp)
        prt(wave_photos_esp,i)


#****************************************************BLOQUE***********************************************

##----------------------------------------------Preparar Video -----------------------------------
## Esta pare del código solo necesita ser ejecutada una vez por video
#Read_Images(color_photos, video_path)
#Convert_To_Gray(color_photos, gray_photos)
#Make_Video(color_photos, color_video, color_video_name)
#Make_Video(gray_photos, gray_video, gray_video_name)

##----------------------------------------------Ejecutar FFT -------------------------------------
## El valor proporcionado al método es un coeficiente de la matriz que sirve de filtro
#Generate_FFT_Images(4)
#Make_Video(fft_photos_quantification, fft_video_quantification, fft_video_name)
#Make_Video(fft_photos_umbral, fft_video_umbral, fft_video_name) 
 

##-----------------------------------------------Ejecutar Wavelet --------------------------------
## Para ejecutar este pedazo de código se debe tener en cuenta que de la forma que diseñamos una de las
## compresiones de wavelet es necesario suministrarle la cantidad de filas y columnas. Esta parte del
## algoritmo toma las n filas y las convierte en filas de m elementos que son procesados juntos
## y luego devueltos en la misma forma. Dado que el numero de frames de un video es desconocido
## se hace necesari suministrar estos datos a mano, para saber la cantidad de frames (fotos) presentes
## se puede descomentar la primera parte del código y revisar cualquiera de sus carpetas generadas

#Generate_Wavelet_Images(x,x)
#Make_Video(wave_photos_temp, wave_video_temp, wave_video_name)
#Make_Video(wave_photos_esp, wave_video_esp, wave_video_name)

#**********************************************************************************************************


#**************************************************BLOQUE****************************************************

#------------------------------------------------Ejemplo1------------------------------------------------
#Read_Images(color_photos, video_path)
#Convert_To_Gray(color_photos, gray_photos)
Generate_FFT_Images(4)
Generate_Wavelet_Images(4,20)
#Make_Video(color_photos, color_video, color_video_name)
#Make_Video(gray_photos, gray_video, gray_video_name)
Make_Video(fft_photos_quantification, fft_video_quantification, fft_video_name)
Make_Video(fft_photos_umbral, fft_video_umbral, fft_video_name)
Make_Video(wave_photos_temp, wave_video_temp, wave_video_name)
Make_Video(wave_photos_esp, wave_video_esp, wave_video_name)
#print('Ejemplo1 Done !!')

#***************************************************************************************************************

#****************************************************BLOQUE****************************************************

##------------------------------------------------Ejemplo2------------------------------------------------
#Read_Images(color_photos, video_path)
#Convert_To_Gray(color_photos, gray_photos)
#Generate_FFT_Images(4)
#Generate_Wavelet_Images(16,73)
#Make_Video(color_photos, color_video, color_video_name)
#Make_Video(gray_photos, gray_video, gray_video_name)
#Make_Video(fft_photos_quantification, fft_video_quantification, fft_video_name)
#Make_Video(fft_photos_umbral, fft_video_umbral, fft_video_name)
#Make_Video(wave_photos_temp, wave_video_temp, wave_video_name)
#Make_Video(wave_photos_esp, wave_video_esp, wave_video_name)
#print('Ejemplo2 Done !!')

#*****************************************************************************************************************
