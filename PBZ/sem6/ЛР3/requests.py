import pymysql
from neo4j import GraphDatabase
from tkinter.messagebox import showerror, showwarning, showinfo

uri="bolt://localhost:7687"
user = "neo4j"
password=""

driver = GraphDatabase.driver(uri, auth=(user, password))

def db_request(string):
    session = driver.session(database='neo4j')
    try:
        result = session.run(string)
        return [record.values() for record in result]
    except Exception:
        session.cancel()
        raise
    finally:
        session.close()

def check_exeption(str):
    try:
        db_request(str)
    except Exception as ex: showerror(title="Ошибка", message="Что-то пошло не так, проверьте данные")
