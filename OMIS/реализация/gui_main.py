from tkinter import *
from tkinter import ttk
import datetime
from datetime import timedelta
from funcs import *
from logic import *


class ViewController():
    def __init__(self):
        self.main_window = self.create_window("Платформа управления блогами", '400x300')
        self.main_controller = Main_controller("all_users.json", "posts.json")
        self.widgets = []
        self.user_id = -1

    def create_window(self, text, size):
        window = Tk()
        window.title(text)
        window.geometry(size)
        return window

    def destroy(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

    def create_post(self, post_table):
        add_post_window = create_window("Добавление поста", "400x400")
        fr1, entry_name = create_frame_with_entry("Введите название", add_post_window)
        fr1.pack(anchor=N)
        fr2, entry_content = create_frame_with_entry("Введите содержание", add_post_window)
        fr2.pack(anchor=N)

        def on_close():
            new_post = self.main_controller.posts_controller.get_post(self.main_controller.posts_controller.add_post(entry_name.get(), entry_content.get()))
            post_table.insert("", END, values=(new_post.get_id(), new_post.get_name(), new_post.get_date()))
            add_post_window.destroy()
            
        add_post_btn = ttk.Button(add_post_window, text="Внести запись", command= on_close)
        add_post_btn.pack(anchor=N)

    def authorization(self):
        label = ttk.Label(self.main_window, text="АВТОРИЗАЦИЯ")
        label.pack(anchor=N)
        fr1, entry_email = create_frame_with_entry("Введите email", self.main_window)
        fr1.pack(anchor=N, fill=X, padx=5, pady=5)
        fr2, entry_password = create_frame_with_entry("Введите пароль", self.main_window)
        fr2.pack(anchor=N, fill=X, padx=5, pady=5)

        def check():
            self.user_id = self.main_controller.user_controller.check(entry_email.get(),entry_password.get())
            self.destroy()
            if  self.user_id != -1:
                if self.main_controller.user_controller.is_admin(self.main_controller.user_controller.get_user(self.user_id)):
                    self.admin_menu()
                else:
                    self.user_menu()
            else: 
                self.registration()

        auth_btn = ttk.Button(self.main_window, text = "Авторизоваться", command = check, width=20)
        auth_btn.pack(anchor=N)
        self.widgets += [fr1, fr2, label, auth_btn]

    def registration(self):
        label = ttk.Label(self.main_window, text="РЕГИСТРАЦИЯ")
        label.pack(anchor=N)
        fr1, entry_email = create_frame_with_entry("Введите email", self.main_window)
        fr1.pack(anchor=N, fill=X, padx=5, pady=5)
        fr2, entry_password = create_frame_with_entry("Введите пароль", self.main_window)
        fr2.pack(anchor=N, fill=X, padx=5, pady=5)
        fr3, entry_name = create_frame_with_entry("Введите фамилию и имя", self.main_window)
        fr3.pack(anchor=N, fill=X, padx=5, pady=5)

        def add():
            self.user_id = self.main_controller.user_controller.add_user(entry_name.get(), entry_email.get(), entry_password.get())
            self.destroy()
            self.user_menu()

        auth_btn = ttk.Button(self.main_window, text = "Зарегистрироваться", command = add, width=20)
        auth_btn.pack(anchor=N)
        self.widgets += [fr1, fr2, fr3, label, auth_btn]

    def repass(self):
        repass_wind = create_window("Смена пароля", "200x150")
        label = ttk.Label(repass_wind, text=f"Текущий пароль: {self.main_controller.user_controller.get_user(self.user_id).get_password()}")
        label.pack(anchor=NW)
        fr2, entry_password = create_frame_with_entry("Введите пароль", repass_wind)
        fr2.pack(anchor=N, fill=X, padx=5, pady=5)
        def on_close():
            self.main_controller.user_controller.get_user(self.user_id).set_password(entry_password.get())
            repass_wind.destroy()
        auth_btn = ttk.Button(repass_wind, text = "Сменить", command = on_close, width=20)
        auth_btn.pack(anchor=N)

    def see_post_user(self, item, posts_table): 
        id = posts_table.item(item)["values"][0]
        post_wind = create_window("Пост", "500x400")
        post = self.main_controller.posts_controller.get_post(id)
        label1 = ttk.Label(post_wind, text=f"{post.get_name()}")
        label1.pack(anchor=N)
        label2 = ttk.Label(post_wind, text=f"{post.get_content()}")
        label2.pack(anchor=NW)

        coms_col = ("name","comments")
        rows = []
        for comment in post.get_comments():
            rows.append((self.main_controller.user_controller.get_user(comment[0]).get_first_name(), comment[1]))
        coms_table = ttk.Treeview(post_wind, columns = coms_col, show="headings")
        create_table(coms_col, ["Имя", "Комментарии"], coms_table, rows)
   
        def on_close():
            post.add_comment([self.user_id, entry.get()])
            coms_table.insert("", END, values=(self.main_controller.user_controller.get_user(self.user_id).get_first_name(), entry.get()))

        entry = ttk.Entry(post_wind, width=30)
        entry.pack(anchor=NW, side = LEFT)
        auth_btn = ttk.Button(post_wind, text = "Добавить комментарий", command = on_close, width=30)
        auth_btn.pack(anchor=NW, side=LEFT)

    def user_menu(self):
        post_col = ("id", "name","date")
        rows =[]
        for post in self.main_controller.posts_controller.get_posts():
            rows.append((post.get_id(), post.get_name(),post.get_date()))
        posts_table = ttk.Treeview(columns = post_col, show="headings")
        create_table(post_col, ["№", "Название", "Дата"], posts_table, rows)
        posts_table.column("#1", width=10)
        posts_table.column("#2", width=150)
        posts_table.column("#3", width=20)

        def item_selected(event):
            return posts_table.selection()[0]
        posts_table.bind("<<TreeviewSelect>>", item_selected)

        btn1 = ttk.Button(self.main_window, text = "Поменять пароль", command = lambda: self.repass(), width=30)
        btn1.pack(anchor=N, side=LEFT)
        btn2 = ttk.Button(self.main_window, text = "Выбрать пост", command = lambda: self.see_post_user(item_selected("<<TreeviewSelect>>"), posts_table), width=32)
        btn2.pack(anchor=N, side=LEFT)

    def see_post_admin(self, item, posts_table): 
        id = posts_table.item(item)["values"][0]
        post_wind = create_window("Пост", "500x400")
        post = self.main_controller.posts_controller.get_post(id)
        label1 = ttk.Label(post_wind, text=f"{post.get_name()}")
        label1.pack(anchor=N)
        label2 = ttk.Label(post_wind, text=f"{post.get_content()}")
        label2.pack(anchor=NW)
        coms_col = ("name","comments")
        rows = []
        for comment in post.get_comments():
            rows.append((self.main_controller.user_controller.get_user(comment[0]).get_first_name(), comment[1]))
        coms_table = ttk.Treeview(post_wind, columns = coms_col, show="headings")
        create_table(coms_col, ["Имя", "Комментарии"], coms_table, rows)

        def item_selected(event):
            return coms_table.selection()[0]
        coms_table.bind("<<TreeviewSelect>>", item_selected)

        def del_selected_comm(item_id):
            id = coms_table.item(item_id)["values"][1]
            coms_table.delete(item_id)
            post.delete_comment(id)

        auth_btn = ttk.Button(post_wind, text = "Удалить комментарий", command = lambda: del_selected_comm(item_selected("<<TreeviewSelect>>")), width=30)
        auth_btn.pack(anchor=N)

    def admin_menu(self):
        post_col = ("id", "name","date")
        rows =[]
        for post in self.main_controller.posts_controller.get_posts():
            rows.append((post.get_id(), post.get_name(),post.get_date()))
        posts_table = ttk.Treeview(columns = post_col, show="headings")
        create_table(post_col, ["№", "Название", "Дата"], posts_table, rows)
        posts_table.column("#1", width=10)
        posts_table.column("#2", width=150)
        posts_table.column("#3", width=20)

        def item_selected(event):
            return posts_table.selection()[0]
        posts_table.bind("<<TreeviewSelect>>", item_selected)

        def delete_post(item_id):
            id = posts_table.item(item_id)["values"][0]
            posts_table.delete(item_id)
            self.main_controller.posts_controller.delete_post(id)

        btn1 = ttk.Button(self.main_window, text = "Удалить пост", command = lambda: delete_post(item_selected("<<TreeviewSelect>>")), width=20)
        btn1.pack(anchor=N, side=LEFT)
        btn2 = ttk.Button(self.main_window, text = "Проверить пост", command = lambda: self.see_post_admin(item_selected("<<TreeviewSelect>>"), posts_table), width=20)
        btn2.pack(anchor=N, side=LEFT)
        btn3 = ttk.Button(self.main_window, text = "Создать пост", command = lambda: self.create_post(posts_table), width=20)
        btn3.pack(anchor=N, side=LEFT)

def main(): 
    obj = ViewController()
    main_window = obj.main_window
    obj.authorization()
    main_window.mainloop()

main()