from cv2 import CAP_PROP_FPS, COLOR_BGR2GRAY, cvtColor, destroyAllWindows, imread, imwrite, \
    resize, VideoCapture, VideoWriter, VideoWriter_fourcc
from .config import video_path as v_path
from .utils import mkdir, jpgcount, prt


def read_images(photos_path, video_path):
    cap = VideoCapture(video_path) # Reproducir video para realizar la captura por frames

    fps = cap.get(CAP_PROP_FPS) # Optener los fps del video

    print(f'fps: {fps}')

    mkdir(photos_path)

    currentFrame = 0

    while True:
        _, frame = cap.read() # Obtener 1 frame
        try:
            len(frame)
        except:
            break
        # Salvar la catura
        name = prt(photos_path, currentFrame)
        imwrite(name, frame)

        currentFrame += 1 # Indice de la imagen

    # Cerrar el video
    cap.release()
    destroyAllWindows()


def make_video(photos_path, video_path, video_name):
    cap = VideoCapture(v_path)
    fps = cap.get(CAP_PROP_FPS)
    cap.release()

    mkdir(video_path)

    images_cnt = jpgcount(photos_path)

    print(f'{images_cnt} imagenes')

    img = []

    # Cargar las imágenes
    for i in range(images_cnt):
        img.append(imread(photos_path + '/frame' + str(i) + '.jpg'))

    height, width, _ = img[1].shape

    # Inicializar el video
    video = VideoWriter(video_path + '/' + video_name + '.mp4', VideoWriter_fourcc(*'MP4V'), fps,
                        (width, height))

    print('Codificando video')

    # Insertar cada imagen
    for j in range(images_cnt):
        video.write(img[j])

    # Cerrar proceso
    destroyAllWindows()
    video.release()

    print('Video Codificado')


def get_numpy_array(photos_path):
    result = []

    images_cnt = jpgcount(photos_path)

    for i in range(images_cnt):
        img = imread(photos_path + '/frame' + str(i) + '.jpg', 0)
        result.append(img)

    return result


def convert_to_gray(photos_path, output_path):
    mkdir(output_path)

    cant = jpgcount(photos_path)

    for i in range(cant):
        image = imread(photos_path + '/frame' + str(i) + '.jpg')
        gray_image = cvtColor(image, COLOR_BGR2GRAY)
        resized = resize(gray_image, (1024, 512))
        imwrite(output_path + '/frame' + str(i) + '.jpg', resized)
