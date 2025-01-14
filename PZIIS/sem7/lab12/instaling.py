import subprocess

def install_postgresql():
    try:
        print("Installing PostgreSQL...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "postgresql", "-y"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "postgresql"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "postgresql"], check=True)
        print("PostgreSQL installed and started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

# Пример вызова
install_postgresql()

