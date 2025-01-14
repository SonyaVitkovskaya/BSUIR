"""Лабораторная работа 3
    Вариант 1: Реализовать модель сети Джордана с логарифмической функцией активации – гиперболический арксинус
    гр.121702, Витковская С.И. """

import numpy as np
import math as m
import time

def scale(x):
    i = 0
    while x >= 10:
        x = x/10
        i+=1
    return 10**i

def fibonacci(pair, number):
    result = []
    for _ in range(number):
        result.append(pair[0] + pair[1])
        pair = [pair[1], result[-1:][0]]
    return result

def arithmetic(last, number):
    result = []
    for _ in range(number):
        result.append(last + 2)
        last = result[-1:][0]
    return result

def geometric(last, number):
    result = []
    for _ in range(number):
        result.append(last * 2)
        last = result[-1:][0]
    return result

def power(last, number):
    last = int(m.sqrt(last))
    return [(i+last)**2 for i in range(1, number+1)]

def periodic(last, number):
    result = []
    for _ in range(number):
        if last == 3: result.append(1)
        else: result.append(last + 1)
        last = result[-1:][0]
    return result


def create_matrices(size, seq):
    return [seq[i:i+size[1]] for i in range(size[0])], [seq[i+size[1]:i+size[2]+size[1]] for i in range(size[0])]

def create_weights(rows, columns):
    return np.array([list(np.random.uniform(-1.0, 1.0, size=columns)) for _ in range(rows)])


def activ_func(x):
    return np.arcsinh(x)

def derivative_active_func(x):
    return 1/(np.sqrt(1 + x**2)) # 1/(np.cosh(np.arcsinh(x)))


def correct_weights(W_ih, W_ho, l_rate, diff, state):
    delta_o = diff * derivative_active_func(state[2])
    delta_h = np.dot(delta_o, W_ho.T) * derivative_active_func(state[1])
    grad_h = np.dot(np.atleast_2d(state[0]).T, np.atleast_2d(delta_h)) 
    grad_o = np.dot(np.atleast_2d(state[1]).T, np.atleast_2d(delta_o))
    new_Who = W_ho - (l_rate * grad_o)
    new_Wih = W_ih - (l_rate * grad_h)
    return new_Wih, new_Who

def count_output(state, W_ih, W_ho, input, scale):
    current_input = np.array(input)/scale
    state[0][:len(current_input)], state[0][len(current_input):]  = current_input, state[2]
    state[1] = activ_func(np.dot(state[0], W_ih))
    state[2] = activ_func(np.dot(state[1], W_ho))
    return state


def train(network_state, l_rate, max_error, l_matrix, e_matrix, W_ih, W_ho, scale):
    error = max_error + 1
    iteration = 1

    while error > max_error:
        error = 0
        for row_index in range(len(l_matrix)):
            network_state = count_output(network_state, W_ih, W_ho, l_matrix[row_index], scale)
            current_output = network_state[2]
            current_target = np.array(e_matrix[row_index])/scale
            diff = current_output - current_target
            error += (diff**2).sum()

            W_ih, W_ho = correct_weights(W_ih, W_ho, l_rate, diff, network_state)

        print(f'{iteration}) {error}')
        iteration += 1
    return W_ih, W_ho, network_state




def network(inp, hid, out, error, l_rate, seq):
    s = scale(seq[-1])
    learning_matrix, expected_matrix = create_matrices([hid, inp, out], seq)
    W_ih = create_weights(inp+out,hid)
    W_ho = create_weights(hid,out)
    network_state = [[0 for _ in range(W_ih.shape[0])], [0 for _ in range(hid)], [0 for _ in range(out)]]
    W_ih, W_ho, network_state = train(network_state, l_rate, error, learning_matrix, expected_matrix, W_ih, W_ho, s)
    miss =  0
    for i in range(hid):
        output = count_output(network_state, W_ih, W_ho, learning_matrix[i], s)[2]*s
        print(expected_matrix[i], " -> ", output)
        miss += ((np.abs(expected_matrix[i]-output)/expected_matrix[i]).sum())/out
    print("ошибка", miss/hid)


def main():
    sequences = [["fibonacci",  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]], 
                 ["arithmetic", [0, 1, 3, 5, 7, 9, 11, 13, 15, 17]], 
                 ["geometric", [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]], 
                 ["power", [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]], 
                 ["periodic", [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]]]
    
    for i in range(len(sequences)): print(i+1, sequences[i][0], sequences[i][1])
    choice = 4 #int(input("Выберите последовательность "))
    seq = sequences[choice-1][1]
        
    input_layer = 1
    hidden = 6
    output = 3

    add_seq_len = input_layer + output + hidden - len(seq) - 1
    if add_seq_len > 0:
        if choice == 1: seq += fibonacci(seq[-2:], add_seq_len)
        elif choice == 2:  seq += arithmetic(seq[-1:][0], add_seq_len)
        elif choice == 3:  seq += geometric(seq[-1:][0], add_seq_len)
        elif choice == 4:  seq += power(seq[-1:][0], add_seq_len)
        elif choice == 5:  seq += periodic(seq[-1:][0], add_seq_len)

    error = 0.1
    learning_rate = 0.01
    network(input_layer, hidden, output, error, learning_rate, seq)

for i in range(5):
    main()
    time.sleep(5)