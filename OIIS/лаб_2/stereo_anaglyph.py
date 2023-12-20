from PIL import Image, ImageDraw
import numpy as np

COLOR_ANAGLYPH_MATRIX = [np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]], float),
                         np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]], float)]

HALF_COLOR_ANAGLYPH_MATRIX = [np.array([[0.229, 0.587, 0.114], [0, 0, 0], [0, 0, 0]], float),
                              np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]], float)]

OPTIMIZED_ANAGLYPH_MATRIX = [np.array([[0, 0.45, 1.05], [0, 0, 0], [0, 0, 0]], float),
                             np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]], float)]


def make_anaglyph(left_image, right_image, anaglyph_type='color'):
    anaglyph_img = Image.new("RGB", left_image.size)
    if anaglyph_type == 'color':
        coef_matrix = COLOR_ANAGLYPH_MATRIX
    elif anaglyph_type == 'half color':
        coef_matrix = HALF_COLOR_ANAGLYPH_MATRIX
    elif anaglyph_type == 'optimized':
        coef_matrix = OPTIMIZED_ANAGLYPH_MATRIX
    else:
        raise Exception("Unknown anaglyph type")
    draw = ImageDraw.Draw(anaglyph_img)
    left_pix = left_image.load()
    right_pix = right_image.load()
    for i in range(left_image.size[0]):
        for j in range(left_image.size[1]):
            left_pix_rgb = np.array([left_pix[i, j][0],
                                     left_pix[i, j][1],
                                     left_pix[i, j][2]],
                                    float)
            right_pix_rgb = np.array([right_pix[i, j][0],
                                      right_pix[i, j][1],
                                      right_pix[i, j][2]],
                                     float)
            new_rgb = np.dot(
                coef_matrix[0], left_pix_rgb) + np.dot(coef_matrix[1], right_pix_rgb)
            draw.point((i, j), (int(round(new_rgb[0])), int(
                round(new_rgb[1])), int(round(new_rgb[2]))))
    return anaglyph_img


if __name__ == "__main__":
    left_img = Image.open("./images/4/stereopair_left.jpg")
    right_img = Image.open("./images/4/stereopair_right.jpg")

    make_anaglyph(left_img, right_img, 'color').save(
        "color_anaglyph.jpg", "JPEG")
    
    make_anaglyph(left_img, right_img, 'half color').save(
        "half_color_anaglyph.jpg", "JPEG")

    make_anaglyph(left_img, right_img, 'optimized').save(
        "optimized_anaglyph.jpg", "JPEG")
