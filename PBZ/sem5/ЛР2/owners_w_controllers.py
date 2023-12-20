from tkinter import *
from tkinter import ttk
from requests import take_max, insert_note, take_rows, delete_row
from checks import *
from tkinter.messagebox import showerror
from funcs import *

def owners_wind():

    def item_selected(event):
        return owners_table.selection()[0]

    def insert_in_owners(license_number, full_name, sex, dob, place_of_registration):
        err_string = ""
        if lisence_number_check(license_number) == '': err_string += "Некорректный ввод номера удостоверения\n"
        if sex == '': err_string += "Пол не выбран\n"
        if date_check(dob) == '': err_string += "Некорректный ввод даты рождения\n"
        if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
        else:
            insert_note("owner", f"('{license_number}', '{full_name}', '{sex}', '{dob}', '{place_of_registration}')")
            owners_table.insert("", END, values=take_rows("owner", condition= f"WHERE license_number = '{license_number}'")[0])
        
    def add_note_owners():
        add_note_window = create_window("Добавление записи о владельце", "400x430")
        fr1, license_number = create_frame_with_entry("Введите номер водительского удостоверения", add_note_window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr2, full_name = create_frame_with_entry("Введите полное имя", add_note_window)
        fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr3 = create_frame("Выберите пол", add_note_window)
        sex = StringVar(fr3)
        rb1 = ttk.Radiobutton(fr3, text="Ж", value="Ж", variable=sex)
        rb2 = ttk.Radiobutton(fr3, text="М", value="М", variable=sex)
        rb1.pack(anchor=NW)
        rb2.pack(anchor=NW)
        fr3.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr4, dob = create_frame_with_entry("Введите дату рождения в формате ГГГГ-ММ-ДД", add_note_window)
        fr4.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr5, place_of_registration = create_frame_with_entry("Введите адрес прописки", add_note_window)
        fr5.pack(anchor=NW, fill=X, padx=5, pady=5)
        add_note_btn = ttk.Button(add_note_window, text="Внести запись", command=lambda: insert_in_owners(license_number.get(),full_name.get(),sex.get(), dob.get(), place_of_registration.get()))
        add_note_btn.place(x = 130, y = 395, width = 140, height = 22)

    def del_selected_note_owners(item_id):
        id = owners_table.item(item_id)["values"][0]
        owners_table.delete(item_id)
        delete_row("owner", f"license_number='{id}'")

    def edit_owners(license_number, full_name, sex, dob, place_of_registration, item_id):
        id = owners_table.item(item_id)["values"][0]
        owners_table.delete(item_id)
        delete_row("owner", f"id={id}")
        insert_in_owners(license_number, full_name, sex, dob, place_of_registration)

    def edit_note_owners(item_id):
        edit_note_window = create_window("Редактирование записи о владельце", "400x430")
        fr1, license_number = create_frame_with_entry("Введите номер водительского удостоверения", edit_note_window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr2, full_name = create_frame_with_entry("Введите полное имя", edit_note_window)
        fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr3 = create_frame("Выберите пол", edit_note_window)
        sex = StringVar(fr3)
        rb1 = ttk.Radiobutton(fr3, text="Ж", value="Ж", variable=sex)
        rb2 = ttk.Radiobutton(fr3, text="М", value="М", variable=sex)
        rb1.pack(anchor=NW)
        rb2.pack(anchor=NW)
        fr3.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr4, dob = create_frame_with_entry("Введите дату рождения в формате ГГГГ-ММ-ДД", edit_note_window)
        fr4.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr5, place_of_registration = create_frame_with_entry("Введите адрес прописки", edit_note_window)
        fr5.pack(anchor=NW, fill=X, padx=5, pady=5)

        edit_note_btn = ttk.Button(edit_note_window, text="Редактировать запись", command=lambda: edit_owners(license_number.get(),full_name.get(),sex.get(), dob.get(), place_of_registration.get(), item_id))
        edit_note_btn.place(x = 130, y = 395, width = 140, height = 22)

    owners_window = create_window("Владельцы авто", "850x400")
    top = Frame(owners_window)
    top.pack()
    owners_columns = ("license_number", "full_name", "sex","dob", "place_of_registration")
    owners_rows = take_rows("owner")
    owners_table = ttk.Treeview(owners_window, columns = owners_columns, show="headings")
    create_table(owners_columns, ["Номер вод. удостоверения", "ФИО", "Пол", "Дата рождения", "Адрес прописки"], owners_table, owners_rows)
    owners_table.column("#1", width=120)
    owners_table.column("#2", width=170)
    owners_table.column("#3", width=10)
    owners_table.column("#4", width=70)
    owners_table.column("#5", width=300)
    
    owners_table.bind("<<TreeviewSelect>>", item_selected)
    create_buttons_row(top, ["Добавить запись", "Редактировать запись", "Удалить запись"], [add_note_owners,  lambda: edit_note_owners(item_selected("<<TreeviewSelect>>")), lambda :del_selected_note_owners(item_selected("<<TreeviewSelect>>"))])