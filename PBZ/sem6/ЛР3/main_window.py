from tkinter import *
from tkinter import ttk
from requests import db_request, check_exeption, dbb
from funcs import *

main_window = create_window('Структура книжного треккера', '800x600')
top = Frame(main_window)
bot = Frame(main_window)
bot2 = Frame(main_window)
top.pack()
bot.pack()
bot2.pack()
is_activ = ""
active_table = ttk.Treeview(columns=["", ""], show="headings")

def item_selected(event):
    return active_table.selection()[0]

active_table.bind("<<TreeviewSelect>>", item_selected)

def add_class():
    add_window = create_window("Добавление класса", "400x280")
    fr1, entry1 = create_frame_with_entry("Введите название класса", add_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr2, entry2 = create_frame_with_entry("Введите ID экземпляра", add_window)
    fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr3 = create_frame("Добавить", add_window)
    selected_result = StringVar(fr3)
    rb1 = ttk.Radiobutton(fr3, text="только этому экземпляру", value = 0, variable=selected_result)
    rb2 = ttk.Radiobutton(fr3, text="всем экзеплярам", value = 1, variable=selected_result)
    rb1.pack(anchor=NW)
    rb2.pack(anchor=NW)
    fr3.pack(anchor=NW, fill=X, padx=5, pady=5)

    def insert(label, id, everyone):
        if (everyone =="1"): check_exeption(f"Match (b), (p) where id(b) = {int(id)} and labels(p) = labels(b) set p:{label}")
        else: db_request(f"Match (b) where id(b) = {int(id)} set p:{label}")
        show_class()
        add_window.destroy()

    add_btn = ttk.Button(add_window, text="Добавить класс", command=lambda: insert(entry1.get(),entry2.get(), selected_result.get()))
    add_btn.place(x = 130, y = 243, width = 140, height = 25)

def add_relation():
    add_window = create_window("Добавление отношения", "400x260")
    fr1, entry1 = create_frame_with_entry("Введите ID первого экземпляра", add_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr2, entry2 = create_frame_with_entry("Введите ID второго экземпляра", add_window)
    fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr3, entry3 = create_frame_with_entry("Введите отношение", add_window)
    fr3.pack(anchor=NW, fill=X, padx=5, pady=5)

    def insert(id1, id2, relation):
        check_exeption(f"Match (b), (p) where id(b) = {int(id1)} and id(p) = {int(id2)} create (b)-[:{relation}]->(p)")
        show_relation()
        add_window.destroy()

    add_btn = ttk.Button(add_window, text="Добавить отношение", command=lambda: insert(entry1.get(), entry2.get(), entry3.get()))
    add_btn.place(x = 130, y = 223, width = 140, height = 25)

def add_instance():
    add_window = create_window("Добавление сущности", "400x280")
    fr1, entry1 = create_frame_with_entry("Введите имя сущности", add_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr2, entry2 = create_frame_with_entry("Введите класс", add_window)
    fr2.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr3, entry3 = create_frame_with_entry("Введите свойство-значение", add_window)
    fr3.pack(anchor=NW, fill=X, padx=5, pady=5)

    def insert(name, classes, properties):
        properties = properties.split(", ")
        prop = ""
        for property in properties:
            if (property):
                property = property.split("=")
                prop += f", {property[0]}: '{property[1]}'"
        classes = classes.split()
        req = f"create (p:{':'.join(classes)} {{name: '{name}' {prop}}})"
        check_exeption(req)
        show_instance()
        add_window.destroy()

    add_btn = ttk.Button(add_window, text="Добавить сущность", command=lambda: insert(entry1.get(), entry2.get(), entry3.get()))
    add_btn.place(x = 130, y = 245, width = 140, height = 25)

def add():
    global is_activ
    if is_activ == "class": add_class()
    elif is_activ == "relation": add_relation()
    elif is_activ == "instance": add_instance()

def edit_class(item_id):
    name = active_table.item(item_id)["values"][0]
    edit_window = create_window("Редактирование класса", "400x100")
    fr1, entry1 = create_frame_with_entry("Введите новое название", edit_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    def set_new_name(new_name, name):
        check_exeption(f"match (n: {name}) set n:{new_name} remove n:{name}")
        show_class()
        edit_window.destroy()
    edit_btn = ttk.Button(edit_window, text="Редактировать класс", command = lambda: set_new_name(entry1.get(), name))
    edit_btn.place(x = 130, y = 69, width = 140, height = 22)

def edit_relation(item_id):
    quest_edit_window = create_window("Вопросик", "400x150")
    fr1 = create_frame("Поменять:", quest_edit_window)
    selected_result = StringVar(fr1)
    rb1 = ttk.Radiobutton(fr1, text="Первую сущность", value = 1, variable=selected_result)
    rb2 = ttk.Radiobutton(fr1, text="Вторую сущность", value = 2, variable=selected_result)
    rb3 = ttk.Radiobutton(fr1, text="Отношение", value = 0, variable=selected_result)
    rb1.pack(anchor=NW)
    rb2.pack(anchor=NW)
    rb3.pack(anchor=NW)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)

    def choose(choice, item_id):
        quest_edit_window.destroy()
        window = create_window("Редактирование", "400x100")
        fr1, entry1 = create_frame_with_entry("Введите новое наименование", window)
        fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
        def ps(data, item_id, choice):
            window.destroy()
            name1 = active_table.item(item_id)["values"][0]
            relation = active_table.item(item_id)["values"][1]
            name2 = active_table.item(item_id)["values"][2]
            if choice == '1': check_exeption(f"match (p)-[r:{relation}]->(b), (c) where p.name = '{name1}' and b.name = '{name2}' and c.name = '{data}' delete r\n create (c)-[:{relation}]->(b)")
            if choice == '2': check_exeption(f"match (p)-[r:{relation}]->(b), (c) where p.name = '{name1}' and b.name = '{name2}' and c.name = '{data}' delete r\n create (c)<-[:{relation}]->(p)")
            if choice == '0': check_exeption(f"match (p)-[r:{relation}]->(b) where p.name = '{name1}'and b.name = '{name2}' delete r\n create (p)-[:{data}]->(b)")
            show_relation()

        edit_btn = ttk.Button(window, text="Ввести", command = lambda: ps(entry1.get(), item_id, choice))
        edit_btn.place(x = 130, y = 69, width = 140, height = 22)
    
    ch_btn = ttk.Button(quest_edit_window, text="Выбрать", command = lambda: choose(selected_result.get(), item_id))
    ch_btn.place(x = 130, y = 115, width = 140, height = 22)

def edit_instance(item_id):
    save = [0,0]   

    def saving(who): 
        nonlocal save
        if who == "name": save[0]=1
        if who == "properties": save[1]=1

    edit_window = create_window("Редактирование сущности", "400x280")
    fr1, entry1 = create_frame_with_entry_and_button("Введите имя сущности", edit_window, lambda: saving("name"), "Оставить")
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    fr3, entry3 = create_frame_with_entry_and_button("Введите свойство-значение", edit_window, lambda: saving("properties"), "Оставить")
    fr3.pack(anchor=NW, fill=X, padx=5, pady=5)

    def edit_inst(name, properties):
        nonlocal save, item_id
        id = active_table.item(item_id)["values"][0]
        if not save[0]: check_exeption(f"match (p) where id(p) = {id} set p.name = '{name}' ")
        if not save[1]:
            properties = properties.split(", ")
            prop = f"match (p) where id(p) = {id} set"
            for property in properties:
                if(property):
                    property = property.split("=")
                    prop += f" p.{property[0]} = '{property[1]}',"
            check_exeption(prop[:-1])
        edit_window.destroy()
        show_instance()
     
    ch_btn = ttk.Button(edit_window, text="Изменить", command = lambda: edit_inst(entry1.get(), entry3.get()))
    ch_btn.place(x = 100, y = 245, width = 240, height = 22)

def edit(item_id): 
    global is_activ
    if is_activ == "class": edit_class(item_id)
    elif is_activ == "relation": edit_relation(item_id)
    elif is_activ == "instance": edit_instance(item_id)

def delete_class(item_id):
    quest_edit_window = create_window("Вопросик", "400x150")
    fr1 = create_frame("Удалить:", quest_edit_window)
    selected_result = StringVar(fr1)
    rb1 = ttk.Radiobutton(fr1, text="Все ноды", value = 1, variable=selected_result)
    rb2 = ttk.Radiobutton(fr1, text="Только лейбл", value = 0, variable=selected_result)
    rb1.pack(anchor=NW)
    rb2.pack(anchor=NW)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    def choose(choice):
        nonlocal item_id
        name = active_table.item(item_id)["values"][0]
        if choice == "1": check_exeption(f"match (n: {name}) detach delete n")
        else: check_exeption(f"match (n: {name}) remove n:{name}")
        quest_edit_window.destroy()
        show_class()

    ch_btn = ttk.Button(quest_edit_window, text="Выбрать", command = lambda: choose(selected_result.get()))
    ch_btn.place(x = 130, y = 115, width = 140, height = 22)

def delete_relation(item_id):
    name1 = active_table.item(item_id)["values"][0]
    relation = active_table.item(item_id)["values"][1]
    name2 = active_table.item(item_id)["values"][2]
    check_exeption(f"match (p)-[r:{relation}]->(b) where p.name = '{name1}'and b.name = '{name2}' delete r")
    show_relation()

def delete_instance(item_id):
    id = active_table.item(item_id)["values"][0]
    check_exeption(f"match (a) where id(a) = {id} detach delete a")
    show_instance()

def delete(item_id):
    global is_activ
    if is_activ == "class": delete_class(item_id)
    elif is_activ == "relation": delete_relation(item_id)
    elif is_activ == "instance": delete_instance(item_id)

def change_status(btns):
    for btn in btns:
        print(btn["state"])
        if btn["state"] == "disabled": 
            btn["state"] = "normal"

edit_btns = create_buttons_row(bot, ["Добавить запись", "Редактировать запись", "Удалить запись"], [add, lambda:  edit(item_selected("<<TreeviewSelect>>")), lambda: delete(item_selected("<<TreeviewSelect>>"))], "disabled")

def show_class(btns = edit_btns):
    global is_activ
    is_activ = "class"
    change_status(btns)
    class_columns = ("class_name", "amount_of_instances")
    class_rows = db_request('match (p) return distinct labels(p)')
    set_classes = set()
    for row in class_rows: set_classes.update([class_ for class_ in row[0]])
    table_rows = [[class_, db_request(f"match (p:{class_}) return count(p)")[0][0]]for class_ in set_classes]
    class_table = ttk.Treeview(columns=class_columns, show="headings")
    create_table(class_columns, ["Название класса", "Количество экземпляров"], class_table, table_rows)
    global active_table
    old_table = active_table
    active_table = class_table
    old_table.destroy()

def show_relation(btns = edit_btns):
    global is_activ
    is_activ = "relation"
    change_status(btns)
    relation_rows = db_request('match (p)-[r:%]->(n) return p.name,  type(r), n.name')
    relation_columns = ("1_inst", "relation", "2_inst")
    relation_table = ttk.Treeview(columns=relation_columns, show="headings")
    create_table(relation_columns, ["Первая сущность", "Отношение", "Вторая сущность"], relation_table, relation_rows)
    global active_table
    old_table = active_table
    active_table = relation_table
    old_table.destroy()

def show_instance(btns = edit_btns):
    global is_activ
    is_activ = "instance"
    change_status(btns)
    instance_rows = db_request('match (p) return id(p), p.name, properties(p)')
    instance_columns = ("id", "instance", "properties")
    instance_table = ttk.Treeview(columns=instance_columns, show="headings")
    create_table(instance_columns, ["ID", "Сущность", "Свойства"], instance_table, instance_rows)
    instance_table.column("#1", width=10)
    instance_table.column("#2", width=150)
    instance_table.column("#3", width=300)
    global active_table
    old_table = active_table
    active_table = instance_table
    old_table.destroy()

def show_query():
    from tkinter.scrolledtext import ScrolledText

    q_window = create_window("", "600x380")
    fr1 = create_frame("Составьте запрос на Cypher", q_window)
    fr1.pack(anchor=NW, fill=X, padx=5, pady=5)
    st = ScrolledText(fr1, width=50,  height=10)
    st.pack(fill=BOTH, side=LEFT, expand=True)

    fr2 = ttk.Frame(q_window)
    fr2.pack()
    table = ttk.Treeview(q_window, columns=["", ""], show="headings")

    def get_text(st):
        request = st.get("1.0", "end")
        rows = db_request(request)
        column_names = request.split("return ")[1].split(", ")
        nonlocal table
        table.destroy()
        table = ttk.Treeview(q_window, columns=column_names, show="headings")
        create_table(column_names, column_names, table, rows)

    add_btn = ttk.Button(fr1, text="query", command=lambda: get_text(st))
    add_btn.pack(side=BOTTOM)

    







create_buttons_row(top, ["Классы", "Отношения", "Экземпляры"], [lambda: show_class(edit_btns), lambda: show_relation(edit_btns), lambda: show_instance(edit_btns)], "normal")
req_btn = ttk.Button(bot2, text="Запросы", command=show_query, width=42).pack(anchor=N)
main_window.mainloop()
