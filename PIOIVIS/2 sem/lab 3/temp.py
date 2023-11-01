from булеан import *


def main():
    setX = create_set()
    print('{',end='')
    for item in setX:
        if item != setX[len(setX) - 1]:
            print(item, end=',')
        else:
            print(item, end='')
    print('}')
    print('Булеан: ')
    boolean_set(setX)

def create_set() -> list:
    temp_set = []
    size = int(input("Введите мощность множества: "))
    print("Введите элементы множества: ")
    for i in range(size):
        inp = str(input())
        check_element(temp_set,inp)
    my_list = []
    for item in temp_set:
        my_list.append(item)
    return my_list

main()