/*
 Create table statement.
 */
create database if not exists students;
use students;

create table students
(
    UNI     varchar(6) primary key,
    first_name varchar(128) not null,
    last_name varchar(128) not null,
    email varchar(128) not null
);

/*
 Example insert statement. Note that since auto_id is auto-increment, the insert
 statement does not need to specify it.
 */
 insert into students (UNI, first_name, last_name, email)
    values ("hw2910","Huifeng","Wu", "hw2910@columbia.edu");

