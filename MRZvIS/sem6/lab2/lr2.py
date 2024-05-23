"""Лабораторная работа 2 по дисциплине 'Модели решения задач в интеллектуальных системах'
Реализация модели решения задач в интеллектуальных системах
Выполнили: студентки гр.121702  Витковская С.И., Мойсевич А.В.
Вариант 9"""

import random
import math
ALFABET = [str(i) for i in range(10)]
A, B, E, G, C = [], [], [], [], []
Tn = 0
p, q, m = 0, 0, 0
sum_call, mult_call, diff_call, compare_call = 0,0,0,0
t_sum, t_mult, t_diff, t_comparison, n, r = 1, 1, 1, 1, 1, 1
Lavg, Tavg = 0, 0

def sum(a, b):
    global sum_call
    sum_call += 1
    return a + b

def mult(a, b):
    global mult_call
    mult_call += 1
    return a * b

def diff(a, b):
    global diff_call
    diff_call += 1
    return a - b

def compare(a, b, max_or_min):
    global compare_call
    compare_call += 1
    if (max_or_min): return max(a, b)
    return min(a, b)

def check_input(str):
    for i in str:
        if i not in ALFABET:
            return 1
    return 0

def print_matrix(matr, name = ''):
    print(name)
    for row in matr:
        string = ""
        for col in row:
            string += str(col) + "  "
        print(string)

def fill_matrix(m, p, q):
    global A, B, E, G
    A = [[round(random.uniform(-1,1.001), 3) for _ in range(m)] for i in range(p)]
    B = [[round(random.uniform(-1,1.001), 3) for _ in range(q)] for i in range(m)]
    E = [[round(random.uniform(-1,1.001), 3) for _ in range(m)] for i in range(1)]
    G = [[round(random.uniform(-1,1.001), 3) for _ in range(q)] for i in range(p)]

def find_C(x, y, m):
    global C, Tavg

    def find_impl(u, v):
        return compare(diff(1, u), v, 1)

    def find_compose(f, d):
        return compare(f, d, 0)

    def find_kf(i, j):
        global A, B, E, G, mult_call, diff_call, sum_call, compare_call, n, Tn, p, q, m, Tavg
        multipl_arr = []
        for k in range(m):
            old_mult_call, old_diff_call, old_sum_call, old_compare_call = mult_call, diff_call, sum_call, compare_call
            a_to_b = find_impl(A[i][k], B[k][j])
            b_to_a = find_impl(B[k][j], A[i][k])
            #f = a_to_b*(2*E[0][k]-1)*E[0][k] + b_to_a*(1+(4*a_to_b-2)*E[0][k])*(1-E[0][k])
            term1 = mult(mult(a_to_b, diff(mult(2, E[0][k]), 1)), E[0][k])
            term2 = mult(mult(b_to_a, sum(1, (mult(diff(mult(4, a_to_b), 2), E[0][k])))), diff(1, E[0][k]))
            print("f " + str(term1+term2))
            multipl_arr.append(sum(term1, term2))
            Tn += math.ceil(((mult_call - old_mult_call)*t_mult + (diff_call - old_diff_call)*t_diff +
                            (sum_call - old_sum_call)*t_sum+(compare_call - old_compare_call)*t_comparison)/n)
        kf = multipl_arr[0]
        old_mult_call = mult_call
        for i_mult in range(1, len(multipl_arr)):
            kf = mult(kf, multipl_arr[i_mult])   
        Tn += math.ceil((mult_call - old_mult_call) * t_mult/n)
        #Tavg += p * q * m * 2*(3*(t_diff + t_comparison) + 7*t_mult + 3*t_diff + 2*t_sum)
        print(kf)
        return kf
    
    def find_dd(i, j):
        nonlocal m
        global A, B, mult_call, diff_call, sum_call, compare_call, n, Tn, Tavg, q, p
        multipl_arr = []
        for k in range(m):
            old_mult_call, old_diff_call, old_sum_call, old_compare_call = mult_call, diff_call, sum_call, compare_call
            multipl_arr.append(diff(1, compare(A[i][k], B[k][j], 0)))
            Tn += math.ceil(((mult_call - old_mult_call)*t_mult + (diff_call - old_diff_call)*t_diff +
                            (sum_call - old_sum_call)*t_sum+(compare_call - old_compare_call)*t_comparison)/n)
        dd_res = multipl_arr[0]
        old_mult_call, old_diff_call = mult_call, diff_call
        for i_mult in range(1, len(multipl_arr)):
            dd_res = mult(dd_res, multipl_arr[i_mult])
        dd = diff(1, dd_res)
        print("dd " + str(dd))
        Tn += math.ceil(((mult_call - old_mult_call)*t_mult + (diff_call - old_diff_call)*t_diff)/n)
        #Tavg += p * q * m * 2 * t_comparison
        return dd

    def find_cij(i, j):
        global A, B, E, G, sum_call, diff_call, mult_call, compare_call, n, Tn  
        f = find_kf(i, j)
        d = find_dd(i, j)
        old_mult_call, old_diff_call, old_sum_call, old_compare_call = mult_call, diff_call, sum_call, compare_call 
        f_and_d = find_compose(f, d)
        print(f_and_d)
        cij = sum(mult(mult(f, diff(mult(3, G[i][j]), 2)), G[i][j]), 
                  mult(sum(d, mult(diff(mult(4, f_and_d), mult(3,d)), G[i][j])), diff(1, G[i][j])))
        Tn += math.ceil(((mult_call - old_mult_call)*t_mult + (diff_call - old_diff_call)*t_diff +
                        (sum_call - old_sum_call)*t_sum+(compare_call - old_compare_call)*t_comparison)/n)
        #cij = f*(3*G[i][j] - 2)*G[i][j] + (d+(4*f_and_d-3*d)*G[i][j])*(1-G[i][j])
        return cij

    #Tavg += 2 * x * y * (7 * t_mult + 2 * t_sum + 3 * t_diff + t_comparison) + 2 * ((m - 1) * t_mult + (m + 1) * t_diff) + 2 * ((m - 1) * t_mult)
    C = [[find_cij(i,j) for j in range(y)] for i in range(x)]

