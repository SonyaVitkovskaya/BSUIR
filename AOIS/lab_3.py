from lab_2 import calculations, formula_to_list, build_initial_table, replace_x_with_numbers, build_scnf, build_sdnf, unar_operation

def start(formula):
    form_lst, amount_of_x = formula_to_list(formula)
    x_list = []
    index_form = ''
    for lines_ind in range (0, amount_of_x, 1): x_list.append(f'x{lines_ind+1}')
    amount_of_lines = 2**amount_of_x
    initial_table = build_initial_table(amount_of_lines, amount_of_x)
    amount_of_1 = 0
    amount_of_0 = 0
    for lines_ind in range(0 , amount_of_lines , 1):
        replacement_pairs = []
        for columns_ind in range(0, amount_of_x, 1):
            replacement_pairs.append([x_list[columns_ind], initial_table[lines_ind][columns_ind]])
        result = calculations(replace_x_with_numbers(form_lst.copy(), replacement_pairs))
        initial_table[lines_ind].append(result)
        index_form += str(result)
        line =''
        for column_ind in range(0, amount_of_x + 1, 1): 
            line += initial_table[lines_ind][column_ind] + ' '
        print(line)
        if initial_table[lines_ind][amount_of_x] == '1': amount_of_1 +=1
        else: amount_of_0 +=1
    Sdnf, numeric_sdnf = build_sdnf(amount_of_lines, amount_of_x, initial_table, x_list, amount_of_1)
    Scnf, numeric_scnf = build_scnf(amount_of_lines, amount_of_x, initial_table, x_list, amount_of_0)
    print(index_form)
    print(f'СДНФ = {Sdnf}\nСКНФ = {Scnf}')
    print('Минимизация СДНФ расчетным методом: ', computational_method_for_sdnf(Sdnf))
    print('Минимизация СКНФ расчетным методом: ', computational_method_for_scnf(Scnf))
    print('Минимизация СДНФ расчетно-табличным методом: ')
    tabular_calculation_method_sdnf(Sdnf)
    print('Минимизация СКНФ расчетно-табличным методом: ')
    tabular_calculation_method_scnf(Scnf)
    print('Минимизациятабличным методом: ')
    tabular_method_sdnf(index_form)
    tabular_method_scnf(index_form)


def build_implicant_table(sXnf):
    implicant_table = []
    implicant_beginning = sXnf.index('(', 0, len(sXnf))
    while implicant_beginning < len(sXnf):
        implicant_end = sXnf.index(')', implicant_beginning, len(sXnf))
        implicant = []
        for index in range(implicant_beginning, implicant_end, 1):
            if sXnf[index][0] == 'x':
                if sXnf[index-1] == '!': implicant.append(f'!{sXnf[index]}')
                else: implicant.append(f'{sXnf[index]}')
        implicant_table.append(implicant)
        implicant_beginning = implicant_end + 2
    return implicant_table

def reduce_constituents(table, elements_in_impl):
    have_same_elements, reduced, not_intersected = {}, [], []
    for impl_ind in range(len(table)): not_intersected.append(impl_ind)
    for line_ind in range(0, len(table) - 1, 1):
        for line_ind_2 in range(line_ind + 1, len(table), 1):
            have_same_elements[f'{line_ind}{line_ind_2}'] = []
            if not(check_negation(table[line_ind], table[line_ind_2])): 
                have_same_elements.pop(f'{line_ind}{line_ind_2}')
                continue
            for index in range(len(table[line_ind])):
                if table[line_ind][index] in table[line_ind_2]:
                    have_same_elements[f'{line_ind}{line_ind_2}'].append(table[line_ind][index])
            if len(have_same_elements[f'{line_ind}{line_ind_2}']) + 1 < elements_in_impl: 
                have_same_elements.pop(f'{line_ind}{line_ind_2}')
            if f'{line_ind}{line_ind_2}' in have_same_elements:
                if line_ind in not_intersected: not_intersected.remove(line_ind)
                if line_ind_2 in not_intersected: not_intersected.remove(line_ind_2)
    reduced += have_same_elements.values()
    return reduced, not_intersected

def delete_same_implicants(table):
    index = 0
    while index < len(table):
        if table.count(table[index]) > 1: 
            table.pop(index)
            index-=1
        index += 1
    return table

def check_negation(list1, list2):
    is_crossing = True
    for index in range(0, len(list1)):
        if (not(list1[index] in list2)) and (not('!'+list1[index] in list2)) and (not(list1[index][1:] in list2)): is_crossing = False
        if (not(list2[index] in list1)) and (not('!'+list2[index] in list1)) and (not(list2[index][1:] in list1)): is_crossing = False
    return is_crossing

