# School-DMS
Yet another school data management system

# Installation:
1. Install Mariadb from mariadb.org
2. run `CREATE USER 'admin'@'localhost IDENTIFIED BY '12345678';`
3. run `GRANT ALL PRIVILEGES ON *.*  TO 'admin'@'localhost';`
4. run `CREATE DATABASE sdb_db;`
5. run `python manage.py make migrations` and `python manage.py migrate`
6. At last, run `python manage.py runserver`
7. If you want to access admin panel, create superuser by `python manage.py createsuperuser`

# How-to-run:
1. cd into main folder
2. run `python manage.py runserver`
3. Veiw the rendered page at localhost:8000

# Requirements:
1. Python 3.7+
2. MariaDB
3. Django
4. Pandas
5. Openpyxl

# Implemented:
1. Bus management

# Roadmap:
1. User login and logout(Teachers and students)
2. Staff management
3. Time Table allocation
4. Attendence
5. Fee management

# Screenshot:
![](https://github.com/STRTSNM/School-DMS/blob/main/scrnsht.png)
![](https://github.com/STRTSNM/School-DMS/blob/main/scrnsht1.png)
![](https://github.com/STRTSNM/School-DMS/blob/main/scrnsht2.png)
![](https://github.com/STRTSNM/School-DMS/blob/main/scrnsht3.png)


   
