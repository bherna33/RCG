CREATE TABLE Employee(
    person_id int PRIMARY KEY NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email_address varchar(100) NOT NULL,
    hire_date date NOT NULL,
    job_title varchar(100) NOT NULL,
    agency_num int,
    registration_date date NOT NULL
);