def build_abbreviated_implicants(sXnf, amount_of_rounds):
    abbreviated_implicants = []
    table = build_implicant_table(sXnf)
    elements_in_impl = amount_of_rounds
    for round in range(amount_of_rounds):
        implicants, aborts = reduce_constituents(table, elements_in_impl)
        for ind in range(len(aborts)): abbreviated_implicants.append(table[aborts[ind]])    
        elements_in_impl-=1
        table = delete_same_implicants(implicants)
    return abbreviated_implicants
    
def form_abbreviated_sdnf(abbreviated_implicants):
    abbrev_form = ''
    for implicant_ind in range(len(abbreviated_implicants)):
        conjunction = '('
        for index in range(len(abbreviated_implicants[implicant_ind])):
            conjunction += abbreviated_implicants[implicant_ind][index]
            conjunction += ' * ' if index != (len(abbreviated_implicants[implicant_ind])-1) else ')'
        abbrev_form += conjunction
        abbrev_form += ' + ' if implicant_ind != (len(abbreviated_implicants)-1)  else ''
    if len(abbrev_form)>0:
        return abbrev_form 
    else:  return 1

def form_abbreviated_scnf(abbreviated_implicants):
    abbrev_form = ''
    for implicant_ind in range(len(abbreviated_implicants)):
        conjunction = '('
        for index in range(len(abbreviated_implicants[implicant_ind])):
            conjunction += abbreviated_implicants[implicant_ind][index]
            conjunction += ' + ' if index != (len(abbreviated_implicants[implicant_ind])-1) else ')'
        abbrev_form += conjunction
        abbrev_form += ' * ' if implicant_ind != (len(abbreviated_implicants)-1)  else ''
    if len(abbrev_form)>0:
        return abbrev_form 
    else:  return 0

def computational_method_for_sdnf(Sdnf):
    sdnf, amount_of_x = formula_to_list(Sdnf)
    abbrev_table = build_abbreviated_implicants(sdnf, amount_of_x)
    print('Склеивание: ', form_abbreviated_sdnf(abbrev_table))
    comp_sdnf =[]
    for index in range(len(abbrev_table)):
        elements_values = {}
        for elem in abbrev_table[index]:
            if elem[0]=='!': elements_values[f'{elem[1:]}'] = '0'
            else: elements_values[f'{elem[0:]}'] = '1'
        others = []
        for index2 in range(len(abbrev_table)):
            if abbrev_table[index]!= abbrev_table[index2]:others.append(abbrev_table[index2])
        if necessity_check_sdnf(elements_values, others): comp_sdnf.append(abbrev_table[index])
    return form_abbreviated_sdnf(comp_sdnf)

def necessity_check_sdnf(elements_values, others):
    substitution_expression=[]
    for impl in others:
        replaced_impl=[]
        for elem_of_impl in impl:
            if elem_of_impl[0] == "!" and elem_of_impl[1:] in elements_values:
                replaced_impl.append(unar_operation(elements_values[elem_of_impl[1:]]))
            elif elem_of_impl in elements_values:
                replaced_impl.append(elements_values[elem_of_impl])
            else: replaced_impl.append(elem_of_impl)
        have_0 = False
        all_1 = True
        for elem in replaced_impl:
            if elem == '0': have_0 = True
            if elem != '1': all_1 = False
        if all_1: return False
        if have_0: continue
        else: 
            while replaced_impl.count('1'): replaced_impl.remove('1')
            substitution_expression.append(replaced_impl)
    if len(substitution_expression)==0: return True
    for elem in range(len(substitution_expression)):
       for elem2 in range(len(substitution_expression)):
        if len(substitution_expression[elem2]) == 1 and len(substitution_expression[elem]) == 1 \
            and (substitution_expression[elem][0] == f'!{substitution_expression[elem2][0]}' 
            or substitution_expression[elem2][0]== f'!{substitution_expression[elem][0]}'):
            substitution_expression.remove(substitution_expression[elem])
            elem-=1
            elem2-=1
            substitution_expression.remove(substitution_expression[elem2])
            break
    if len(substitution_expression) == 0: return False
    else:return True

