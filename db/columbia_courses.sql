/*
 Create table statement.
 */
create database if not exists courses;
use courses;
drop table if exists sections;
drop table if exists enrollments;
create table sections
(
    call_no     varchar(128) primary key,
    course_name varchar(128) not null,
    enrollment_number int not null
);
create table enrollments
(
    call_no     varchar(128) not null,
    uni     varchar(128) not null,
    primary key (call_no, uni),
    foreign key (call_no) references sections(call_no)
);



/*
 Example insert statement. Note that since auto_id is auto-increment, the insert
 statement does not need to specify it.
 */
 insert into sections (call_no, course_name, enrollment_number)
    values ("COMS6156","Cloud Computing","400");

 insert into enrollments (call_no, uni)
    values ("COMS6156","hr2543");

 insert into enrollments (call_no, uni)
    values ("COMS6156","hw2910");
