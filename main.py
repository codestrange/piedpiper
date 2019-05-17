from ImageProcessing import *
from Fourier import *
from Wavelets import *

#modulo principal de la aplicación

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
    
    print('FFT Done!!')

def Generate_FFT_Unmbral():
    images = Get_Numpy_Array(gray_photos)
    mkdir(fft_photos_umbral)
    blocks = compress_image(image)
    std = np.std(image)
    blocks_umbral = [[umbral(block, std) for block in row] for row in blocks]
    data = decompress_image(blocks_umbral)
    cv2.imwrite(fft_photos_umbral + '/frame' + str(i) + '.jpg', data)
    
def Generate_FFT_Qratio(qratio):
    images = Get_Numpy_Array(gray_photos)
    blocks = compress_image(image)
    mkdir(fft_photos_quantification)
    blocks_quantification = [[quntification(block, Q, qratio) for block in row] for row in blocks]
    data = decompress_image(blocks_quantification)
    
    cv2.imwrite(fft_photos_quantification + '/frame' + str(i) + '.jpg', data)

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
        reuslt = time_compression(temp,2000000)
        for i in range(0,len(reuslt)):
            result.append(full_compress_wavelets(reuslt[i]))
    
    for i,image in enumerate(result):
        cv2.imwrite(wave_photos_temp + '/frame' + str(i) + '.jpg', image)        
        
def Generate_Wave_Esp():
    images = Get_Numpy_Array(gray_photos)
    
    mkdir(wave_photos_esp)
    
    for i,image in enumerate(images):
        comp = full_compress_wavelets(image)
        cv2.imwrite(wave_photos_esp + '/frame' + str(i) + '.jpg', comp)
    
    print('Wavelets Done!!')

Read_Images(color_photos, video_path)

Convert_To_Gray(color_photos, gray_photos)

Generate_FFT_Images(qratio)
    
Generate_Wavelet_Images(4,20)


Make_Video(color_photos, color_video, color_video_name)
Make_Video(gray_photos, gray_video, gray_video_name)
Make_Video(fft_photos_quantification, fft_video_quantification, fft_video_name)
Make_Video(fft_photos_umbral, fft_video_umbral, fft_video_name)
Make_Video(wave_photos_temp, wave_video_temp, wave_video_name)
Make_Video(wave_photos_esp, wave_video_esp, wave_video_name)