def computational_method_for_scnf(Scnf):
    scnf, amount_of_x = formula_to_list(Scnf)
    abbrev_table = build_abbreviated_implicants(scnf, amount_of_x)
    print('Склеивание: ', form_abbreviated_sdnf(abbrev_table))
    comp_scnf =[]
    for index in range(len(abbrev_table)):
        elements_values = {}
        for elem in abbrev_table[index]:
            if elem[0]=='!': elements_values[f'{elem[1:]}'] = '1'
            else: elements_values[f'{elem[0:]}'] = '0'
        others = []
        for index2 in range(len(abbrev_table)):
            if abbrev_table[index]!= abbrev_table[index2]:others.append(abbrev_table[index2])
        if necessity_check_scnf(elements_values, others): comp_scnf.append(abbrev_table[index])
    return form_abbreviated_scnf(comp_scnf)

def necessity_check_scnf(elements_values, others):
    substitution_expression=[]
    for impl in others:
        replaced_impl=[]
        for elem_of_impl in impl:
            if elem_of_impl[0] == "!" and elem_of_impl[1:] in elements_values:
                replaced_impl.append(unar_operation(elements_values[elem_of_impl[1:]]))
            elif elem_of_impl in elements_values:
                replaced_impl.append(elements_values[elem_of_impl])
            else: replaced_impl.append(elem_of_impl)
        have_1 = False
        all_0 = True
        for elem in replaced_impl:
            if elem == '1': have_1 = True
            if elem != '0': all_0 = False
        if all_0: return False
        if have_1: continue
        else: 
            while replaced_impl.count('0'): replaced_impl.remove('0')
            substitution_expression.append(replaced_impl)
    if len(substitution_expression) == 0: return True
    for elem in range(len(substitution_expression)):
       for elem2 in range(len(substitution_expression)):
        if len(substitution_expression[elem2]) == 1 and len(substitution_expression[elem]) == 1 \
            and (substitution_expression[elem][0] == f'!{substitution_expression[elem2][0]}' 
            or substitution_expression[elem2][0]== f'!{substitution_expression[elem][0]}'):
            substitution_expression.remove(substitution_expression[elem])
            elem -= 1
            elem2 -= 1
            substitution_expression.remove(substitution_expression[elem2])
            break
    if len(substitution_expression) == 0: return False
    else:return True
                    
def tabular_calculation_method(Sxnf):
    sxnf, amount_of_x = formula_to_list(Sxnf)
    initial_implicants = build_implicant_table(sxnf)
    glued_implicants = build_abbreviated_implicants(sxnf, amount_of_x)
    table = []
    for lines in range(len(glued_implicants)):
        table.append([])
        for impl in range(len(initial_implicants)):
            all_here = True
            for elem in glued_implicants[lines]:
                if not(elem in initial_implicants[impl]): all_here = False
            table[lines].append('X') if all_here else table[lines].append(' ')
    return table, initial_implicants, glued_implicants

def tabular_calculation_method_sdnf(Sdnf):
    table, initial_implicants, glued_implicants = tabular_calculation_method(Sdnf)
    lines = to_string_sdnf(glued_implicants)
    colomns = to_string_sdnf(initial_implicants)
    print_table(lines, colomns, table)
    result = delete_unnecessary(table, glued_implicants)
    print('Результат: ', form_abbreviated_sdnf(result))

def tabular_calculation_method_scnf(Scnf):
    table, initial_implicants, glued_implicants = tabular_calculation_method(Scnf)
    lines = to_string_scnf(glued_implicants)
    colomns = to_string_scnf(initial_implicants)
    print_table(lines, colomns, table)
    result = delete_unnecessary(table, glued_implicants)
    print('Результат: ', form_abbreviated_scnf(result))
    
def to_string_scnf(lst):
    str_lst = []
    for inner_lst in lst:
        str_inner_lst = ''
        for elem in inner_lst:
            str_inner_lst += elem + '+'
        str_lst.append(str_inner_lst[:len(str_inner_lst)-1].ljust(15))
    return str_lst

def to_string_sdnf(lst):
    str_lst = []
    for inner_lst in lst:
        str_inner_lst = ''
        for elem in inner_lst:
            str_inner_lst += elem + '*'
        str_lst.append(str_inner_lst[:len(str_inner_lst)-1].ljust(15))
    return str_lst

def print_table(lines, colomns, table):
    init_impl = '               '
    for colomn in colomns:
        init_impl += colomn
    print(init_impl)
    for line_id in range(len(lines)):
        line = lines[line_id].ljust(17)
        for colomn_id in range(len(colomns)):
            line += table[line_id][colomn_id].ljust(15)
        print(line)    

def delete_unnecessary(table, glued_implicants):
    line = 0
    while line < len(table):
        all_unnecessary = True
        for elem_ind in range(len(table[line])):
            if not(table[line][elem_ind] == 'X'): continue
            unnecessary_elem = False
            for line_ind in range(len(table)): 
                if table[line_ind][elem_ind] == 'X' and line_ind!= line: unnecessary_elem = True
            if not(unnecessary_elem): 
                all_unnecessary = False
                break
        if all_unnecessary:
            glued_implicants.pop(line)
            table.pop(line)
            line-=1
        line+=1
    return glued_implicants