def main():
    global p, q, m,Tn, n
    while (1):
        m = input("m = ")
        p = input("p = ")
        q = input("q = ")
        n = input("количество процессорных элементов: ")
        #t_sum = int(input("Время операции суммирования: "))
        #t_mult = int(input("Время операции умножения: "))
        #t_diff = int(input("Время операции вычитания: "))
        #t_comparison = int(input("Время операции сравнения: "))

        if (check_input(m+p+q+n)):
            print("Некорректный ввод")
            continue
        elif int(n) == 0 or int(p) == 0 or int(m) == 0 or int(q) == 0:
            print("Введите значения больше 0")
            continue
        else:
            p = int(p)
            q = int(q)
            m = int(m)
            fill_matrix(m, p, q)
            n = int(n)
            find_C(int(p), int(q), int(m))
            break

    T1 = mult_call*t_mult + diff_call*t_diff +sum_call* t_sum + compare_call*t_comparison
    Ky = T1/Tn
    e = Ky/n
    r = p* q  + q* m + p*m + 1*m + p*q
    #Lavg = Tavg/(p* q * m) 
    Lavg = 2*(mult_call*t_mult + diff_call*t_diff +sum_call* t_sum + compare_call*t_comparison)/r    
    D = Tn/Lavg

    print_matrix(A, "A:")
    print_matrix(B, "B:")
    print_matrix(E, "E:")   
    print_matrix(G, "G:")
    print_matrix(C, "C:")
    print("T1 = " + str(T1))
    print("Tn = " + str(Tn))
    print("r = " + str(r))
    print("Ky = " + str(Ky))
    print("e = " + str(e))
    print("Lavg = " + str(Lavg))
    print("D = " + str(D))

main()


def main_graphics():
    global p, q, m, Tn, sum_call, mult_call, diff_call, compare_call, n, Tavg
    x = []
    d_= []
    ky_ = []

    for i in range(10):
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0,0,0,0
        m = i+1
        p = i+1
        q = i+1
        n = 4
        fill_matrix(int(m), int(p), int(q))
        find_C(int(p), int(q), int(m))
        r = p* q  + q* m + p*m + 1*m + p*q
        T1 = mult_call*t_mult + diff_call*t_diff +sum_call* t_sum + compare_call*t_comparison
        Ky = T1/Tn
        e = Ky/n
        Lavg = 2*(mult_call*t_mult + diff_call*t_diff +sum_call* t_sum + compare_call*t_comparison)/r #внутри программы
        D = Tn/Lavg #или pq2m / pq / или pqm
        ky_.append(Ky)
        d_.append(D)
        x.append(r)
    y2 = []
    for i in range(10):
        Tn, Tavg = 0, 0
        sum_call, mult_call, diff_call, compare_call = 0,0,0,0
        m = i+1
        p = i+1
        q = i+1
        n = 5
        fill_matrix(int(m), int(p), int(q))
        find_C(int(p), int(q), int(m))
        r = p* q  + q* m + p*m + 1*m + p*q
        print(r)
        T1 = mult_call*t_mult + diff_call*t_diff +sum_call* t_sum + compare_call*t_comparison
        Ky = T1/Tn
        e = Ky/n
        Lavg = 2*(mult_call*t_mult + diff_call*t_diff +sum_call* t_sum + compare_call*t_comparison)/r #внутри программы
        D = Tn/Lavg #или pq2m / pq / или pqm
        ky_.append(Ky)
        y2.append(D)

    import numpy as np
    import matplotlib.pyplot as plt
    y= d_
    plt.figure(figsize=(10,5))
    plt.plot(x,y,'k', label = 'n = 4')
    plt.plot(x, y2, label = "n = 5") 
    plt.xlabel('r', fontsize=14)
    plt.ylabel('D(r)', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.show()

#main_graphics()
