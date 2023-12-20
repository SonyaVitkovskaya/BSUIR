from tkinter import *
from tkinter import ttk
from requests import take_max, insert_note, take_rows, delete_row, task1, task2, task3
from checks import *
from tkinter.messagebox import showerror, showwarning, showinfo
from funcs import *
from auto_w_controllers import auto_wind
from owners_w_controllers import owners_wind
from off_w_controllers import officers_wind
import datetime
from datetime import timedelta

def insert_in_history(date, off_id, auto, result, id):
    err_string = ""
    if date_check(date) == '': err_string += "Некорректный ввод даты\n"
    if id_check(off_id) == 0: err_string += "Отсутствует сотрудник с данным ID\n"
    if reg_license_plate_number(auto) == '': err_string += "Отсутствует авто с введенным госномером\n"
    if  result == '': err_string+="Не выбран результат техосмотра"
    if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
    else: 
        if check_off_work(int(off_id), date) == 1: 
            license = take_rows("auto", "owner_license", f"WHERE license_plate_number = '{auto}'")[0][0]
            insert_note("inspection_history", f"('{id}', '{date}', {int(off_id)}, '{license}', '{auto}', '{result}')")
            history_table.insert("", END, values=take_rows("inspection_history", condition= f"WHERE id = {id}")[0])
        else: showerror(title="Ошибка", message="Сотрудник уже провел 10 осмотров")

main_window = create_window('История техосмотров в учреждении ГИБДД', '800x600')
top = Frame(main_window)
bot = Frame(main_window)
bot2 = Frame(main_window)
top.pack()
bot.pack()
bot2.pack()

history_columns = ("id", "date", "officer_id", "license_number", "lisence_plate_number", "result")
history_rows = take_rows("inspection_history")
history_table = ttk.Treeview(columns = history_columns, show="headings")
create_table(history_columns, ["№", "Дата", "ID сотрудника", "Водительское удостоверение", "Рег. номер авто", "Результат"], history_table, history_rows)
history_table.column("#1", width=35)
history_table.column("#2", width=120)
history_table.column("#3", width=90)
history_table.column("#5", width=150)

def item_selected(event):
    return history_table.selection()[0]
history_table.bind("<<TreeviewSelect>>", item_selected)

