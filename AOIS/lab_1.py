import math
NULL_STR = '00000000000000000000000000000000'
ONE_STR = '00000000000000000000000000000001'
FIRST_MANT_INDEX = 9
ALL_BITES = 32
DEFAULT_EXP = 127
MANTISSA_BITES = 23
FIRST_INDEX = 0
LAST_INDEX = 31


def sum(x1, x2, sign) -> str:
    sum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sum[FIRST_INDEX] = sign
    for index in range(LAST_INDEX, FIRST_INDEX, -1):
        preliminary_result = int(x1[index]) + int(x2[index]) + int(sum[index])
        if preliminary_result == 0 or preliminary_result == 1:
            sum[index] = str(preliminary_result)
        else:
            sum[index] = '0' if preliminary_result == 2 else '1'
            if index != FIRST_INDEX + 1: sum[index - 1] += 1
            else: return 'Переполнение'
    return ''.join(sum)

def sum_for_same_sign(x1, x2) -> str:
    sign = x1[FIRST_INDEX]
    if sign == '0': return sum(x1, x2, sign)
    else: return sum(convert_return(x1), convert_return(x2), '1')

def compare_moduls(x1, x2, are_same, from_ind, to_ind) -> str:
    start_index_x1 = find_start_index(x1,'0', from_ind, to_ind)
    if are_same: 
        start_index_x2 = find_start_index(x2,'0', from_ind, to_ind)
    else: 
        start_index_x2 = find_start_index(x2,'1', from_ind, to_ind)
    if (start_index_x1 == 'none' and start_index_x2 !='none'): return 'x2'
    elif (start_index_x2 == 'none' and start_index_x1 !='none'): return 'x1'
    elif (start_index_x1 == 'none' and start_index_x2 =='none'): return 'same'
                
    if start_index_x1 == start_index_x2:
        if int(start_index_x1) == to_ind:
            return 'same'
        else:
            return compare_moduls(x1, x2, are_same, int(start_index_x1) + 1, to_ind)
    elif start_index_x1 < start_index_x2: return 'x1'
    else: return 'x2'

def sum_for_diff_signs(positive, negative) -> str:
    larger_modul = compare_moduls(positive, negative, False, FIRST_INDEX + 1, LAST_INDEX)
    if larger_modul == 'same': return NULL_STR
    elif larger_modul == 'x2': return convert_return(sum(positive, negative, '1'))
    else: return sum_if_positive_bigger(positive, negative)

def sum_if_positive_bigger(x1, x2) -> str:
    result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    result[FIRST_INDEX] = '0'
    for index in range(LAST_INDEX, FIRST_INDEX, -1):
        preliminary_result = int(x1[index]) + int(x2[index]) + result[index]
        if preliminary_result == 0 or preliminary_result == 1:
            result[index] = str(preliminary_result)
        else:
            result[index] = '0' if preliminary_result == 2 else '1'
            if index != FIRST_INDEX + 1: result[index-1] += 1
    return sum(result, ONE_STR, '0')

def addition(x1, x2) -> str:
    if x1[FIRST_INDEX] == x2[FIRST_INDEX]: 
        return sum_for_same_sign(x1, x2)
    elif x1[FIRST_INDEX] == '1':
        positive = x1
        negative = x2
    else:
        positive = x2
        negative = x1
    return sum_for_diff_signs(positive, negative)

def subtraction(x1, x2) -> str:
    x1_list = list(x1)
    x2_list = list(x2)
    if x2_list[FIRST_INDEX] == '1': 
        x2_list = list(convert_return(x2))
        x2_list[FIRST_INDEX] = '0'
    else: 
        x2_list[FIRST_INDEX] = '1'
        x2_list = list(convert_return(''.join(x2_list)))
    return addition(''.join(x1_list),''.join(x2_list))

