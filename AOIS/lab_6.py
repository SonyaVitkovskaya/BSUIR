TABLE_LEN = 20
KEY_IND = 0
V_IND = 1
H_IND = 2
COLLIS_IND = 3
U_IND = 4
T_IND = 5
D_IND = 6
NEXT_IND = 7
DATA_IND = 8


def get_number(word):
    alfabet = {'а':0,'б':1,'в':2,'г':3,'д':4,'е':5,'ж':6,'з':7,'и':8,'й':9,'к':10,'л':11,'м':12,'н':13,'о':14,'п':15,'р':16,'с':17,'т':18,'у':19,'ф':20,'х':21,'ц':22,'ч':23,'ш':24,'щ':25,'ъ':26,'ы':27,'ь':28,'э':29,'ю':30,'я':31}
    value = alfabet[word[0].lower()]*32 + alfabet[word[1].lower()]
    return value, value % TABLE_LEN

def add_elem(key, data, table):
    v, h = get_number(key)
    collis, prev_ind = 0, 0
    for ind in range(len(table)):
        if table[ind][H_IND] == h and table[ind][NEXT_IND] == '':
            table[ind][COLLIS_IND] = 1
            collis = 1
            prev_ind = ind
            table[ind][T_IND] = 0
    for note_ind in range(len(table)):
        if table[note_ind][U_IND] == 0:
            table[note_ind][KEY_IND] = key
            table[note_ind][V_IND] = v
            table[note_ind][H_IND] = h
            table[note_ind][COLLIS_IND] = collis
            table[note_ind][DATA_IND] = data
            table[note_ind][U_IND] = 1
            table[note_ind][T_IND] = 1
            if collis == 1: table[prev_ind][NEXT_IND] = note_ind
            break

def find(table, key):
    for note in table:
        if note[KEY_IND]==key:
            print(note[KEY_IND].ljust(15) + str(note[V_IND]).ljust(6) +str(note[H_IND]).ljust(3)
               + str(note[COLLIS_IND]).ljust(2)+str(note[U_IND]).ljust(2)+str(note[T_IND]).ljust(2)
               +str(note[D_IND]).ljust(2)+str(note[NEXT_IND]).ljust(5)+note[DATA_IND])
            
def delete(table, key):
    for note_ind in range(len(table)):
        if table[note_ind][KEY_IND] == key:
            if table[note_ind][COLLIS_IND] == 1:
                prev_ind, prev_prev_ind = '', ''
                for ind in range(len(table)):
                    if table[ind][NEXT_IND] == note_ind:
                        prev_ind = ind
                        break
                for ind in range(len(table)):
                    if table[ind][NEXT_IND] == prev_ind:
                        prev_prev_ind = ind
                        break
                if prev_ind == '' and table[table[note_ind][NEXT_IND]][T_IND]==1:
                    table[table[note_ind][NEXT_IND]][COLLIS_IND]==0
                elif table[note_ind][T_IND]==1 and prev_prev_ind == '':
                    table[prev_ind][T_IND]=1
                    table[prev_ind][COLLIS_IND]=0
                    table[prev_ind][NEXT_IND]=''
                elif table[note_ind][T_IND]== 0 and prev_prev_ind == '':
                    table[prev_ind][NEXT_IND] = table[note_ind][NEXT_IND]
                elif prev_prev_ind != '' and table[note_ind][T_IND]==1:
                    table[prev_ind][T_IND]=1
                    table[prev_ind][NEXT_IND]=''
            table[note_ind][KEY_IND]=''
            table[note_ind][V_IND]=''
            table[note_ind][H_IND]=''
            table[note_ind][COLLIS_IND] = 0
            table[note_ind][U_IND]= 0
            table[note_ind][T_IND]= 0
            table[note_ind][D_IND]=0
            table[note_ind][NEXT_IND]=''
            table[note_ind][DATA_IND]=''
            break



def print_table(table):
    print('№  key            value h  c u t d next data')
    ind = 0
    for note in table:
        print(str(ind).ljust(3) +note[KEY_IND].ljust(15) + str(note[V_IND]).ljust(6) +str(note[H_IND]).ljust(3)
               + str(note[COLLIS_IND]).ljust(2)+str(note[U_IND]).ljust(2)+str(note[T_IND]).ljust(2)
               +str(note[D_IND]).ljust(2)+str(note[NEXT_IND]).ljust(5)+note[DATA_IND])
        ind+=1








table = []
for index in range(TABLE_LEN):
    table.append(['','','',0,0,1,0,'',''])
add_elem('Неман', 'река', table)
add_elem('Эверест', 'гора', table)
add_elem('Беларусь', "государство", table )
add_elem('Везувий', 'вулкан', table)
add_elem('Мадагаскар', "остров", table )
add_elem('Гродно', "город", table )
add_elem('Гомель', "город", table )
add_elem('Евразия', 'континент', table)
add_elem('Янцзы', 'река', table)
add_elem('Антарктида', 'континент', table)
add_elem('Альборан', 'море', table)
add_elem('Байкал', 'озеро', table)
add_elem('Макалу', 'гора', table)
add_elem('Минск', 'город', table)
add_elem('Амур', 'река', table)
add_elem('Ява', 'остров', table)
add_elem('Чогори', 'гора', table)
add_elem('Танганьика', 'озеро', table)
add_elem('Нил', 'река', table)
add_elem('Амазонка', 'река', table)
print_table(table)

find(table, input('Найти: '))
delete(table, input('Удалить: '))
print_table(table)
add_elem(input(),input(),table)
print_table(table)