def add_note_history():
    add_note_window = create_window("Добавление записи о техосмотре", "400x400")
    fr1, entry_date = create_frame_with_entry("Введите дату в формате ГГГГ-ММ-ДД", add_note_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr2, entry_off = create_frame_with_entry_and_button("Введите ID сотрудника", add_note_window, officers_wind, "Таблица сотрудников")
    fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr3, entry_auto = create_frame_with_entry_and_button("Введите регистрационный номера авто", add_note_window, auto_wind, "Таблица авто")
    fr3.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr4 = create_frame("Выберите результат техосмотра", add_note_window)
    selected_result = StringVar(fr4)
    rb1 = ttk.Radiobutton(fr4, text="соответствует", value="соответствует", variable=selected_result)
    rb2 = ttk.Radiobutton(fr4, text="не соответствует", value="не соответствует", variable=selected_result)
    rb1.pack(anchor=NW)
    rb2.pack(anchor=NW)
    fr4.pack(anchor=NW, fill=X, padx=5, pady=5)
    id = take_max("inspection_history", "id")+1
    add_note_btn = ttk.Button(add_note_window, text="Внести запись", command=lambda: insert_in_history(entry_date.get(),entry_off.get(),entry_auto.get(),selected_result.get(), id))
    add_note_btn.place(x = 130, y = 365, width = 140, height = 22)

def del_selected_note_history(item_id):
    id = history_table.item(item_id)["values"][0]
    history_table.delete(item_id)
    delete_row("inspection_history", f"id={id}")

def edit_history(date, off_id, auto, result,item_id):
    id = history_table.item(item_id)["values"][0]
    history_table.delete(item_id)
    delete_row("inspection_history", f"id={id}")
    insert_in_history(date, off_id, auto, result, id)

def edit_note_history(item_id):
    edit_note_window = create_window("Редактирование записи о техосмотре", "400x400")
    fr1, entry_date = create_frame_with_entry("Введите дату в формате ГГГГ-ММ-ДД", edit_note_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr2, entry_off = create_frame_with_entry_and_button("Введите ID сотрудника", edit_note_window, officers_wind, "Таблица сотрудников")
    fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr3, entry_auto = create_frame_with_entry_and_button("Введите регистрационный номера авто", edit_note_window, auto_wind, "Таблица авто")
    fr3.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr4 = create_frame("Выберите результат техосмотра", edit_note_window)
    selected_result = StringVar(fr4)
    rb1 = ttk.Radiobutton(fr4, text="соответствует", value="соответствует", variable=selected_result)
    rb2 = ttk.Radiobutton(fr4, text="не соответствует", value="не соответствует", variable=selected_result)
    rb1.pack(anchor=NW)
    rb2.pack(anchor=NW)
    fr4.pack(anchor=NW, fill=X, padx=5, pady=5)
    edit_note_btn = ttk.Button(edit_note_window, text="Редактировать запись", command= lambda: edit_history(entry_date.get(),entry_off.get(),entry_auto.get(), selected_result.get(), item_id))
    edit_note_btn.place(x = 130, y = 365, width = 140, height = 22)

create_buttons_row(top, ["Добавить запись", "Редактировать запись", "Удалить запись"], [add_note_history,lambda:  edit_note_history(item_selected("<<TreeviewSelect>>")), lambda: del_selected_note_history(item_selected("<<TreeviewSelect>>"))])
create_buttons_row(bot, ["Таблица сотрудников", "Таблица авто", "Таблица владельцев"], [officers_wind, auto_wind, owners_wind])


def count_a(date1, date2):
    err_string = ""
    if date_check(date1) == '': err_string += "Некорректный ввод начальной даты\n"
    if date_check(date2) == '': err_string += "Некорректный ввод конечной даты\n"
    if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
    else:
        count_res = f"{task1(date1, date2)} авто прошли техосмотр в указанный период\n"
        from_date = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
        to_date = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
        by_date = ""
        while from_date <= to_date:
            str = count("inspection_history", f"date = '{from_date}'")
            by_date += f"{str} - {from_date}\n" if str>0 else ""
            from_date = from_date + timedelta(days=1) 
        showinfo(title = "Результат подсчета", message = count_res+by_date)
    
def count_date_auto(): 
    count_window = create_window("Расчет количество автомобилей, прошедших техосмотр за заданный промежуток времени", "400x200")
    fr1, entry_date1 = create_frame_with_entry("Введите начальную дату в формате ГГГГ-ММ-ДД", count_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr2, entry_date2 = create_frame_with_entry("Введите конечную дату в формате ГГГГ-ММ-ДД", count_window)
    fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
    add_note_btn = ttk.Button(count_window, text="Посчитать", command=lambda: count_a(entry_date1.get(),entry_date2.get()))
    add_note_btn.place(x = 130, y = 150, width = 140, height = 22)

def date_off_a(date):
    err_string = ""
    if date_check(date) == '': err_string += "Некорректный ввод даты\n"
    if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
    else:
        res_wind = create_window("Список сотрудников", "800x400")
        rows = task2(date)
        columns = ("full_name", "license_number", "job_title")
        retable = ttk.Treeview(res_wind, columns = columns, show="headings")
        create_table(columns, ["Имя", "Авто", "Должность"], retable, rows)
        retable.column("#1", width=90)
        retable.column("#2", width=25)
        retable.column("#3", width=200)

def date_off():
    count_window = create_window("Список сотрудников ГАИ, проводивших осмотр на заданную дату", "400x100")
    fr1, entry_date = create_frame_with_entry("Введите дату в формате ГГГГ-ММ-ДД", count_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    add_note_btn = ttk.Button(count_window, text="Получить список", command=lambda: date_off_a(entry_date.get()))
    add_note_btn.place(x = 130, y = 70, width = 140, height = 22)

def auto_history_a(engine_number):
    err_string = ""
    if not_reg_engine_number(engine_number) == '': err_string += "Двигаетль не зарегистрирован\n"
    if len(err_string)!=0: showerror(title="Ошибка", message=err_string)
    else:
        res_wind = create_window("История авто", "600x400")
        rows = task3(engine_number)
        columns = ("date", "result")
        retable = ttk.Treeview(res_wind, columns = columns, show="headings")
        create_table(columns, ["Дата", "Результат"], retable, rows)

def auto_history():
    count_window = create_window("Список сотрудников ГАИ, проводивших осмотр на заданную дату", "400x140")
    fr1, engine_number = create_frame_with_entry_and_button("Введите номер двигателя", count_window, auto_wind,"Таблица авто")
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    add_note_btn = ttk.Button(count_window, text="Получить историю", command=lambda: auto_history_a(engine_number.get()))
    add_note_btn.place(x = 130, y = 110, width = 140, height = 22)

create_buttons_row(bot2, ["Расчет авто по дате","Список сотрудников по дате","История конкретного авто"], [count_date_auto, date_off, auto_history])

main_window.mainloop()