def convert_direct(x_int) -> str:
    if x_int == 0 : return NULL_STR
    x_str = '0' if x_int > 0 else '1'
    number_itself = ''
    while abs(x_int) > 0:
        number_itself = str(abs(x_int) % 2) + number_itself
        x_int = abs(x_int) // 2
    for i in range(LAST_INDEX - len(number_itself), FIRST_INDEX, -1):
        x_str += '0'
    x_str += number_itself
    return x_str

def convert_return(x_str) -> str:
    if list(x_str)[FIRST_INDEX] == '1': 
        result = '1' 
        for index in range(FIRST_INDEX + 1, ALL_BITES, 1):
            result += '1' if list(x_str)[index] == '0' else '0'
        return result
    else: return x_str
    
def convert_additional(x) -> str:
    return sum(ONE_STR, x, '1') if x[FIRST_INDEX] == '1' else x 

def find_start_index(x, sign, from_index, to_index) -> str:
    to_find = '1' if sign == '0' else '0'
    for index in range(from_index, to_index + 1, 1): 
        if x[index] == to_find:
            return str(index)
    return 'none'
            
def multiplication(x1, x2):
    start_ind_1 = int(find_start_index(x1, '0', FIRST_INDEX + 1, LAST_INDEX))
    start_ind_2 = int(find_start_index(x2, '0', FIRST_INDEX + 1, LAST_INDEX))
    if (start_ind_1 + start_ind_2) <= ALL_BITES: return 'Перегрузка'
    result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    result[FIRST_INDEX] = '1' if x1[FIRST_INDEX] != x2[FIRST_INDEX] else '0' 
    for x2_index in range(LAST_INDEX, FIRST_INDEX, -1):
        if x2[x2_index] == '1': 
            for index in range(x2_index, FIRST_INDEX, -1):
                result[index] += int(x1[LAST_INDEX - x2_index + index])
    for result_ind in range(LAST_INDEX, FIRST_INDEX, -1):
        if result[result_ind] == 0 or result[result_ind] == 1:
            result[result_ind]= str(result[result_ind])
        else:
            if result_ind != FIRST_INDEX + 1:
                result[result_ind - 1] += (int(result[result_ind])//2)
            else: return 'Переполнение'
            result[result_ind] = '0' if result[result_ind] % 2 == 0 else '1'  
    return ''.join(result)

def division(x1, x2):
    dividend = divisor = ''
    if compare_moduls(x1, x2, True, FIRST_INDEX + 1, LAST_INDEX) == 'same':
        if x1[FIRST_INDEX] == x2[FIRST_INDEX]: return ONE_STR
        else: 
            result = list(ONE_STR)
            result[FIRST_INDEX] == '1'
            return ''.join(result)
    elif compare_moduls(x1, x2, True, FIRST_INDEX + 1, LAST_INDEX) == 'x1':
        dividend = x1
        divisor = x2
    else:
        return NULL_STR
    result = '1' if x1[FIRST_INDEX] != x2[FIRST_INDEX] else '0'
    division = division_operation(dividend, divisor)
    for i in range(LAST_INDEX-len(division), FIRST_INDEX, -1): 
        result += '0'
    result += division
    return result

def division_operation(dividend, divisor) -> str:
    result_str = ''
    start_index1 = int(find_start_index(dividend, '0', FIRST_INDEX + 1, LAST_INDEX))
    start_index2 = int(find_start_index(divisor, '0', FIRST_INDEX + 1, LAST_INDEX))
    divisor_size = ALL_BITES - start_index2
    last_digit = start_index1 + divisor_size - 1
    dividend_temp = []
    divisor_temp = []
    for ind in range(start_index1, last_digit + 1, 1):
        dividend_temp.append(dividend[ind])
    for ind in range(start_index2, ALL_BITES, 1): 
        divisor_temp.append(divisor[ind])
    str_divison = ''.join(divisor_temp)
    while(last_digit <= LAST_INDEX):
        x1 = x2 = '0'
        while (len(dividend_temp) - len(divisor_temp)) > 0: divisor_temp.insert(FIRST_INDEX,'0')
        while (len(dividend_temp) - len(divisor_temp)) < 0: dividend_temp.insert(FIRST_INDEX,'0')
        while(compare_moduls(dividend_temp, divisor_temp, True, 0, len(dividend_temp) - 1 ) == 'x2'):
            result_str += '0'
            divisor_temp.insert(0,'0')
            last_digit += 1
            if last_digit == ALL_BITES: return result_str
            dividend_temp.append(dividend[last_digit])  
        for i in range(LAST_INDEX-len(''.join(dividend_temp)), FIRST_INDEX, -1): 
            x1 += '0'
            x2 += '0'
        x1 += ''.join(dividend_temp)
        x2 += ''.join(divisor_temp)
        substraction_result = list(subtraction(x1, x2))
        if find_start_index(substraction_result,'0', FIRST_INDEX + 1 ,LAST_INDEX) != 'none':
            from_id = int(find_start_index(substraction_result,'0', FIRST_INDEX + 1 ,LAST_INDEX))
            dividend_temp = []
            for ind in range(from_id, ALL_BITES, 1): 
                dividend_temp.append(substraction_result[ind])
        else: dividend_temp = []
        divisor_temp = list(str_divison)
        last_digit += 1
        if last_digit < ALL_BITES: dividend_temp.append(dividend[last_digit])
        result_str += '1'
    return result_str

def find_mant_for_not0(x_integer_decimal, x_fractional_decimal) -> list:
    x_integer_binary = list(convert_direct(x_integer_decimal))
    while x_integer_binary[FIRST_INDEX] != '1': x_integer_binary.pop(FIRST_INDEX)
    x_integer_binary.pop(FIRST_INDEX)
    x_integer_binary = ''.join(x_integer_binary)
    x_fractional_binary = ''
    while len(x_fractional_binary) + len(x_integer_binary) < MANTISSA_BITES:
        x_fractional_decimal *= 2
        x_fractional_binary += '0' if math.floor(x_fractional_decimal) == 0 else '1'
        if x_fractional_decimal >= 1: 
            x_fractional_decimal = x_fractional_decimal - 1 
    mantissa = x_integer_binary + x_fractional_binary
    order = len(x_integer_binary)
    return [mantissa, order]
        
def find_mant_for_0(x_fractional_decimal) -> list:
    x_fractional_binary = ''
    while len(x_fractional_binary) < ALL_BITES:
        x_fractional_decimal *= 2
        x_fractional_binary += '0' if math.floor(x_fractional_decimal) == 0 else '1'
        if x_fractional_decimal >= 1: 
            x_fractional_decimal = x_fractional_decimal - 1 
    order = 0
    mantissa = list(x_fractional_binary)
    while mantissa[FIRST_INDEX] != '1':
        mantissa.pop(FIRST_INDEX)
        order -= 1
    mantissa.pop(FIRST_INDEX)
    order -= 1
    while len(mantissa) < MANTISSA_BITES:
        mantissa += '0'
    return [''.join(mantissa), order]

def convert_float(x_decimal) -> str:
    if x_decimal == 0: return NULL_STR
    sign = '0' if x_decimal > 0 else '1'
    x_integer_decimal = math.floor(abs(x_decimal) // 1)
    x_fractional_decimal = abs(x_decimal) - x_integer_decimal
    mantissa_and_order = [] 
    if x_integer_decimal != 0:
        mantissa_and_order = find_mant_for_not0(x_integer_decimal, x_fractional_decimal)
    else: mantissa_and_order = find_mant_for_0(x_fractional_decimal)
    mantissa = list(mantissa_and_order[0])
    order = mantissa_and_order[1]  
    exp = convert_direct(order + DEFAULT_EXP)
    for index in range (LAST_INDEX, MANTISSA_BITES, -1):
        mantissa.insert(FIRST_INDEX, exp[index])
    result = sign + ''.join(mantissa[FIRST_INDEX:LAST_INDEX])
    return result

def convert_return_float(x) -> str:
    return x[FIRST_INDEX:FIRST_MANT_INDEX] + convert_return(x)[FIRST_MANT_INDEX:ALL_BITES]
    
def sum_float(x1, x2):
    exp1 = int(x1[FIRST_INDEX + 1:FIRST_MANT_INDEX], 2) - DEFAULT_EXP
    exp2 = int(x2[FIRST_INDEX + 1:FIRST_MANT_INDEX], 2) - DEFAULT_EXP
    exp = 0
    smaller = bigger = []
    if exp1 < exp2:
        bigger = list(x2[FIRST_INDEX]+x2[FIRST_MANT_INDEX:ALL_BITES])
        smaller = list(x1[FIRST_INDEX]+x1[FIRST_MANT_INDEX:ALL_BITES])
        exp = exp2
    else :
        bigger = list(x1[FIRST_INDEX]+x1[FIRST_MANT_INDEX:ALL_BITES])
        smaller = list(x2[FIRST_INDEX]+x2[FIRST_MANT_INDEX:ALL_BITES])
        exp = exp1
    add_0 = abs(exp1-exp2)

    def positive(x, is_bigger):
        x.insert(FIRST_INDEX + 1, '1')
        for i in range(FIRST_INDEX, add_0, 1):
            x.append('0') if is_bigger else x.insert(FIRST_INDEX + 1,'0')   
        while len(x) < ALL_BITES: x.insert(FIRST_INDEX, '0')
        return x
        
    def negative(x, is_bigger):
        x.insert(FIRST_INDEX + 1, '0')
        for i in range(FIRST_INDEX, add_0, 1):
            x.append('1') if is_bigger else x.insert(FIRST_INDEX + 1,'1')     
        while len(x) < ALL_BITES: x.insert(FIRST_INDEX, '1')
        return x
    
    term1 = positive(bigger, True) if bigger[0]=='0' else negative(bigger, True)
    term2 = positive(smaller, False) if smaller[0]=='0' else negative(smaller, False)
    sum = list(addition((''.join(term1))[0:ALL_BITES],(''.join(term2))[0:ALL_BITES]))
    sign = sum[FIRST_INDEX]
    sum.pop(FIRST_INDEX)
    mantissa = []
    overload = False 
    default_amount_0 = ALL_BITES - (MANTISSA_BITES + 1) - 1 #7
    only_0 = default_amount_0 - add_0
    for index in range(FIRST_INDEX, only_0, 1):
        if sum[index] == '1': overload = True
    if overload: 
        exp += 1
        mantissa = sum[(only_0) : (only_0+MANTISSA_BITES)]
    else:
        decrease_digit = 0
        while only_0 + decrease_digit < LAST_INDEX - 1 and sum[(only_0) + decrease_digit] != '1': decrease_digit += 1
        exp -= decrease_digit
        mantissa = sum[(only_0 + decrease_digit + 1):ALL_BITES]
        while len(mantissa) < MANTISSA_BITES: mantissa.append('0')
    exponenta = convert_direct(exp + DEFAULT_EXP)
    for index in range (LAST_INDEX, MANTISSA_BITES, - 1): mantissa.insert(FIRST_INDEX, exponenta[index])
    result = sign + ''.join(mantissa[FIRST_INDEX:LAST_INDEX])
    return result


    




x1_pos = 10
x2_pos = 18
print('Числа введенные в системе: ', x1_pos, 'и ', x2_pos, ', ввести новые числа?')
if input('1)Да\n2)Нет\n') == '1':
    x1_pos = math.floor(abs(float(input())))
    x2_pos = math.floor(abs(float(input())))
x1_neg = x1_pos * (-1)
x2_neg = x2_pos * (-1)

x1_pos_direct = convert_direct(x1_pos)
x2_pos_direct = convert_direct(x2_pos)
x1_neg_direct = convert_direct(x1_neg)
x2_neg_direct = convert_direct(x2_neg)

x1_pos_return = convert_return(x1_pos_direct)
x2_pos_return = convert_return(x2_pos_direct)
x1_neg_return = convert_return(x1_neg_direct)
x2_neg_return = convert_return(x2_neg_direct)

sum_pos_pos = addition(x1_pos_return, x2_pos_return)
sum_neg_neg = addition(x1_neg_return, x2_neg_return)
sum_pos1_neg2 = addition(x1_pos_return,x2_neg_return)
sum_neg1_pos2 = addition(x1_neg_return,x2_pos_return)

x1_pos_additional = convert_additional(x1_pos_direct)
x2_pos_additional = convert_additional(x2_pos_direct)
x1_neg_additional = convert_additional(x1_neg_return)
x2_neg_additional = convert_additional(x2_neg_return)

subtr_pos_pos = subtraction(x1_pos_return, x2_pos_return)
subtr_pos_neg = subtraction(x1_pos_return, x2_neg_return)
subtr_neg_pos = subtraction(x1_neg_return, x2_pos_return)
subtr_neg_neg = subtraction(x1_neg_return, x2_neg_return)

division_pos_pos = division(x1_pos_direct, x2_pos_direct)
division_pos_neg = division(x1_pos_direct, x2_neg_direct)
division_neg_pos = division(x1_neg_direct, x2_pos_direct)
division_neg_neg = division(x1_neg_direct, x2_neg_direct)

multipl_pos_pos = multiplication(x1_pos_direct, x2_pos_direct)
multipl_pos_neg = multiplication(x1_pos_direct, x2_neg_direct)
multipl_neg_pos = multiplication(x1_neg_direct, x2_pos_direct)
multipl_neg_neg = multiplication(x1_neg_direct, x2_neg_direct)

print('В двоичной системе ', x1_pos, ': ', x1_pos_direct)
print('В двоичной системе ', x2_pos, ': ', x2_pos_direct)
print('В двоичной системе ', x1_neg, ': ', x1_neg_direct)
print('В двоичной системе ', x2_neg, ': ', x2_neg_direct, '\n')

while(1):
    print('Выберите операцию:\n1.Перевод в обратный код')
    print('2.Перевод в дополнительный код')
    print('3.Арифметические операции')
    print('4.Ввести дробные числа')
    choice = input('5.Завершить работу\n')
    if choice == '1':
        print('Обратный код ', x1_pos, ': ', x1_pos_return)
        print('Обратный код ', x2_pos, ': ', x2_pos_return)
        print('Обратный код ', x1_neg, ': ', x1_neg_return)
        print('Обратный код ', x2_neg, ': ', x2_neg_return, '\n')
    elif choice == '2':
        print('Дополнительный код ', x1_pos, ': ', x1_pos_additional)
        print('Дополнительный код ', x2_pos, ': ', x2_pos_additional)
        print('Дополнительный код ', x1_neg, ': ', x1_neg_additional)
        print('Дополнительный код ', x2_neg, ': ', x2_neg_additional, '\n')
    elif choice == '3':
        choice_2 = input('Выберите операцию:\n1.Сложение\n2.Вычитание\n3.Умножение\n4.Деление\n')
        if choice_2 == '1':
            choise_3 = input('Выберите знаки слагаемых:\n1.++\n2.+-\n3.-+\n4.--\n')
            if choise_3 == '1': print(x1_pos, '+', x2_pos, ':', sum_pos_pos)
            elif choise_3 == '2': print(x1_pos, '+', x2_neg, ':', sum_pos1_neg2)
            elif choise_3 == '3': print(x1_neg, '+', x2_pos, ':', sum_neg1_pos2)
            elif choise_3 == '4': print(x1_neg, '+', x2_neg, ':', sum_neg_neg)
        elif choice_2 == '2':
            choise_3 = input('Выберите знаки:\n1.++\n2.+-\n3.-+\n4.--\n')
            if choise_3 == '1': print(x1_pos, '-', x2_pos, ':', subtr_pos_pos)
            elif choise_3 == '2': print(x1_pos, '-', x2_neg, ':', subtr_pos_neg)
            elif choise_3 == '3': print(x1_neg, '-', x2_pos, ':', subtr_neg_pos)
            elif choise_3 == '4': print(x1_neg, '-', x2_neg, ':', subtr_neg_neg)
        elif choice_2 == '3':
            choise_3 = input('Выберите знаки:\n1.++\n2.+-\n3.-+\n4.--\n')
            if choise_3 == '1': print(x1_pos, '*', x2_pos, ':', multipl_pos_pos)
            elif choise_3 == '2': print(x1_pos, '*', x2_neg, ':', multipl_pos_neg)
            elif choise_3 == '3': print(x1_neg, '*', x2_pos, ':', multipl_neg_pos)
            elif choise_3 == '4': print(x1_neg, '*', x2_neg, ':', multipl_neg_neg)
        elif choice_2 == '4':
            choise_3 = input('Выберите знаки:\n1.++\n2.+-\n3.-+\n4.--\n')
            if choise_3 == '1': print(x1_pos, '/', x2_pos, ':', division_pos_pos)
            elif choise_3 == '2': print(x1_pos, '/', x2_neg, ':', division_pos_neg)
            elif choise_3 == '3': print(x1_neg, '/', x2_pos, ':', division_neg_pos)
            elif choise_3 == '4': print(x1_neg, '/', x2_neg, ':', division_neg_neg)
    elif choice == '4':
        x1_pos_float = 0.3
        x2_pos_float = 0.5
        print(f'Числа введенные в системе:{x1_pos_float} и {x2_pos_float}, ввести новые числа?')
        if input('1)Да\n2)Нет\n') == '1':
            x1_pos_float = abs(float(input()))
            x2_pos_float = abs(float(input()))
        x1_neg_float = x1_pos_float * (-1)
        x2_neg_float = x2_pos_float * (-1)
        x1_pos_mantissa = convert_float(x1_pos_float)
        x2_pos_mantissa = convert_float(x2_pos_float)
        x1_neg_mantissa = convert_float(x1_neg_float)
        x2_neg_mantissa = convert_float(x2_neg_float)

        print('В двоичной системе ', x1_pos_float, ': ', x1_pos_mantissa)
        print('В двоичной системе ', x2_pos_float, ': ', x2_pos_mantissa)
        print('В двоичной системе ', x1_neg_float, ': ', x1_neg_mantissa)
        print('В двоичной системе ', x2_neg_float, ': ', x2_neg_mantissa, '\n')

        x1mant_pos_return = convert_return_float(x1_pos_mantissa)
        x2mant_pos_return = convert_return_float(x2_pos_mantissa)
        x1mant_neg_return = convert_return_float(x1_neg_mantissa)
        x2mant_neg_return = convert_return_float(x2_neg_mantissa)

        print('Обратный код: ', x1mant_pos_return)
        print('Обратный код: ', x2mant_pos_return)
        print('Обратный код: ', x1mant_neg_return)
        print('Обратный код: ', x2mant_neg_return, '\n')

        sum_mant_pos_pos = sum_float(x1mant_pos_return, x2mant_pos_return)
        sum_mant_pos_neg = sum_float(x1mant_pos_return, x2mant_neg_return)
        sum_mant_neg_pos = sum_float(x1mant_neg_return, x2mant_pos_return)
        sum_mant_neg_neg = sum_float(x1mant_neg_return, x2mant_neg_return)
        choice = input('Сумма: \n1)++\n2)+-\n3)-+\n4)--\n')
        if choice == '1': print(sum_mant_pos_pos)
        elif choice == '2': print(sum_mant_pos_neg)
        elif choice == '3': print(sum_mant_neg_pos)
        elif choice == '4': print(sum_mant_neg_neg)
    elif choice == '5':
        break

