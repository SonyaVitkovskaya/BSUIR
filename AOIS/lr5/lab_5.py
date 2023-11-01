from lab_2 import build_initial_table, build_sdnf
from lab_1 import sum
from lab_4 import sdnf,computational_method_for_sdnf
AMOUNT_OF_ENTERS = 4
AMOUNT_OF_LINES = 2**AMOUNT_OF_ENTERS
ONE = '00000000000000000000000000000001'

def sdnf(init_table, to_add, x_list):
    amount_of_1 = 0
    for lines_ind in range(AMOUNT_OF_LINES*2):
        init_table[lines_ind][len(x_list)] = to_add[lines_ind]
        if to_add[lines_ind] == '1': amount_of_1 +=1
    Sdnf, numeric_sdnf = build_sdnf(AMOUNT_OF_LINES*2, len(x_list), init_table, x_list, amount_of_1)
    return Sdnf


def start():
    temp_initial_table = build_initial_table(AMOUNT_OF_LINES*2, AMOUNT_OF_ENTERS+1)
    initial_table = [temp_initial_table[i] for i in range(len(temp_initial_table)-1, -1,-1)]
    print('x1  x2  x3  x4  x5')
    print('q1* q2* q3* q4* v   q1 q2 q3 q4 h1 h2 h3 h4')
    q1, q2, q3, q4 = '', '', '', ''
    h1, h2, h3, h4 = '', '', '', ''
    for lines_ind in range(AMOUNT_OF_LINES*2):
        line_for_sum = '0000000000000000000000000000'
        line =''
        for column_ind in range(AMOUNT_OF_ENTERS+1): 
            line += initial_table[lines_ind][column_ind] + '   '
        for column_ind in range(AMOUNT_OF_ENTERS): 
            line_for_sum += initial_table[lines_ind][column_ind]
        q = sum(list(line_for_sum), list(ONE), '0') if initial_table[lines_ind][4]=='1' else line_for_sum
        q1 += q[28]
        h1+= '1' if q[28]!= initial_table[lines_ind][0] else '0'
        q2 += q[29]
        h2+= '1' if q[29]!= initial_table[lines_ind][1] else '0'
        q3 += q[30]
        h3+= '1' if q[30]!= initial_table[lines_ind][2] else '0'
        q4 += q[31]
        h4+= '1' if q[31]!= initial_table[lines_ind][3] else '0'
        line += q1[lines_ind] + '  ' + q2[lines_ind] + '  ' + q3[lines_ind] + '  ' + q4[lines_ind] + '  ' + \
            h1[lines_ind] + '  ' + h2[lines_ind] + '  ' + h3[lines_ind] + '  ' + h4[lines_ind]
        print(line)
        initial_table[lines_ind].append('')
    x_list = ['x1', 'x2', 'x3', 'x4', 'x5']
    sdnf1 = sdnf(initial_table, h1, x_list)
    print('СДНФ для h1:', sdnf1,'\n')
    print('Минимизированная СДНФ для h1:', computational_method_for_sdnf(sdnf1),'\n\n')
    sdnf2 = sdnf(initial_table, h2, x_list)
    print('СДНФ для h2:',sdnf2,'\n')
    print('Минимизированная СДНФ для h2:', computational_method_for_sdnf(sdnf2),'\n\n')
    sdnf3 = sdnf(initial_table, h3, x_list)
    print('СДНФ для h3:', sdnf3,'\n')
    print('Минимизированная СДНФ для h3:', computational_method_for_sdnf(sdnf3),'\n\n')
    sdnf4 = sdnf(initial_table, h4, x_list)
    print('СДНФ для h4:', sdnf4,'\n')
    print('Минимизированная СДНФ для h4:', computational_method_for_sdnf(sdnf4),'\n\n')





start()