def tabular_method_sdnf(index_form):
    lst_ind_f = list(index_form)
    if len(index_form) == 8:
        lst_ind_f[6], lst_ind_f[7]=lst_ind_f[7], lst_ind_f[6]
        lst_ind_f[2], lst_ind_f[3]=lst_ind_f[3], lst_ind_f[2]
    for_0 = lst_ind_f[0:int(len(index_form)/2)]
    for_1 = lst_ind_f[int(len(index_form)/2):]
    map = ''
    for elem in for_0: map+=elem+'  '
    map+='\n'
    for elem in for_1: map+=elem+'  '
    print('Карта Карно:')
    print(map)
    print('Результат минимизации СДНФ: ', )
    sdnf_len = for_0.count('1') + for_1.count('1')
    if sdnf_len == 8:
        print('1')
        return
    implicants = find_pairs_sdnf(for_0, for_1)
    print(form_abbreviated_sdnf(implicants))

def find_pairs_sdnf(line1, line2):
    quad, pairs_1, pairs_2, vertical, singles, used1,used2 = [], [], [], [], [],[],[]
    for index in range(len(line1)): 
        if line1[index]=='1':
            if index < len(line1)-1: 
                if line1[index+1] == '1':
                    pairs_1.append([index, index+1]) 
                    used1.append(index+1)
                    used1.append(index)
                elif line2[index]==line1[index] and not(index in used1): 
                    vertical.append(index)
                    used1.append(index)
                elif not(index in used1) and not(index == 0 and line1[3]=='1'): singles.append(['!x1', index])
            else:
                if line1[0]=='1': 
                    pairs_1.append([index, 0])
                    used1.append(index)
                elif line2[index]==line1[index] and not(index in used1):
                    vertical.append(index)
                    used1.append(index)
                elif not(index in used1): singles.append(['!x1', index])
    for index in range(len(line2)): 
        if line2[index]=='1':
            if index < len(line2)-1: 
                if line2[index+1]=='1': 
                    pairs_2.append([index, index+1])
                    used2.append(index+1)
                    used2.append(index)
                elif line2[index]==line1[index] and not(index in used2) and not(index in vertical):
                    vertical.append(index)
                    used2.append(index)
                elif not(index in used2) and not(index == 0 and line2[3]=='1') and not(index in vertical): singles.append(['x1', index])
            else:
                if line2[0]=='1': 
                    pairs_2.append([index, 0])
                    used2.append(index+1)
                    used2.append(index)
                elif line2[index]==line1[index] and not(index in used2) and not(index in vertical):
                    vertical.append(index)
                    used2.append(index)
                elif not(index in used2)and not(index in vertical): singles.append(['x1', index])
    if len(pairs_1)==4: quad.append(['!x1'])
    else:
        for pair in pairs_1:
            if not(pair in pairs_2):
                if pair[0] == 0: quad.append(['!x1','!x2'])
                if pair[0] == 1: quad.append(['!x1','x3'])
                if pair[0] == 2: quad.append(['!x1','x2'])
                if pair[0] == 3: quad.append(['!x1','!x3'])
    if len(pairs_2)==4: quad.append(['x1'])
    else: 
        for pair in pairs_2:
            if not(pair in pairs_1):
                if pair[0] == 0: quad.append(['x1','!x2'])
                if pair[0] == 1: quad.append(['x1','x3'])
                if pair[0] == 2: quad.append(['x1','x2'])
                if pair[0] == 3: quad.append(['x1','!x3'])
    for pair in pairs_1:
        if pair in pairs_2:
            if pair[0] == 0: quad.append(['!x2'])
            if pair[0] == 1: quad.append(['x3'])
            if pair[0] == 2: quad.append(['x2'])
            if pair[0] == 3: quad.append(['!x3'])
    for index in vertical:
        need=2
        for elem in pairs_1:
            if index in elem:
                need-=1
                break
        for elem in pairs_2:
            if index in elem:
                need-=1
                break
        if need:
            if index == 0: quad.append(['!x2','!x3'])
            if index == 1: quad.append(['!x2','x3'])
            if index == 2: quad.append(['x2','x3'])
            if index == 3: quad.append(['x2','!x3'])
    for elem in singles:
        if elem[1]==0: quad.append([elem[0], '!x2','!x3'])
        if elem[1]==1: quad.append([elem[0], '!x2','x3'])
        if elem[1]==2: quad.append([elem[0], 'x2','x3'])
        if elem[1]==3: quad.append([elem[0], 'x2','!x3'])
    return quad
    
