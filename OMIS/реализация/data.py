from abc import ABC, abstractmethod
import json

class User(ABC):
    @abstractmethod
    def __init__(self, id:int, email:str, password:str, first_name:str, second_name:str):pass
       
    @abstractmethod
    def get_id(self): pass

    @abstractmethod
    def set_email(self, email): pass

    @abstractmethod
    def get_password(self): pass
    
    @abstractmethod
    def set_password(self, password):pass

    @abstractmethod
    def get_first_name(self): pass

    @abstractmethod
    def get_second_name(self): pass

    @abstractmethod
    def get_admin_status(self): pass
    
class Regular_user(User):
    def __init__(self, id, email, password, first_name, second_name):
        self.__id = id
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__second_name = second_name
        self.__admin_status = False

    def get_id(self): 
        return self.__id
    
    def get_email(self): 
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_password(self): 
        return self.__password
    
    def set_password(self, password):
        self.__password = password

    def get_first_name(self): 
        return self.__first_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_second_name(self): 
        return self.__second_name
    
    def set_second_name(self, second_name):
        self.__second_name = second_name

    def get_admin_status(self): return self.__admin_status

    def set_admin_status(self, status): self.__admin_status = status

class Admin(User):
    def __init__(self, id, email, password, first_name, second_name):
        self.__id = id
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__second_name = second_name
        self.__admin_status = True

    def get_id(self): 
        return self.__id
    
    def get_email(self): 
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_password(self): 
        return self.__password
    
    def set_password(self, password):
        self.__password = password

    def get_first_name(self): 
        return self.__first_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_second_name(self): 
        return self.__second_name
    
    def set_second_name(self, second_name):
        self.__second_name = second_name

    def get_admin_status(self): return self.__admin_status

    def set_admin_status(self, status): self.__admin_status = status

class Post_int(ABC):
    @abstractmethod
    def __init__(self, id:int, name:str, content:str, date: str):pass
       
    @abstractmethod
    def get_id(self): pass

    @abstractmethod
    def get_name(self): pass

    @abstractmethod
    def set_name(self, name): pass

    @abstractmethod
    def get_content(self): pass
    
    @abstractmethod
    def set_content(self, password):pass

    @abstractmethod
    def get_comments(self): pass
    
    @abstractmethod
    def get_date(self): pass

    @abstractmethod
    def set_date(self): pass
    
    @abstractmethod
    def get_likes(self): pass

    @abstractmethod
    def set_likes(self, likes): pass
 
class Post(Post_int):
    def __init__(self, id:int, name:str, content:str, date: str):
        self.__id = id
        self.__name = name
        self.__content = content
        self.__comments = []
        self.__date = date
        self.__likes = 0

    def get_id(self): return self.__id

    def get_name(self): return self.__name

    def set_name(self, name): self.__name = name

    def get_content(self): return self.__content
    
    def set_content(self, content): self.__content = content

    def get_comments(self): return self.__comments

    def add_comment(self, comment): self.__comments.append(comment)
    
    def get_date(self): return self.__date

    def set_date(self, date): self.__date = date

    def get_likes(self): return self.__likes

    def set_likes(self, likes): self.__likes = likes 

    def delete_comment(self, str): 
        for i in range(len(self.__comments)):
            if self.__comments[i][1]==str: 
                self.__comments.pop(i)
                break

class User_storage_int(ABC):
    @abstractmethod
    def __init__(self, users_file):pass

    @abstractmethod
    def get_everybody(self): pass 

    @abstractmethod
    def add_user(self, user): pass

    @abstractmethod
    def get_user(self, id): pass

class User_storage(User_storage_int):
    def __init__(self, users_file):
        self.__everybody = []  
        with open(users_file, encoding ="utf-8") as f:
            users = json.load(f)
        for admin in users["admins"]:
            self.__everybody.append(Admin(admin["id"], admin["email"], admin["password"], 
                                          admin["first_name"],admin["second_name"]))
        for user in users["regular_users"]:
            self.__everybody.append(Regular_user(user["id"], user["email"], user["password"], 
                                          user["first_name"],user["second_name"]))

    def get_everybody(self): return self.__everybody 

    def add_user(self, user):
        self.__everybody.append(user)

    def get_user(self, id):
        for user in self.__everybody: 
            if user.get_id() == id: return user 

class Post_storage_int(ABC):
    @abstractmethod
    def __init__(self, posts_file):pass
         
    @abstractmethod
    def get_posts(self): pass

    @abstractmethod
    def add_post(self, post): pass

    @abstractmethod
    def delete_post(self, post): pass

    @abstractmethod
    def get_post(self, id): pass

class Post_storage(Post_storage_int):
    def __init__(self, posts_file):
        self.__posts = [] 
        with open(posts_file, encoding ="utf-8") as f:
            posts = json.load(f)
        for post in posts["posts"]:
            post_to_add = Post(post["id"], post["name"], post["content"], post["date"])
            for comment in post["comments"]: post_to_add.add_comment(comment)
            self.__posts.append(post_to_add)

    def get_posts(self): return self.__posts 

    def add_post(self, post):
        self.__posts.append(post)

    def get_post(self, id):
        for post in self.__posts: 
            if post.get_id() == id: return post 

    def delete_post(self, post):
        self.__posts.remove(post)