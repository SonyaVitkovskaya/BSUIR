from tkinter import *
from tkinter import ttk
from requests import take_max, insert_note, take_rows, delete_row
from checks import *
from tkinter.messagebox import showerror
from funcs import *

def officers_wind():

    def item_selected(event):
        return off_table.selection()[0]

    def insert_in_off(full_name, job, id):
        err_string = ""
        if job == '': err_string += "Должность не выбрана"
        if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
        else:
            insert_note("traffic_police_officer", f"({id}, '{full_name}', '{job}')")
            off_table.insert("", END, values=take_rows("traffic_police_officer", condition= f"WHERE id = {id}")[0])
        
    def add_note_off():
        add_note_window = create_window("Добавление записи о сотруднике", "400x200")
        fr1, full_name = create_frame_with_entry("Введите полное имя", add_note_window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr2 = create_frame("Выберите должность", add_note_window)
        job = StringVar(fr2)
        rb1 = ttk.Radiobutton(fr2, text="инженер по техническому осмотру транспортных средств", value="инженер по техническому осмотру транспортных средств", variable=job)
        rb2 = ttk.Radiobutton(fr2, text="инженер по допуску ТС к участию в дорожном движении", value="инженер по допуску ТС к участию в дорожном движении", variable=job)
        rb1.pack(anchor=NW)
        rb2.pack(anchor=NW)
        fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
        id = take_max("traffic_police_officer", "id")+1
        add_note_btn = ttk.Button(add_note_window, text="Внести запись", command=lambda: insert_in_off(full_name.get(),job.get(), id))
        add_note_btn.place(x = 130, y = 165, width = 140, height = 22)

    def del_selected_note_off(item_id):
        id = off_table.item(item_id)["values"][0]
        off_table.delete(item_id)
        delete_row("traffic_police_officer", f"id={id}")

    def edit_off(full_name, job, id, item_id):
        id = off_table.item(item_id)["values"][0]
        off_table.delete(item_id)
        delete_row("traffic_police_officer", f"id={id}")
        insert_in_off(full_name, job, id)

    def edit_note_off(item_id):
        edit_note_window = create_window("Редактирование записи о сотруднике", "400x200")
        fr1, full_name = create_frame_with_entry("Введите полное имя", edit_note_window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr2 = create_frame("Выберите должность", edit_note_window)
        job = StringVar(fr2)
        rb1 = ttk.Radiobutton(fr2, text="инженер по техническому осмотру транспортных средств", value="инженер по техническому осмотру транспортных средств", variable=job)
        rb2 = ttk.Radiobutton(fr2, text="инженер по допуску ТС к участию в дорожном движении", value="инженер по допуску ТС к участию в дорожном движении", variable=job)
        rb1.pack(anchor=NW)
        rb2.pack(anchor=NW)
        fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
        id = take_max("traffic_police_officer", "id")+1
        edit_note_btn = ttk.Button(edit_note_window, text="Редактировать запись", command=lambda: edit_off(full_name.get(),job.get(), id, item_id))
        edit_note_btn.place(x = 130, y = 165, width = 140, height = 22)

    off_window = create_window("Сотрудники участка", "850x400")
    top = Frame(off_window)
    top.pack()
    off_columns = ("id", "full_name", "job_title")
    off_rows = take_rows("traffic_police_officer")
    off_table = ttk.Treeview(off_window, columns = off_columns, show="headings")
    create_table(off_columns, ["ID", "ФИО", "Должность"], off_table, off_rows)
    off_table.column("#1", width=10)
    off_table.column("#2", width=150)
    off_table.column("#3", width=300)
    
    off_table.bind("<<TreeviewSelect>>", item_selected)
    create_buttons_row(top, ["Добавить запись", "Редактировать запись", "Удалить запись"], [add_note_off,  lambda:  edit_note_off(item_selected("<<TreeviewSelect>>")), lambda: del_selected_note_off(item_selected("<<TreeviewSelect>>"))])
