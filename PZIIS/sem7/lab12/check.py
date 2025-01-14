
import subprocess


def test_access(role, password, query):
    try:
        conn = psycopg2.connect(dbname="testdb", user=role, password=password)
        cursor = conn.cursor()
        cursor.execute(query)

        if cursor.description:
            print(f"Query results for {role}:")
            for row in cursor.fetchall():
                print(row)
        else:
            print(f"Query executed successfully for {role}.")
        
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error for role {role}: {e}")

# Пример тестов
test_access("guest", "guestpassword", "SELECT * FROM your_table;")
test_access("user", "userpassword", "INSERT INTO your_table (column) VALUES ('test');")
test_access("admin", "adminpassword", "DROP TABLE your_table;")
