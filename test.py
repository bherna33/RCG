import sqlite3
from datetime import date

connection = sqlite3.connect('test.db')


cur = connection.cursor()

cur.execute("CREATE TABLE Employee(person_id int PRIMARY KEY NOT NULL, first_name varchar(50) NOT NULL, last_name varchar(50) NOT NULL,email_address varchar(100) NOT NULL,hire_date date NOT NULL,job_title varchar(100) NOT NULL,agency_num int,registration_date date NOT NULL);")

cur.execute("INSERT INTO Employee (person_id, first_name, last_name, email_address, hire_date, job_title, agency_num, registration_date) VALUES(?,?,?,?,?,?,?,?)" , 
            ("11","ese","Is","cool", date.today(),  "Awsome", "4563",date.today() )
            )

connection.commit()
connection.close()