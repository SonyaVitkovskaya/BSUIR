def formula_to_list(formula):
    formula = list(formula)
    i = 0
    max_x = 0
    while i < len(formula):
        if formula[i] == 'x' or formula[i] == '-':
            if formula[i] == 'x' and int(formula[i+1]) > max_x: max_x = int(formula[i+1])
            formula[i] += formula[i+1]
            formula.pop(i+1)
        if formula[i] == ' ': 
            formula.pop(i)
            i -= 1
        i += 1
    return formula, max_x

def calculations(expression):
    bin_operations_amount = expression.count('+') + expression.count('*') + expression.count('->') + expression.count('~')
    unar_operations = expression.count('!')
    while(bin_operations_amount or unar_operations):
        if bin_operations_amount == 1 and not(unar_operations): return binary_operations(expression)
        elif bin_operations_amount == 1 and expression.count('(')==0: return final_operation(expression)
        elif bin_operations_amount == 0 and unar_operations == 1: return unar_operation(expression[1])
        else:
            start_ind = find_index(expression)
            end_ind = expression.index(')', start_ind, len(expression))
            if (end_ind - start_ind) == 4:
                numeral = calculations(expression[start_ind + 1:end_ind])
                for i in range (0, end_ind - start_ind + 1, 1):
                    expression.pop(start_ind)
                expression.insert(start_ind, numeral)    
                bin_operations_amount -=1
            else: 
                not_ind = expression.index('!', start_ind, len(expression))
                numeral = unar_operation(expression[not_ind+1])
                expression.pop(not_ind)
                expression[not_ind] = numeral
                unar_operations -=1
    return expression

def find_index(expression):
    for index in range(len(expression) - 1, -1, -1):
        if expression[index] == '(': return index

def final_operation(expression):
    n = expression.count('!')
    while n > 0:
        not_ind = expression.index('!', 0, len(expression))
        numeral = unar_operation(expression[not_ind+1])
        expression.pop(not_ind)
        expression[not_ind] = numeral
        n -=1
    return calculations(expression)

def build_initial_table(amount_of_lines, amount_of_x) -> list:
    initial_table = []
    for k in range (0, amount_of_lines, 1): initial_table.append([])
    for i in range(0, amount_of_x, 1):
        amount_of_groups = 2**(i+1)
        lines_in_group = amount_of_lines/amount_of_groups
        numeral, line = '0', 1
        for j in range (0, amount_of_lines, 1):
            if line > lines_in_group:
                line = 1
                numeral = '0' if numeral == '1' else '1'
            initial_table[j].append(numeral)
            line += 1
    return initial_table

def binary_operations(expression) -> str:
    x1, operation, x2 = int(expression[0]), expression[1], int(expression[2])
    if operation == '~' :
        if (not(x1) and x2) or (x1 and not(x2)): return '0'
        else: return '1'
    if operation == '+' :
        if not(x1) and not(x2): return '0'
        else: return '1'
    if operation == '*':
        if not(x1) or not(x2): return '0'
        else: return '1'
    if operation == '->':
        if x1 == 1 and not(x2): return '0'
        else: return '1'

def unar_operation(x) -> str:
    return '0' if int(x) else '1'

def replace_x_with_numbers(formula, replacement_pairs):
    for formula_ind in range(0, len(formula), 1):
        for x_ind in range(0, len(replacement_pairs), 1):
            if formula[formula_ind] == replacement_pairs[x_ind][0]:
                formula[formula_ind] = replacement_pairs[x_ind][1]
    return formula

def sdnf(amount_of_lines, amount_of_x, initial_table, x_list, amount_of_1):
    sdnf = ''
    numeric_form = ''
    for lines_ind in range(0, amount_of_lines, 1):
        if initial_table[lines_ind][amount_of_x] == '1':
            numeric_form += str(lines_ind)
            conjunction = '('
            amount_of_1 -=1
            for column_ind in range(0, amount_of_x, 1):
                if initial_table[lines_ind][column_ind] == '0': 
                    conjunction += '!'
                conjunction += x_list[column_ind]
                conjunction += ' * ' if column_ind != amount_of_x - 1 else ')'
            sdnf += conjunction
            sdnf += ' + ' if amount_of_1 != 0 else ''
            numeric_form += ', ' if amount_of_1 != 0 else ''
    return sdnf, numeric_form

def scnf(amount_of_lines, amount_of_x, initial_table, x_list, amount_of_0):
    scnf = ''
    numeric_form = ''    
    for lines_ind in range(0 , amount_of_lines , 1):
        if initial_table[lines_ind][amount_of_x] == '0':
            numeric_form += str(lines_ind)
            disjunction = '('
            amount_of_0 -=1
            for column_ind in range(0, amount_of_x, 1):
                if initial_table[lines_ind][column_ind] == '1': disjunction += '!'
                disjunction += x_list[column_ind]
                disjunction += ' + ' if column_ind != (amount_of_x - 1) else ')'
            scnf += disjunction
            scnf += ' * ' if amount_of_0 != 0 else ''
            numeric_form += ', ' if amount_of_0 != 0 else ''
    return scnf, numeric_form

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
    Sdnf, numeric_sdnf = sdnf(amount_of_lines, amount_of_x, initial_table, x_list, amount_of_1)
    Scnf, numeric_scnf = scnf(amount_of_lines, amount_of_x, initial_table, x_list, amount_of_0)
    print(f'Sdnf = {Sdnf} = +({numeric_sdnf})\nScnf  = {Scnf} = *({numeric_scnf})')
    print(f'{index_form} = {int(index_form, 2)}({amount_of_x})')
    

while 1:
    formula = input('Введите формулу\n')
    if formula == 'end': break
    else: start(formula)