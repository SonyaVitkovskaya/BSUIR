from abc import ABC, abstractmethod
from data import User_storage, Post_storage, Regular_user, Post
import json
import datetime

#добавить лайки, дизлайки

class User_controller_int(ABC):
    @abstractmethod
    def __init__(self, users_file): pass

    @abstractmethod
    def save_users(self):pass

    @abstractmethod
    def get_everybody(self): pass 
         
    @abstractmethod
    def get_users(self): pass

    @abstractmethod
    def get_admins(self): pass

    @abstractmethod
    def add_user(self, name,  email, password): pass

    @abstractmethod
    def get_user(self, id): pass

    @abstractmethod
    def is_admin(self, user): pass
        
class User_controller(User_controller_int):
    def __init__(self, users_file):
        self.file = users_file
        self.__user_storage = User_storage(users_file)

    def __del__(self):
        self.save_users()

    def save_users(self):
        users = {"admins":[], "regular_users":[]}
        for admin in self.get_admins():
            users["admins"].append({"id":admin.get_id(), "email": admin.get_email(), "password": admin.get_password(), "first_name": admin.get_first_name(), "second_name": admin.get_second_name()})
        for user in self.get_users():
            users["regular_users"].append({"id":user.get_id(), "email": user.get_email(), "password": user.get_password(), "first_name": user.get_first_name(), "second_name": user.get_second_name()})
    
        with open(self.file, 'w') as f:
            json.dump(users, f, indent=2)

    def get_everybody(self): return self.__user_storage.get_everybody() 
         
    def get_users(self): 
        return [user for user in self.__user_storage.get_everybody() if user.get_admin_status()==False]

    def get_admins(self): 
        return [user for user in self.__user_storage.get_everybody() if user.get_admin_status()==True]

    def add_user(self, name,  email, password):
        second_name, first_name = name.split(" ")
        all_users = self.get_everybody()
        max_id = 0
        for user in all_users: 
            if user.get_id() > max_id:  max_id = user.get_id()      
        new_user = Regular_user(max_id+1, email, password, first_name, second_name)
        self.__user_storage.add_user(new_user)
        return new_user.get_id()

    def get_user(self, id): return self.__user_storage.get_user(id)

    def is_admin(self, user): return user.get_admin_status() 

    def check(self, email, password):
        for user in self.__user_storage.get_everybody():
            if user.get_email()==email and user.get_password()==password: return user.get_id()
        return -1


class Post_controller_int(ABC):
    @abstractmethod
    def __init__(self, posts_file): pass

    @abstractmethod
    def save_posts(self):pass

    @abstractmethod
    def get_posts(self): pass

    @abstractmethod
    def add_post(self, name, content): pass

    @abstractmethod
    def delete_post(self, id): pass

    @abstractmethod
    def get_post(self, id): pass

class Post_controller(Post_controller_int):
    def __init__(self, posts_file):
        self.posts_file = posts_file
        self.__post_storage = Post_storage(posts_file)

    def __del__(self):
        self.save_posts()

    def save_posts(self):
        posts = {"posts":[]}
        for post in self.get_posts():
            posts["posts"].append({"id":post.get_id(), "name": post.get_name(), "content": post.get_content(), "comments": post.get_comments(), "date": post.get_date()})
        with open(self.posts_file, 'w') as f:
            json.dump(posts, f, indent=2)

    def get_posts(self): return self.__post_storage.get_posts() 

    def add_post(self, name, content):
        all_posts = self.get_posts()
        max_id = 0
        for post in all_posts: 
            if post.get_id() > max_id:  max_id = post.get_id()
        date = str(datetime.datetime.today()).split(" ")[0]
        new_post = Post(max_id+1, name, content, date)
        self.__post_storage.add_post(new_post)
        return new_post.get_id()

    def get_post(self, id): return self.__post_storage.get_post(id)

    def delete_post(self, id): self.__post_storage.delete_post(self.get_post(id))

class Main_controller():
    def __init__(self, users_file, posts_file):
        self.user_controller = User_controller(users_file)
        self.posts_controller = Post_controller(posts_file)

