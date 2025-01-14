"""Лабораторная работа 1
    Вариант 1: Реализовать модель линейной рециркуляционной сети с постоянным коэффициентом обучения и ненормированными весовыми коэффициентами 
    гр.121702, Витковская С.И. """

import numpy as np
from PIL import Image

"""
def multiply(A, B):
    if len(A[0]) == len(B): return np.clip([[sum([A[i][k]*B[k][j] for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))], -1e+10, 1e+10)
    print("Ошибка в размерностях")

def transpose(matrix):
    return np.array([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))], dtype = np.float64)

def difference(A, B):
    return np.clip([[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))], -1e+10, 1e+10)
"""

def image_to_matrix(img_file, b_height, b_width):
    with Image.open(img_file) as im:
        array, (width, height) =  np.array(im), im.size

    blocks = []
    for i in range(0, height, b_height): 
        for j in range(0, width, b_width):  
            block = []
            for i_ in range(b_height):
                for j_ in range(b_width):
                    block += list(map(lambda color: (2*color/255) - 1, array[i+i_, j+j_][:3]))
            blocks.append(block)
    return blocks, (width, height)

def matrix_to_image(blocks, img_size, b_height, b_width, output_file= "output3.jpg"):
    width, height = img_size
    array = np.zeros((height, width, 3), dtype=np.uint8) 

    block_index = 0
    for i in range(0, height, b_height):
        for j in range(0, width, b_width): 
            block = blocks[block_index]
            block_index += 1
            pixel_index = 0
            for i_ in range(b_height):
                for j_ in range(b_width):
                    pixel = [np.clip(int(((block[pixel_index + color] + 1) * 255) / 2), 0, 255) for color in range(3)]
                    array[i + i_, j + j_] = pixel
                    pixel_index += 3

    restored_image = Image.fromarray(array)
    restored_image.save(output_file)
    print(f"Изображение сохранено как: {output_file}")

def multiply(A, B):
    if len(A[0]) == len(B): return np.dot(A, B)
    print("Ошибка в размерностях")

def difference(A, B):
    if (A.shape == B.shape): return A - B
    print("Ошибка в размерностях")

def create_weights(rows, columns):
    first = np.array([list(np.random.uniform(-1.0, 1.0, size=columns)) for _ in range(rows)])
    return first, first.T

def correct_weights(X, Y, delta, fl_weights, sl_weights, learn_rate):
    new_fl_weights = difference(fl_weights, learn_rate * np.matmul(np.matmul(X.T, delta), sl_weights.T))
    new_sl_weights = difference(sl_weights, learn_rate * np.matmul(Y.T, delta))
    return new_fl_weights, new_sl_weights

def train(arr, fl_weights, sl_weights, max_error, learning_rate): 
    error = max_error + 1
    iteration = 1
    while error > max_error:
        error = 0
        for block in arr:
            X = np.array([block])
            Y = multiply(X, fl_weights)
            new_X = multiply(Y, sl_weights)
            delta = difference(new_X, X)

            fl_weights, sl_weights = correct_weights(X, Y, delta, fl_weights, sl_weights, learning_rate)

        for block in arr:            
            X = np.array([block])
            Y = multiply(X, fl_weights)
            new_X = multiply(Y, sl_weights)
            delta = difference(new_X, X)

            error += multiply(delta, delta.T)[0][0]

        print(f'{iteration}) {error}')
        iteration += 1

    return fl_weights, sl_weights

def network(img_array, first_layer_size, second_layer_size, error, learning_rate):
    img_array = np.array(img_array)
    first_layer_weights, second_layer_weights = create_weights(first_layer_size, second_layer_size)
    first_layer_weights, second_layer_weights = train(img_array, first_layer_weights, second_layer_weights, error, learning_rate)

    compressed_img = multiply(img_array, first_layer_weights)
    decompressed_img = multiply(compressed_img, second_layer_weights)
    return decompressed_img

def main():
    img = "Lena.jpg"
    error = 3500
    learning_rate = 0.001005
    block_height, block_width = 8, 8
    first_layer_size = block_width * block_height * 3
    second_layer_size = 16

    img_array, img_size = image_to_matrix(img, block_height, block_width)
    print(f"Из изображения {img_size} cформирована матрица ({len(img_array)}, {first_layer_size})")

    q, n, p = img_size[0]*img_size[1]/(block_height*block_width), first_layer_size, second_layer_size
    print(f"Z: {(q * n)/(2 + ((n+q)*p)) }")

    result_array = network(img_array, first_layer_size, second_layer_size, error, learning_rate)
    matrix_to_image(result_array, img_size, block_width, block_height)
    return result_array

main()