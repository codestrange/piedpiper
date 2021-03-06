from numpy import asarray, std
from scipy import fftpack


def get_2d_dct(coefficients):
    """ Get 2D Cosine Transform of Image
    """
    return fftpack.dct(fftpack.dct(coefficients, norm='ortho').T, norm='ortho')


def get_2d_idct(coefficients):
    """ Get 2D Inverse Cosine Transform of Image
    """
    return fftpack.idct(fftpack.idct(coefficients, norm='ortho').T, norm='ortho')


def umbral(matrix, value):
    return [[int(0 if abs(elem) < value else elem) for elem in row] for row in matrix]


Q = [[16, 11, 10, 16, 24, 40, 51, 61],
     [12, 12, 14, 19, 26, 58, 60, 55],
     [14, 13, 16, 24, 40, 57, 69, 56],
     [14, 17, 22, 29, 51, 87, 80, 62],
     [18, 22, 37, 56, 68, 109, 103, 77],
     [24, 35, 55, 64, 81, 104, 113, 92],
     [49, 64, 78, 87, 103, 121, 120, 101],
     [72, 92, 95, 98, 112, 100, 103, 99]]


def quntification(matrix, Q, qratio=4):
    return [
        [int(elem / qelem / qratio) * qelem * qratio for elem, qelem in zip(row, qrow)]
        for row, qrow in zip(matrix, Q)
    ]


block_size = 8


def compress_image(image):
    N, M = image.shape

    blocks = []

    for i in range(0, N, block_size):
        rows = image[i:i + block_size]
        if len(rows) < block_size:
            break

        new_blocks = []

        for j in range(0, M, block_size):
            block = [row[j:j + block_size] for row in rows]
            if len(block) < block_size:
                break

            dct = get_2d_dct(block)

            new_blocks.append(dct)

        blocks.append(new_blocks)

    return blocks


def decompress_image(blocks):
    data = []

    for row in blocks:
        data.extend([] for _ in range(block_size))

        for block in row:
            for i, brow in enumerate(get_2d_idct(block)):
                data[i - block_size].extend(brow)

    return asarray(data)


def umb(data, blocks=None):
    if blocks is None:
        blocks = compress_image(data)
    _std = std(data)
    blocks_umbral = [[umbral(block, _std) for block in row] for row in blocks]
    result = decompress_image(blocks_umbral)
    return result


def quant(number, blocks=None, data=None):
    if blocks is None:
        if data is None:
            return 0
        blocks = compress_image(data)
    blocks_quantification2 = [[quntification(block, Q, number) for block in row] for row in blocks]
    result = decompress_image(blocks_quantification2)
    return result


def umbral_compress(image):
    aux = compress_image(image)
    return umb(image, blocks=aux)


def qratio_compress(image, qratio):
    aux = compress_image(image)
    return quant(qratio, blocks=aux, data=image)
