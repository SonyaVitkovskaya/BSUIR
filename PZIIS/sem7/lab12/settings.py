import psycopg2

def setup_access_control():
    try:
        # Подключение к PostgreSQL под суперпользователем
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="yourpassword")
        conn.autocommit = True
        cursor = conn.cursor()

        # Создание базы данных
        cursor.execute("CREATE DATABASE testdb;")
        print("Database 'testdb' created.")

        # Создание ролей
        cursor.execute("CREATE ROLE admin WITH LOGIN PASSWORD 'adminpassword';")
        cursor.execute("GRANT ALL PRIVILEGES ON DATABASE testdb TO admin;")
        print("Role 'admin' created with full privileges.")

        cursor.execute("CREATE ROLE user WITH LOGIN PASSWORD 'userpassword';")
        cursor.execute("GRANT CONNECT ON DATABASE testdb TO user;")
        cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO user;")
        print("Role 'user' created with partial privileges.")

        cursor.execute("CREATE ROLE guest WITH LOGIN PASSWORD 'guestpassword';")
        cursor.execute("GRANT CONNECT ON DATABASE testdb TO guest;")
        cursor.execute("GRANT SELECT ON ALL TABLES IN SCHEMA public TO guest;")
        print("Role 'guest' created with read-only privileges.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error during access control setup: {e}")

# Пример вызова
setup_access_control()
