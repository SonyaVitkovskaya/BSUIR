# Установка NGINX
sudo apt update
sudo apt install nginx -y

# Создание тестовой страницы
echo "<!DOCTYPE html><html><head><title>Test Page</title></head><body><h1>It works!</h1></body></html>" | sudo tee /var/www/html/index.html

# Запуск и проверка статуса
sudo systemctl start nginx
sudo systemctl enable nginx

# Настройка брандмауэра для доступа
sudo ufw allow 'Nginx Full'

# Проверка доступности страницы
curl http://<IP-адрес-сервера>


Этап 2. Настройка системы журналирования
Для журналирования веб-сервера и других подсистем:

Убедитесь, что логи NGINX пишутся в /var/log/nginx/access.log и /var/log/nginx/error.log.
Для SSH-журналирования используйте /var/log/auth.log (на Ubuntu) или /var/log/secure (на CentOS).
Можно использовать системные инструменты, такие как syslog или journald, для централизованного сбора логов.
Дополнительно можно настроить лог-агрегатор вроде ELK Stack (Elasticsearch + Logstash + Kibana) или Fluentd для анализа логов.


import re
from datetime import datetime

# Путь к лог-файлам
nginx_log = "/var/log/nginx/access.log"
ssh_log = "/var/log/auth.log"

def parse_nginx_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    for log in logs:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(\w+ .*?)" (\d+) (\d+|-)', log)
        if match:
            ip, date, request, status, size = match.groups()
            print(f"IP: {ip}, Date: {date}, Request: {request}, Status: {status}, Size: {size}")

def parse_ssh_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    for log in logs:
        if "Failed password" in log or "Accepted password" in log:
            print(log.strip())

print("NGINX Logs:")
parse_nginx_logs(nginx_log)

print("\nSSH Logs:")
parse_ssh_logs(ssh_log)









вариант1 

sudo apt update
sudo apt install apache2 -y

sudo nano /var/www/html/index.html


<html>
  <head><title>Test Page</title></head>
  <body><h1>Server is up and running!</h1></body>
</html>

curl http://localhost

sudo nano /etc/apache2/apache2.conf

Убедитесь, что логи включены. Логи ошибок и доступа сохраняются в файлах:
/var/log/apache2/error.log
/var/log/apache2/access.log

tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log
