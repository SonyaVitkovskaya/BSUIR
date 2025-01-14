import subprocess

def uninstall_postgresql():
    try:
        print("Stopping PostgreSQL...")
        subprocess.run(["sudo", "systemctl", "stop", "postgresql"], check=True)

        print("Removing PostgreSQL...")
        subprocess.run(["sudo", "apt", "remove", "--purge", "postgresql", "-y"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/lib/postgresql/"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/etc/postgresql/"], check=True)

        print("PostgreSQL removed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during uninstallation: {e}")

# Пример вызова
uninstall_postgresql()
