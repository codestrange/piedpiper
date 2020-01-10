from numpy import std
from cv2 import imwrite
from fourier import compress_image, decompress_image, quntification, Q, umbral
from imageprocessing import convert_to_gray, get_numpy_array, read_images, make_video
from imageprocessing.config import color_photos, color_video, color_video_name, \
    fft_photos_quantification, fft_photos_umbral, fft_video_name, fft_video_quantification, \
    fft_video_umbral, gray_photos, gray_video, gray_video_name, video_path, wave_photos_esp, \
    wave_photos_temp, wave_video_esp, wave_video_name, wave_video_temp
from imageprocessing.utils import mkdir, prt
from wavelets import full_compress_wavelets, time_compression


# Modulo principal de la Aplicación
# Descomentar las secciones a ejecutar (solo ejecutar un bloque a la vez)


def generate_fft_images(qratio):
    images = get_numpy_array(gray_photos)

    mkdir(fft_photos_umbral)
    mkdir(fft_photos_quantification)

    for i, image in enumerate(images):
        blocks = compress_image(image)
        blocks_quantification2 = [
            [quntification(block, Q, qratio) for block in row]
            for row in blocks
        ]
        comp1 = decompress_image(blocks_quantification2)
        _std = std(image)
        blocks_umbral = [[umbral(block, _std) for block in row] for row in blocks]
        comp = decompress_image(blocks_umbral)
        imwrite(fft_photos_quantification + '/frame' + str(i) + '.jpg', comp1)
        imwrite(fft_photos_umbral + '/frame' + str(i) + '.jpg', comp)
        prt(fft_photos_quantification, i)
        prt(fft_photos_umbral, i)

    print('FFT Done!!')


def generate_fft_unmbral():
    images = get_numpy_array(gray_photos)
    mkdir(fft_photos_umbral)
    blocks = compress_image(image)
    _std = std(image)
    blocks_umbral = [[umbral(block, _std) for block in row] for row in blocks]
    data = decompress_image(blocks_umbral)
    imwrite(fft_photos_umbral + '/frame' + str(i) + '.jpg', data)
    prt(fft_photos_umbral, i)


def generate_fft_qratio(qratio):
    images = get_numpy_array(gray_photos)
    blocks = compress_image(image)
    mkdir(fft_photos_quantification)
    blocks_quantification = [[quntification(block, Q, qratio) for block in row] for row in blocks]
    data = decompress_image(blocks_quantification)

    imwrite(fft_photos_quantification + '/frame' + str(i) + '.jpg', data)
    prt(fft_photos_quantification, i)


def generate_wavelet_images(rows, columns):
    generate_wavelet_temp(rows, columns)
    generate_wavelet_esp()

    print('Wavelets Done!!')


def generate_wavelet_temp(rows, columns):
    images = get_numpy_array(gray_photos)

    result = []

    mkdir(wave_photos_temp)

    for j in range(0, rows):
        temp = []
        for i in range(0, columns):
            temp.append(images[j * columns + i])
        temp_result = time_compression(temp, 3000000)
        for item in temp_result:
            result.append(full_compress_wavelets(item))

    for i, image in enumerate(result):
        imwrite(wave_photos_temp + '/frame' + str(i) + '.jpg', image)
        prt(wave_photos_temp, i)


def generate_wavelet_esp():
    images = get_numpy_array(gray_photos)

    mkdir(wave_photos_esp)

    for i, image in enumerate(images):
        comp = full_compress_wavelets(image)
        imwrite(wave_photos_esp + '/frame' + str(i) + '.jpg', comp)
        prt(wave_photos_esp, i)


# ***** BLOQUE ************************************************************************************

# ----- Preparar Video --------------------------------------------------------------------------

# Esta pare del código solo necesita ser ejecutada una vez por video.

read_images(color_photos, video_path)
convert_to_gray(color_photos, gray_photos)
make_video(color_photos, color_video, color_video_name)
make_video(gray_photos, gray_video, gray_video_name)

# ----- Ejecutar FFT ----------------------------------------------------------------------------

# El valor proporcionado al método es un coeficiente de la matriz que sirve de filtro.

generate_fft_images(4)
make_video(fft_photos_quantification, fft_video_quantification, fft_video_name)
make_video(fft_photos_umbral, fft_video_umbral, fft_video_name)


# ----- Ejecutar Wavelet ------------------------------------------------------------------------

# Para ejecutar este pedazo de código se debe tener en cuenta que de la forma que diseñamos una
# de las compresiones de wavelet es necesario suministrarle la cantidad de filas y columnas. Esta
# parte del algoritmo toma las n filas y las convierte en filas de m elementos que son procesados
# juntos y luego devueltos en la misma forma. Dado que el numero de frames de un video es
# desconocido se hace necesario suministrar estos datos a mano, para saber la cantidad de frames
# (fotos) presentes se puede descomentar la primera parte del código y revisar cualquiera de sus
# carpetas generadas.

generate_wavelet_images(x, x)
make_video(wave_photos_temp, wave_video_temp, wave_video_name)
make_video(wave_photos_esp, wave_video_esp, wave_video_name)

# *************************************************************************************************

# ***** BLOQUE ************************************************************************************

# ----- Ejemplo 1 -------------------------------------------------------------------------------

read_images(color_photos, video_path)
convert_to_gray(color_photos, gray_photos)
generate_fft_images(4)
generate_wavelet_images(4, 20)
make_video(color_photos, color_video, color_video_name)
make_video(gray_photos, gray_video, gray_video_name)
make_video(fft_photos_quantification, fft_video_quantification, fft_video_name)
make_video(fft_photos_umbral, fft_video_umbral, fft_video_name)
make_video(wave_photos_temp, wave_video_temp, wave_video_name)
make_video(wave_photos_esp, wave_video_esp, wave_video_name)
print('Ejemplo 1 Done !!')

# *************************************************************************************************

# ***** BLOQUE ************************************************************************************

# ----- Ejemplo 2 -------------------------------------------------------------------------------

read_images(color_photos, video_path)
convert_to_gray(color_photos, gray_photos)
generate_fft_images(4)
generate_wavelet_images(16, 73)
make_video(color_photos, color_video, color_video_name)
make_video(gray_photos, gray_video, gray_video_name)
make_video(fft_photos_quantification, fft_video_quantification, fft_video_name)
make_video(fft_photos_umbral, fft_video_umbral, fft_video_name)
make_video(wave_photos_temp, wave_video_temp, wave_video_name)
make_video(wave_photos_esp, wave_video_esp, wave_video_name)
print('Ejemplo 2 Done !!')

# *************************************************************************************************
