"""Лабораторная работа 1 по дисциплине 'Модели решения задач в интеллектуальных системах'
Выполнили: студентки гр.121702  Витковская С.И., Мойсевич А.В.
Вариант 13: алгоритм вычисления произведения пары 8-разрядных чисел умножением с младших разрядов со сдвигом множимого влево"""

import os
ALFABET = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
ALL_BITES = 8
NULL_STR = "0000000000000000"
RESULT_BITES = 2*ALL_BITES

class Utils():
    def convert_direct(self, x_int) -> str:
        if x_int == 0 : return NULL_STR
        number_itself = ''
        while abs(x_int) > 0:
            number_itself = str(abs(x_int) % 2) + number_itself
            x_int = abs(x_int) // 2
        return "".join(["0" for _ in range(ALL_BITES - len(number_itself))]) + number_itself
  
    def check(self, x):
        for symbol in x:
            if symbol not in ALFABET: return "Неверный формат"
        if int(x)<0 or int(x)>255: return "Выход за пределы допустимых значений"    
        return ""

class Pair():
    def __init__(self, x1, x2, n):
        self.x1 = x1
        self.x2 = x2
        self.current_sum = NULL_STR
        self.current_mult = NULL_STR
        self.index = 0
        self.result = ""
        self.pair_num = n

    def sum(self, x1, x2) -> str:
        sum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for index in range(RESULT_BITES - 1, -1, -1):
            preliminary_result = int(x1[index]) + int(x2[index]) + int(sum[index])
            if preliminary_result == 0 or preliminary_result == 1:
                sum[index] = str(preliminary_result)
            else:
                sum[index] = '0' if preliminary_result == 2 else '1'
                if index != 0: sum[index - 1] += 1
                else: return 'Переполнение'
        return ''.join(sum)

    def partial_multiplication(self, i):
        if self.x2[ALL_BITES-1-i] == "0":
            self.current_mult = NULL_STR
        else:
            self.current_mult = self.x1 + "".join(["0" for j in range(i)])
            self.current_mult = "".join(["0" for j in range(RESULT_BITES - len(self.current_mult))]) + self.current_mult

    def part_sum(self):
        if self.result == "":
            self.partial_multiplication(self.index)
            self.current_sum = self.sum(self.current_mult, self.current_sum)
        self.index +=1            
        if self.index == ALL_BITES: 
            self.result = self.current_sum



class Conveyor():
    def __init__(self):
        self.pairs = []
        self.queue_len = 0
        self.utils = Utils()

    def entry(self):
        while(1):
            queue = input("Введите размер очереди: ")
            if len(set(queue).difference(set(ALFABET)))>0:
                print("Неверный формат")
            else:
                self.queue_len = int(queue)
                break
        print('Принимаемый формат чисел: неотрицательные целые числа в пределах от 0 до 255')
        while(1):
            for n in range(self.queue_len):
                x1 = input(f'Введите первое число {n+1} пары: ')
                check_res = conveyor.utils.check(x1)
                if check_res != "": 
                    print(check_res)
                    self.pairs = []
                    break
                x2 = input(f'Введите второе число {n+1} пары: ')
                check_res = conveyor.utils.check(x2)
                if check_res != "": 
                    print(check_res)
                    self.pairs = []
                    break
                self.pairs.append(Pair(self.utils.convert_direct(int(x1)),self.utils.convert_direct(int(x2)), n))
            if len(self.pairs) == self.queue_len: break

    def write_pairs(self):
        for pair in self.pairs:
            print(f"Пара {pair.pair_num + 1}: {int(pair.x1, 2)} = {pair.x1}, {int(pair.x2, 2)} = {pair.x2}")

    def write_tacts(self):
        self.write_pairs()
        for i in range(ALL_BITES):
            str1 = f"Этап {i+1} "
            str2 = ""
            for pair in self.pairs:
                if pair.index == i + 1:
                    str1 += f"Пара {pair.pair_num + 1}"
                    str2 += f"Частичная сумма: {pair.current_sum} = {int(pair.current_sum,2)}, Частичное произведение: {pair.current_mult} = {int(pair.current_mult, 2)}"
                    break
            print(str1)
            print(str2)

    def write_results(self):
        for j in range(self.queue_len):
            if self.pairs[j].result != "" and self.pairs[j].index != ALL_BITES:
                print(f"Результат {j+1}: {self.pairs[j].result} = {int(self.pairs[j].result, 2 )}")

    def algorithm(self):
        for i in range(ALL_BITES + self.queue_len - 1):                
            for pair in self.pairs: 
                if pair.pair_num <= i and pair.index <= ALL_BITES:
                    pair.part_sum()   
            print(f"Такт {i+1}")       
            self.write_tacts()
            self.write_results()
            input()
            os.system('cls')
        self.write_pairs()
        for j in range(self.queue_len):
            print(f"Результат {j+1}: {self.pairs[j].result} = {int(self.pairs[j].result, 2 )}")     

conveyor = Conveyor()
conveyor.entry()
conveyor.algorithm()