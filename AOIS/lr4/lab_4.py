from lab_3 import computational_method_for_sdnf
from lab_2 import build_initial_table, build_sdnf
from lab_1 import sum

AMOUNT_OF_ENTERS_FOR_TASK1 = 3
AMOUNT_OF_LINES_FOR_TASK1 = 2**AMOUNT_OF_ENTERS_FOR_TASK1
AMOUNT_OF_ENTERS_FOR_TASK2 = 4
AMOUNT_OF_LINES_FOR_TASK2 = 2**AMOUNT_OF_ENTERS_FOR_TASK2
TASK2_NUMBER_4  = '00000000000000000000000000000100'

def summator(table):
    s, p = [], []
    for index in range(len(table)):
        preliminary_result = int(table[index][0]) + int(table[index][1]) + int(table[index][2])
        if preliminary_result == 0 or preliminary_result == 1:
            s.append(str(preliminary_result))
            p.append('0')
        else:
            s.append('0') if preliminary_result == 2 else s.append('0')
            p.append('1')
    return s, p

def sdnf(init_table, to_add, x_list):
    amount_of_1 = 0
    for lines_ind in range(2**len(x_list)):
        init_table[lines_ind][len(x_list)] = to_add[lines_ind]
        if to_add[lines_ind] == '1': amount_of_1 +=1
    Sdnf, numeric_sdnf = build_sdnf(2**len(x_list), len(x_list), init_table, x_list, amount_of_1)
    return Sdnf

def task1():
    initial_table = build_initial_table(AMOUNT_OF_LINES_FOR_TASK1, AMOUNT_OF_ENTERS_FOR_TASK1)
    summa, transfer = summator(initial_table)
    print('x1 x2 x3 S  P')
    for lines_ind in range(AMOUNT_OF_LINES_FOR_TASK1):
        line =''
        for column_ind in range(AMOUNT_OF_ENTERS_FOR_TASK1): 
            line += initial_table[lines_ind][column_ind] + '  '
        line += summa[lines_ind] + '  ' + transfer[lines_ind]
        print(line)
        initial_table[lines_ind].append('')
    tab_sum = sdnf(initial_table, summa, ['x1', 'x2', 'x3'])
    minim_tab_sum = computational_method_for_sdnf(tab_sum)
    tab_trans = sdnf(initial_table, transfer, ['x1', 'x2', 'x3'])
    minim_tab_trans = computational_method_for_sdnf(tab_trans)
    print(f'СДНФ для S: {tab_sum} \nМинимизированная СДНФ для S: {minim_tab_sum}')
    print(f'СДНФ для P: {tab_trans} \nМинимизированная СДНФ для P: {minim_tab_trans}')

def task2():
    initial_table = build_initial_table(AMOUNT_OF_LINES_FOR_TASK2, AMOUNT_OF_ENTERS_FOR_TASK2)
    print('x1 x2 x3 x4 y1 y2 y3 y4')
    y1, y2, y3, y4 = '', '', '', ''
    for lines_ind in range(AMOUNT_OF_LINES_FOR_TASK2):
        line_for_sum = '0000000000000000000000000000'
        line =''
        for column_ind in range(AMOUNT_OF_ENTERS_FOR_TASK2): 
            line += initial_table[lines_ind][column_ind] + '  '
            line_for_sum += initial_table[lines_ind][column_ind]
        if lines_ind >= 10:
                y1 += '-'
                y2 += '-'
                y3 += '-'
                y4 += '-'
        else: 
            y = sum(list(line_for_sum), list(TASK2_NUMBER_4), '0')
            y1 += y[28]
            y2 += y[29]
            y3 += y[30]
            y4 += y[31]
        line += y1[lines_ind] + '  ' + y2[lines_ind] + '  ' + y3[lines_ind] + '  ' + y4[lines_ind]
        print(line)
        initial_table[lines_ind].append('')
    sdnf_y1 = sdnf(initial_table, y1, ['x1', 'x2', 'x3', 'x4'])
    minim_y1 = computational_method_for_sdnf(sdnf_y1)
    sdnf_y2 = sdnf(initial_table, y2, ['x1', 'x2', 'x3', 'x4'])
    minim_y2 = computational_method_for_sdnf(sdnf_y2)
    sdnf_y3 = sdnf(initial_table, y3, ['x1', 'x2', 'x3', 'x4'])
    minim_y3 = computational_method_for_sdnf(sdnf_y3)
    sdnf_y4 = sdnf(initial_table, y4, ['x1', 'x2', 'x3', 'x4'])
    minim_y4 = computational_method_for_sdnf(sdnf_y4)
    print(f'СДНФ для y1: {sdnf_y1} \nМинимизированная СДНФ для y1: {minim_y1}')
    print(f'СДНФ для y2: {sdnf_y2} \nМинимизированная СДНФ для y2: {minim_y2}')
    print(f'СДНФ для y3: {sdnf_y3} \nМинимизированная СДНФ для y3: {minim_y3}')
    print(f'СДНФ для y4: {sdnf_y4} \nМинимизированная СДНФ для y4: {minim_y4}')


task1()
task2()

