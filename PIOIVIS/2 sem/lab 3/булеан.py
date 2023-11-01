import itertools
import re

def main():
    setX = create_set()
    setX=del_povtor(setX)
    print('{',end='')
    for item in setX:
        if item != setX[len(setX) - 1]:
            print(item, end=',')
        else:
            print(item, end='')
    print('}')
    print('Булеан: ')
    boolean_set(setX)
    
def correct_input(inp: str) -> bool:
    perm_char = r'[a-zA-Z0-9\<\>\{\}\,]'
    result = False
    for char in inp:
        if re.search(perm_char, char):
            result = True
        else:
            return False
    return result

def del_povtor(list):
    temp = []
    for x in list:
        if x not in temp:
            temp.append(x)
    return temp


def check_set(inp: str) -> list:
    perm_element = r'[a-zA-Z0-9]+'
    perm_element2 = r'[\{\}]+'
    temp_list = []
    inp = inp.split('{',1)[1]
    inp = inp.rsplit('}',1)[0]
    inp = inp.split(',')
    for element in inp:
        if re.search(perm_element2, element):
            elementz=list(element)
            check_element(elementz,inp)
        if re.search(perm_element, element):
            temp_list.append(element)
    return sorted(temp_list)

def check_element(temp: list,inp):
    if inp[0] == "{":
        temp_list = check_set(inp)
        s = '{'
        for item in temp_list:
            if item != temp_list[len(temp_list) - 1]:
                s += str(item) + ', '
            else:
                s += str(item)
        s += '}'
        temp.append(s)
    elif correct_input(inp):
        temp.append(inp)
        return
    else:
        print('не то: ')
        inp2 = str(input())
        check_element(temp, inp2)

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

def boolean_set(set_i: list)->list:
    boolean = []      
    st=''
    print("{", end='')
    for r in range(len(set_i)+1) :
        if r>0:
            if r==1:
                st+='{}'
            else:
                st+=',{}'
        temp = list(itertools.combinations(set_i, r))
        for i in temp:
            boolean.append(i)
            if r==len(set_i):
                print('{'+st.format(*i),end="") 
                if i==temp[len(temp)-1]:
                    print('}',end="")  
                else:
                    print('},',end="")
            else:
                print('{'+st.format(*i)+'},',end="") 
    print("}")
    

main()