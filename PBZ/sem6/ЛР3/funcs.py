from tkinter import *
from tkinter import ttk

#создание фрейма в окне с текстом, аргументы: отображаемый текст и окно
def create_frame(label_text, root):
    frame = ttk.Frame(root, borderwidth=1, relief=SOLID, padding=[15, 10])
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    return frame

#создание фрейма в окне с текстом и объектом ввода, аргументы: отображаемый текст и окно
def create_frame_with_entry(label_text, root):
    frame = create_frame(label_text, root)
    entry = ttk.Entry(frame, width=30)
    entry.pack(anchor=NW)
    return frame, entry

#создание фрейма в окне с текстом, объектом ввода и кнопкой, аргументы: отображаемый текст, окно, комманда кнопки, текст кнопки
def create_frame_with_entry_and_button(label_text, root, btn_command, btn_text):
    frame, entry = create_frame_with_entry(label_text, root)
    ttk.Button(frame, text=btn_text, command=btn_command, width=20).pack(anchor=NW)
    return frame, entry

#создание окна с заданным названием и размером
def create_window(text, size):
    window = Tk()
    window.title(text)
    window.geometry(size)
    return window

#создание ряда кнопок в передаваемом в качестве аргумента фрейме, итерация по названию кнопок и их командам
def create_buttons_row(frame, text_lst, comands, status):
    btns = []
    for i in range(len(comands)):
        button = ttk.Button(frame, text=text_lst[i], command=comands[i], width= 42, state=status)
        button.pack(anchor=N,side=LEFT)
        btns.append(button)
    return btns

#создание таблицы
def create_table(columns, col_names, table, rows):
    for i in range(len(columns)):
        table.heading(columns[i], text=f"{col_names[i]}", anchor = CENTER)
        table.column(f"#{i+1}", anchor = CENTER)
    for row in rows:
        table.insert("", END, values=row)
    scrolltable = Scrollbar(table, command=table.yview)
    table.configure(yscrollcommand=scrolltable.set)
    scrolltable.pack(side=RIGHT, fill=Y)
    table.pack(expand=YES, fill=BOTH)
