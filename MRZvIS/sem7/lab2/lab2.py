"""Лабораторная работа 2
    Вариант 1: Реализовать модель двунаправленной ассоциативной памяти
    Функция активации – модифицированная функция знака
    гр.121702, Витковская С.И. """

import json
import numpy as np
import math as m
import time

def download_file(filename):
    with open(filename)as f:
        return json.load(f)
    
def print_images(data, size):
    for image in data:
        for string in range(size[0]):
            print("".join(["%" if image[char] == 1 else " " for char in range(string * size[1], string*size[1] + size[1])]))
        print("")

def create_weights(x, y):
    w1 = sum([np.dot(np.array([x[i]]).T, np.array([y[i]])) for i in range(len(x))])
    return w1, w1.T

def activ_func(vec, weight):
    mult = np.dot(vec, weight)
    for i in range(len(mult)):
        for j in range(len(mult[i])):
            #mult[i][j] = round(m.tanh(mult[i][j]))
            if mult[i][j] ==  0: mult[i][j] == vec[j]
            else: mult[i][j] = 1 if mult[i][j] > 0 else -1
    return mult

def detect(w1, w2, inp):
    a = activ_func(activ_func(inp, w1), w2)
    
    for _ in range(200):
        print("Итерация", _ + 1)
        new_a = activ_func(activ_func(a, w1), w2)
        if np.array_equal(new_a, a): break
        else: a = new_a
    
    return new_a

def to_bipolar(vec):
    return [1 if val == 1 else -1 for val in vec]

def main():
    x_size = (5, 3)
    y_size = 5
    data = download_file("input2.json")
    X = np.array([data[image]["x"] for image in data][:5])
    Y = np.array([data[image]["y"] for image in data][:5])
    broken_X = np.array([to_bipolar(data[image]["broken x"]) for image in data])

    print("Вводные изображения")
    print_images(X, x_size)

    W1, W2 = create_weights(X, Y)
    print(W1)
        
    while(True): 
        choice = int(input("1-Распознать зашумленный образ \n2-Найти X через Y"))
        if choice == 2:
            index = format(int(input("Введите число")), "b")
            Y = [-1 for i in range(y_size - len(index))] + to_bipolar([int(x) for x in index])
            print_images(activ_func([Y], W2), x_size)
            continue
            
        index = int(input("Выберите тест ")) - 1
        input_arr = broken_X[index]
        error = 0
        for i in range(input_arr.size):
            if X[index][i] != input_arr[i]: error +=1 
        #print("Доля ошибочных символов", error/(x_size[0] * x_size[1])*100, "%")
        print_images([input_arr], x_size)
        print_images(detect(W1, W2, np.array([input_arr])), x_size)
        time.sleep(1)

main()