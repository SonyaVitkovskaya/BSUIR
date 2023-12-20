from tkinter import *
from tkinter import ttk
from requests import take_max, insert_note, take_rows, delete_row
from checks import *
from tkinter.messagebox import showerror
from funcs import *
from owners_w_controllers import owners_wind 

def auto_wind():

    def item_selected(event):
        return auto_table.selection()[0]

    def insert_in_auto(license_plate_number, engine_number, car_brand, color, passport_number, owner_license):
        err_string = ""
        if lisence_plate_number_check(license_plate_number) == '': err_string += "Некорректный ввод госномера\n"
        if reg_engine_number(engine_number) == '': err_string += "Двигатель с таким номером уже зарегистрирован\n"
        if passport_number_check(passport_number) == '': err_string += "Некорректный ввод техпаспорта\n"
        if reg_owner_license(owner_license) == '': err_string += "Владелец не зарегистрирован\n"
        if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
        else:
            insert_note("auto", f"('{license_plate_number}', '{engine_number}', '{car_brand}', '{color}', '{passport_number}', '{owner_license}')")
            auto_table.insert("", END, values=take_rows("auto", condition= f"WHERE license_plate_number = '{license_plate_number}'")[0])
        
    def add_note_auto():
        add_note_window = create_window("Добавление записи об авто", "400x500")
        fr1, license_plate_number_entry = create_frame_with_entry("Введите регистрационный номер", add_note_window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr2, engine_number_entry = create_frame_with_entry("Введите номер двигателя", add_note_window)
        fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr3, car_brand_entry = create_frame_with_entry("Введите марку", add_note_window)
        fr3.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr4, color_entry = create_frame_with_entry("Введите цвет", add_note_window)
        fr4.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr5, passport_number_entry = create_frame_with_entry("Введите номер техпаспорта", add_note_window)
        fr5.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr6, owner_license_entry = create_frame_with_entry_and_button("Введите номер водительского удостоверения владельца", add_note_window, owners_wind, "Таблица владельцев")
        fr6.pack(anchor=NW, fill=X, padx=5, pady=5)

        add_note_btn = ttk.Button(add_note_window, text="Внести запись", command=lambda: insert_in_auto(license_plate_number_entry.get(),engine_number_entry.get(),car_brand_entry.get(), color_entry.get(), passport_number_entry.get(), owner_license_entry.get()))
        add_note_btn.place(x = 130, y = 465, width = 140, height = 22)

    def del_selected_note_auto(item_id):
        id = auto_table.item(item_id)["values"][0]
        auto_table.delete(item_id)
        delete_row("auto", f"license_plate_number='{id}'")

    def edit_auto(license_plate_number, engine_number, car_brand, color, passport_number, owner_license, item_id):
        id = auto_table.item(item_id)["values"][0]
        auto_table.delete(item_id)
        delete_row("inspection_history", f"id={id}")
        insert_in_auto(license_plate_number, engine_number, car_brand, color, passport_number, owner_license)

    def edit_note_auto(item_id):
        edit_note_window = create_window("Редактирование записи об авто", "400x500")
        fr1, license_plate_number_entry = create_frame_with_entry("Введите регистрационный номер", edit_note_window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr2, engine_number_entry = create_frame_with_entry("Введите номер двигателя", edit_note_window)
        fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr3, car_brand_entry = create_frame_with_entry("Введите марку", edit_note_window)
        fr3.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr4, color_entry = create_frame_with_entry("Введите цвет", edit_note_window)
        fr4.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr5, passport_number_entry = create_frame_with_entry("Введите номер техпаспорта", edit_note_window)
        fr5.pack(anchor=NW, fill=X, padx=5, pady=5)
        fr6, owner_license_entry = create_frame_with_entry_and_button("Введите номер водительского удостоверения владельца", edit_note_window, owners_wind, "Таблица владельцев")
        fr6.pack(anchor=NW, fill=X, padx=5, pady=5)

        edit_note_btn = ttk.Button(edit_note_window, text="Редактировать запись", command=lambda: edit_auto(license_plate_number_entry.get(),engine_number_entry.get(),car_brand_entry.get(), color_entry.get(), passport_number_entry.get(), owner_license_entry.get(), item_id))
        edit_note_btn.place(x = 130, y = 465, width = 140, height = 22)


    auto_window = create_window("Автомобили прошедшие техосмотр","800x400" )
    top = Frame(auto_window)
    
    top.pack()
    auto_columns = ("license_plate_number", "engine_number", "car_brand","color", "passport_number", "owner_license")
    auto_rows = take_rows("auto")
    auto_table = ttk.Treeview(auto_window, columns = auto_columns, show="headings")
    create_table(auto_columns, ["Регистр. номер", "Номер двигателя", "Марка", "Цвет", "Номер техпаспорта", "Вод. удостоверение владельца"], auto_table, auto_rows)
    auto_table.column("#1", width=90)
    auto_table.column("#2", width=120)
    auto_table.column("#3", width=100)
    auto_table.column("#4", width=100)
    auto_table.column("#5", width=120)
    
    auto_table.bind("<<TreeviewSelect>>", item_selected)

    create_buttons_row(top, ["Добавить запись", "Редактировать запись", "Удалить запись"], [add_note_auto,  lambda:  edit_note_auto(item_selected("<<TreeviewSelect>>")), lambda: del_selected_note_auto(item_selected("<<TreeviewSelect>>"))])