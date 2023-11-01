import random
from lab_2 import build_initial_table, formula_to_list, calculations, replace_x_with_numbers
WORD_LENGTH = 4
MASSIV_LENGTH = 15
ALFABET = '01'

def set_random_numbers():
    processor = []
    for word_ind in range(MASSIV_LENGTH):
        word = ''
        for digit_ind in range(WORD_LENGTH): word += random.choice(ALFABET)
        processor.append(word)
        print(f'[{word_ind}] ',word)
    return processor

def compare_words(word, search_word):
    g, l = False, False
    for i in range(WORD_LENGTH):
        s, a = int(word[i]), int(search_word[i])
        new_g = g or (not a and s and not l)
        new_l = l or (a and not s and not g)
        g, l = new_g, new_l
    if not g and not l: return 0
    elif g and not l: return 1
    elif not g and l: return -1

def find_nearest_smaller(smaller):
    biger_from_small = smaller[0]
    for index in range(1, len(smaller)):
        if compare_words(biger_from_small, smaller[index]) == -1:
            biger_from_small = smaller[index]
    return biger_from_small

def find_nearest_bigger(bigger):
    smaller_from_big = bigger[0]
    for index in range(1, len(bigger)):
        if compare_words(smaller_from_big, bigger[index]) == 1:
            smaller_from_big = bigger[index]
    return smaller_from_big

def find_nearest(processor, word):
    bigger_words, smaller_words = [], []
    for elem in processor:
        compare_result = compare_words(elem, word)
        if compare_result == 1: bigger_words.append(elem)
        if compare_result == -1: smaller_words.append(elem)
    nearest_bigger = find_nearest_bigger(bigger_words)
    nearest_smaller = find_nearest_smaller(smaller_words)
    return nearest_bigger, nearest_smaller

def find_from_bool_func(processor, formula):
    form_lst, amount_of_x = formula_to_list(formula)
    index_form, x_list = '', []
    for lines_ind in range (0, amount_of_x, 1): x_list.append(f'x{lines_ind+1}')
    amount_of_lines = 2**amount_of_x
    initial_table = build_initial_table(amount_of_lines, amount_of_x)
    for lines_ind in range(0 , amount_of_lines , 1):
        replacement_pairs = []
        for columns_ind in range(0, amount_of_x, 1): replacement_pairs.append([x_list[columns_ind], initial_table[lines_ind][columns_ind]])
        result = calculations(replace_x_with_numbers(form_lst.copy(), replacement_pairs))
        initial_table[lines_ind].append(result)
        index_form += str(result)
        line =''
        for column_ind in range(0, amount_of_x + 1, 1): line += initial_table[lines_ind][column_ind] + ' '
        print(line)
    print('Найти: ', index_form)
    for word_ind in range(len(processor)):
        if compare_words(processor[word_ind], index_form) == 0: break
    else: return -1
    return word_ind

def main():
    processor = set_random_numbers()
    bigger, smaller = find_nearest(processor, input('Введите число для поиска ближайших  '))
    print('Ближайшее сверху: ', bigger, '\nснизу:  ', smaller)
    sec_res = find_from_bool_func(processor, input('Введите формулу: '))
    if sec_res == -1:
        print('Не найдено')
    else: print(f'[{sec_res}]  ', processor[sec_res])
    
main()