def tabular_method_scnf(index_form):
    lst_ind_f = list(index_form)
    if len(index_form) == 8:
        lst_ind_f[6], lst_ind_f[7]=lst_ind_f[7], lst_ind_f[6]
        lst_ind_f[2], lst_ind_f[3]=lst_ind_f[3], lst_ind_f[2]
    for_0 = lst_ind_f[0:int(len(index_form)/2)]
    for_1 = lst_ind_f[int(len(index_form)/2):]
    print('Результат минимизации СКНФ:', )
    sdnf_len = for_0.count('0') + for_1.count('0')
    if sdnf_len == 8:
        print('0')
        return
    implicants = find_pairs_scnf(for_0, for_1)
    print(form_abbreviated_scnf(implicants))


def find_pairs_scnf(line1, line2):
    quad, pairs_1, pairs_2, vertical, singles, used1,used2 = [], [], [], [], [],[],[]
    for index in range(len(line1)): 
        if line1[index]=='0':
            if index < len(line1)-1: 
                if line1[index+1] == '0':
                    pairs_1.append([index, index+1]) 
                    used1.append(index+1)
                    used1.append(index)
                elif line2[index]==line1[index] and not(index in used1):
                    vertical.append(index)
                    used1.append(index)
                elif not(index in used1) and not(index == 0 and line1[3]=='0'): singles.append(['x1', index])
            else:
                if line1[0]=='0':  
                    pairs_1.append([index, 0])
                    used1.append(index)
                elif line2[index]==line1[index] and not(index in used1):
                    vertical.append(index)
                    used1.append(index)
                elif not(index in used1): singles.append(['x1', index])                
            
    for index in range(len(line2)): 
        if line2[index]=='0':
            if index < len(line2)-1: 
                if line2[index+1]=='0': 
                    pairs_2.append([index, index+1])
                    used2.append(index+1)
                    used2.append(index)
                elif line2[index]==line1[index] and not(index in used2) and not(index in vertical):
                    vertical.append(index)
                    used2.append(index)
                elif not(index in used2) and not(index == 0 and line2[3]=='0')and not(index in vertical): singles.append(['!x1', index])
            else:
                if line2[0]=='0': 
                    pairs_2.append([index, 0])
                    used2.append(index+1)
                    used2.append(index)
                elif line2[index]==line1[index] and not(index in used2) and not(index in vertical):
                    vertical.append(index)
                    used2.append(index)
                elif not(index in used2)and not(index in vertical): singles.append(['!x1', index])
    if len(pairs_1)==4: quad.append(['x1'])
    else:
        for pair in pairs_1:
            if not(pair in pairs_2):
                if pair[0] == 0: quad.append(['x1','x2'])
                if pair[0] == 1: quad.append(['x1','!x3'])
                if pair[0] == 2: quad.append(['x1','!x2'])
                if pair[0] == 3: quad.append(['x1','x3'])
    if len(pairs_2)==4: quad.append(['!x1'])
    else:
        for pair in pairs_2:
            if not(pair in pairs_1):
                if pair[0] == 0: quad.append(['!x1','x2'])
                if pair[0] == 1: quad.append(['!x1','!x3'])
                if pair[0] == 2: quad.append(['!x1','!x2'])
                if pair[0] == 3: quad.append(['1x1','x3'])
    for pair in pairs_1:
        if pair in pairs_2:
            if pair[0] == 0: quad.append(['x2'])
            if pair[0] == 1: quad.append(['!x3'])
            if pair[0] == 2: quad.append(['!x2'])
            if pair[0] == 3: quad.append(['x3'])
    for index in vertical:
        need=2
        for elem in pairs_1:
            if index in elem:
                need-=1
                break
        for elem in pairs_2:
            if index in elem:
                need-=1
                break
        if need:
            if index == 0: quad.append(['x2','x3'])
            if index == 1: quad.append(['x2','!x3'])
            if index == 2: quad.append(['!x2','!x3'])
            if index == 3: quad.append(['!x2','x3'])
    for elem in singles:
        if elem[1]==0: quad.append([elem[0], 'x2','x3'])
        if elem[1]==1: quad.append([elem[0], 'x2','!x3'])
        if elem[1]==2: quad.append([elem[0], '!x2','!x3'])
        if elem[1]==3: quad.append([elem[0], '!x2','x3'])
    return quad

while(1):
    start(input('Введите формулу: '))