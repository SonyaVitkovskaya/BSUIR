import random
from lab_1 import sum
ALFABET =[0, 1]

def diag(words):
    massiv = [[0]*16 for i in range(16)]
    for line_index in range(len(words)):
        for i in range(line_index, len(words[line_index])):
            massiv[i][line_index] = words[line_index][i-line_index]
        for i in range(line_index):
            massiv[i][line_index] = words[line_index][16+i-line_index]
    return massiv
             
def writing(words, index, word):
    for i in range(len(word)):
        words[index][i] = int(word[i])

def reading(massiv, index):
    word = [massiv[line_ind][index] for line_ind in range(index, len(massiv))]
    word += [massiv[line_ind][index] for line_ind in range(index)]
    return word

def compare_words(word1, word2):
    g, l = False, False
    for i in range(16):
        s, a = int(word1[i]), int(word2[i])
        new_g = g or (not a and s and not l)
        new_l = l or (a and not s and not g)
        g, l = new_g, new_l
    if not g and not l: return 0
    elif g and not l: return 1
    elif not g and l: return -1

def f6_(massiv, index1, index2):
    array = transp(massiv.copy())
    line1 = array[index1]
    line2 = array[index2]
    answer = []
    for i in line1:
        answer.append(1) if line1[i] == line2[i] else answer.append(0)
    return answer

def f9_(massiv, index1, index2):
    array = transp(massiv.copy())
    line1 = array[index1]
    line2 = array[index2]
    answer = []
    for i in line1:
        answer.append(1) if line1[i] != line2[i] else answer.append(0)
    return answer

def f11_(massiv, index1, index2):
    array = transp(massiv.copy())
    line1 = array[index1]
    line2 = array[index2]
    answer = []
    for i in line1:
        answer.append(1) if line1[i] or not(line2[i]) else answer.append(0)
    return answer

def f4_(massiv, index1, index2):
    array = transp(massiv.copy())
    line1 = array[index1]
    line2 = array[index2]
    answer = []
    for i in line1:
        answer.append(1) if not(line1[i]) and line2[i] else answer.append(0)
    return answer

def sorting(matrix):
    result = []
    result.append(matrix[0])
    for line in range(1, len(matrix)):
        for elem in range(0, len(result)):
            if compare_words(''.join(map(str, result[elem])), ''.join(map(str, matrix[line])))==-1 or compare_words(''.join(map(str,matrix[elem])), ''.join(map(str, matrix[line])))==0:
                result.insert(elem, matrix[line])
                break
            else:
                if elem == len(result)-1:
                    result.append(matrix[line])
                    break
    return result

def addiction(words, mask):
    array = list(filter(lambda x: x[:3] == mask, words))
    new_mass = words.copy()
    inds = []
    for index in range(len(words)):
        if words[index] in array: inds.append([index, words[index]])
    for pair in inds:
        x1=''.join(map(str, pair[1][4:8]))
        x2 =''.join(map(str,pair[1][8:12]))
        new_mass[pair[0]][12:] = sum(f'0000000000000000000000000000{x1}',f'0000000000000000000000000000{x2}', '0')[28:]
    return new_mass

def transp(massiv):
        return [[massiv[j][i] for j in range(len(massiv))] for i in range(len(massiv[0]))]

def main():
    massiv = [[random.choice(ALFABET) for i in range(16)] for j in range(16)]
    words = [reading(massiv, i) for i in range(len(massiv))]
    for word in words:
        print(' '.join(map(str,word)))
    print("Диагональный вид: ")
    for line in massiv:
        print(' '.join(map(str, line)))
    word = reading(massiv, int(input("Введите индекс для чтения: ")))
    print(word)
    writing(words, int(input('Введите индекс ')), list(input("Введите слово ")))
    massiv = diag(words)
    for line in massiv:
        print(' '.join(map(str, line)))
    print('!x1 * x2' , f4_(massiv, 0, 1))
    print('!(x1~x2)', f6_(massiv, 0, 1))
    print('x1~x2', f9_(massiv, 0, 1))
    print('x1 + !x2', f11_(massiv, 0, 1))
    sort_res = sorting(words)
    #sort_res2 = sorting(transp(massiv))
    for line in sort_res:
        print(' '.join(map(str, line)))
    sec_rec = diag(sort_res)
    print('Диагональный вид сортировки: ')
    for line in sec_rec:
        print(' '.join(map(str, line)))
    add = diag(addiction(words, [0, 1, 1]))
    print('диагональный вид после сложения')
    for line in add:
        print(' '.join(map(str, line)))


main() 