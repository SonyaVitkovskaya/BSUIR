import pymysql
from config import * 

def delete_row(table_name, condition):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'DELETE FROM lab2.{table_name} WHERE {condition}; '
                cursor.execute(request)
                connection.commit()
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)

def take_max(table_name, column, condition=""):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'SELECT MAX({column}) FROM lab2.{table_name} {condition}'
                cursor.execute(request)
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)
    return cursor._rows[0][f"MAX({column})"]

def take_rows(table_name, column = "*", condition = ""):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'SELECT {column} FROM lab2.{table_name} {condition}'
                cursor.execute(request)
                data = cursor.fetchall()
                rows=[]
                for row in data: rows.append(tuple(row.values()))
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)
    return rows

def insert_note(table_name, values):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'INSERT INTO lab2.{table_name} VALUES {values}'
                cursor.execute(request)
                connection.commit()
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)

def count(table_name, condition):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'SELECT COUNT(*) FROM lab2.{table_name} WHERE {condition} '
                cursor.execute(request)
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)
    return cursor._rows[0]["COUNT(*)"]


def task1(date1, date2):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'SELECT COUNT(*) FROM lab2.inspection_history WHERE date BETWEEN "{date1}" AND "{date2}"'
                cursor.execute(request)
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)
    return cursor._rows[0]["COUNT(*)"]

def task2(date):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'SELECT traffic_police_officer.full_name, inspection_history.license_number, traffic_police_officer.job_title\
                      FROM lab2.inspection_history JOIN  lab2.traffic_police_officer ON inspection_history.officer_id = traffic_police_officer.id  WHERE date="{date}" ORDER BY traffic_police_officer.full_name'
                cursor.execute(request)
                data = cursor.fetchall()
                rows = []
                for row in data: rows.append(tuple(row.values()))
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)
    return rows

def task3(engine_number):
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name, cursorclass = pymysql.cursors.DictCursor)
        print("connected")
        try:
            with connection.cursor() as cursor: 
                request = f'SELECT inspection_history.date, inspection_history.result FROM  lab2.inspection_history  JOIN  lab2.auto ON inspection_history.license_plate_number = auto.license_plate_number  WHERE engine_number="{engine_number}"'
                cursor.execute(request)
                data = cursor.fetchall()
                rows = []
                for row in data: rows.append(tuple(row.values()))
        finally: connection.close()
    except Exception as ex: print("connection refused", ex)
    return rows













