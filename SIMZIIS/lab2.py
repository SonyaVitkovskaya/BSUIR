import random
from math import ceil
RUS_ALPHABET= "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def encryption(string, n):
    m = ceil(len(string)/n)
    to_add = m*n - len(string)
    for i in range(to_add):  string += random.choice(RUS_ALPHABET)

    matrix = []
    for i in range(m): matrix.append(list(string[i*n:i*n+n]))
    print_matr(matrix)

    encr_str = ''
    for j in range(n): 
        for i in range(m):  encr_str += matrix[i][j]
    print(encr_str)
    return encr_str
            
def print_matr(matrix):
    print("")
    for line in matrix:
        print(' '.join(line))     

def decription(string, source):
    for i in range(len(string)):
        for j in range(len(string)):
            if i*j != len(string): continue
            decr_string = encryption(string , i)
            if decr_string[:len(source)] == source: return [i, j]

def main():
    source_string = input("Введите строку для шифрования: ")
    string = source_string.replace(' ', '')
    n = int(input(f"Длина строки: {len(string)}\nВведите количество символов в строке : "))
    encr_string = encryption(string.lower(), n)
    decr_string = decription(encr_string, string)
    print(decr_string)

main()