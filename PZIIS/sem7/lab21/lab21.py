import hashlib
import mysql.connector
from mysql.connector import Error
import argparse

def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="bb",
        password="Qw8pPruC!", 
        database="secure_system"
    )

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def handle_http_request(method, endpoint, data=None):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        if endpoint == "/register":
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                           (data["username"], hash_password(data["password"])))
            conn.commit()
            return {"status": "success", "message": "User registered successfully."}

        elif endpoint == "/adduser":
            cursor.execute("INSERT INTO users (username, password_hash, access_level) VALUES (%s, %s, %s)",
                           (data["username"], hash_password(data["password"]), data["access_level"]))
            conn.commit()
            return {"status": "success", "message": "User added successfully."}

        elif endpoint == "/login":
            cursor.execute("SELECT * FROM users WHERE username = %s", (data["username"],))
            user = cursor.fetchone()
            if user and user["password_hash"] == hash_password(data["password"]):
                return {"status": "success", "message": "Login successful.", "user": user}
            else:
                return {"status": "error", "message": "Invalid username or password."}

        elif endpoint == "/addinfo":
            cursor.execute("INSERT INTO information (data, confidentiality_level) VALUES (%s, %s)",
                           (data["data"], data["confidentiality_level"]))
            conn.commit()
            return {"status": "success", "message": "Information added successfully."}

        elif endpoint == "/editinfo":
            cursor.execute("UPDATE information SET data = %s, confidentiality_level = %s WHERE id = %s",
                           (data["data"], data["confidentiality_level"], data["id"]))
            conn.commit()
            return {"status": "success", "message": "Information updated successfully."}

        elif endpoint == "/deleteinfo":
            cursor.execute("DELETE FROM information WHERE id = %s", (data["id"],))
            conn.commit()
            return {"status": "success", "message": "Information deleted successfully."}

        elif endpoint == "/searchinfo":
            cursor.execute("SELECT * FROM information WHERE confidentiality_level <= %s",
                           (data["user"]["access_level"],))
            info = cursor.fetchall()
            return {"status": "success", "data": info}

        elif endpoint == "/updateuser":
            cursor.execute("UPDATE users SET access_level = %s WHERE username = %s",
                           (data["access_level"], data["username"]))
            conn.commit()
            return {"status": "success", "message": "User access level updated successfully."}

        elif endpoint == "/logout":
            return {"status": "success", "message": "Logout successful."}

        else:
            return {"status": "error", "message": "Endpoint not found."}

    except Error as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()
        conn.close()

def main():
    parser = argparse.ArgumentParser(description="Secure System CLI")
    parser.add_argument("command", help="Command to execute")
    parser.add_argument("-n", "--name", help="Username")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-f", "--flag", type=int, help="Access level flag (0 or 1)")
    parser.add_argument("-d", "--data", help="Information data")
    parser.add_argument("-l", "--level", type=int, help="Confidentiality level")
    parser.add_argument("-i", "--id", type=int, help="Information ID")
    args = parser.parse_args()

    if args.command == "register":
        response = handle_http_request("POST", "/register", {"username": args.name, "password": args.password})

    elif args.command == "adduser":
        response = handle_http_request("POST", "/adduser",
                                       {"username": args.name, "password": args.password, "access_level": args.flag})

    elif args.command == "login":
        response = handle_http_request("POST", "/login", {"username": args.name, "password": args.password})

    elif args.command == "addinfo":
        response = handle_http_request("POST", "/addinfo",
                                       {"data": args.data, "confidentiality_level": args.level})

    elif args.command == "editinfo":
        response = handle_http_request("PUT", "/editinfo",
                                       {"id": args.id, "data": args.data, "confidentiality_level": args.level})

    elif args.command == "deleteinfo":
        response = handle_http_request("DELETE", "/deleteinfo", {"id": args.id})

    elif args.command == "searchinfo":
        response = handle_http_request("GET", "/searchinfo", {"user": {"access_level": args.flag}})

    elif args.command == "updateuser":
        response = handle_http_request("PUT", "/updateuser",
                                       {"username": args.name, "access_level": args.flag})

    elif args.command == "logout":
        response = handle_http_request("POST", "/logout", {})

    else:
        response = {"status": "error", "message": "Command not recognized."}

    print(response)


if __name__ == "__main__":
    main()
