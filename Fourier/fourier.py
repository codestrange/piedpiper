import numpy as np
#from PIL import Image
from scipy import fftpack

def get_2D_dct(coefficients):
    """ Get 2D Cosine Transform of Image
    """
    return fftpack.dct(fftpack.dct(coefficients, norm='ortho').T, norm='ortho')

def get_2D_idct(coefficients):
    """ Get 2D Inverse Cosine Transform of Image
    """
    return fftpack.idct(fftpack.idct(coefficients, norm='ortho').T, norm='ortho')

Q = [[16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]]

block_size = len(Q)

def compress_image(image, quantify=False, qratio=4):
    N, M = image.shape

    blocks = []

    for i in range(0, N, block_size):
        rows = image[i:i + block_size]
        if len(rows) < block_size: break
        
        new_blocks = []

        for j in range(0, M, block_size):
            block = [row[j:j + block_size] for row in rows]
            if len(block) < block_size: break

            dct = [[int(c / (qratio * Q[i][j] if quantify else 1)) for j, c in enumerate(row)] for i, row in enumerate(get_2D_dct(block))]

            new_blocks.append(dct)

        blocks.append(new_blocks)

    return blocks


def decompress_image(blocks, quantify=False, qratio=4):
    data = []

    for row in blocks:
        rrow = [[[c * (qratio * Q[i][j] if quantify else 1) for j, c in enumerate(brow)] for i, brow in enumerate(block)] for block in row]
        data.extend([] for _ in range(block_size))

        for block in rrow:
            for i, brow in enumerate(get_2D_idct(block)):
                data[i - block_size].extend(brow)

    return np.matrix(data)

def full_compress(image,qratio=4):
    aux = compress_image(image,True,qratio)
    return decompress_image(aux,True,qratio) 
