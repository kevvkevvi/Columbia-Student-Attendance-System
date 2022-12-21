/*
 Create table statement.
 */
create database attend;

use attend;

DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS attendances;

CREATE TABLE students
(
    uni     varchar(6) primary key,
    first_name varchar(128) not null,
    last_name varchar(128) not null,
    email varchar(128) not null
);

CREATE TABLE sections
(
    call_no     varchar(128) primary key,
    course_name varchar(128) not null,
    enrollment_num int not null
);

CREATE TABLE enrollments
(
    call_no     varchar(128) not null,
    uni     varchar(128) not null,
    primary key (call_no, uni),
    FOREIGN KEY(call_no) REFERENCES sections(call_no) on delete cascade,
    FOREIGN KEY(uni) REFERENCES students(uni) on delete cascade
);

CREATE TABLE classes(
    call_no VARCHAR(128) not null,
    date DATE not null,
    attendance_num INT,
    PRIMARY KEY (call_no, date),
    FOREIGN KEY (call_no) REFERENCES sections(call_no) on delete cascade
);

CREATE TABLE attendances(
    uni varchar(128) not null,
    call_no varchar(128) not null,
    date DATE,
    PRIMARY KEY (uni, call_no, date),
    FOREIGN KEY(uni) REFERENCES students(uni) on delete cascade,
    FOREIGN KEY (call_no, date) REFERENCES classes(call_no, date) on delete cascade
);






/*
 Example insert statement. Note that since auto_id is auto-increment, the insert
 statement does not need to specify it.
 */
INSERT INTO `sections` VALUES ('COMS4119', 'Computer Networks', 100);
INSERT INTO `sections` VALUES ('COMS6156', 'Cloud Computing', 400);


INSERT INTO `students` VALUES ('hr2543', 'h', 'r', 'hr2543@columbia.edu');
INSERT INTO `students` VALUES ('hw2910', 'Huifeng', 'Wu', 'hw2910@columbia.edu');
INSERT INTO `students` VALUES ('yg2233', 'g', 'y', 'yg2233@columbia.edu');
INSERT INTO `students` VALUES ('yx2744', 'yaolun', 'xiao', 'yx2744@columbia.edu');

INSERT INTO `classes` VALUES ('COMS4119', '1997-02-13', 80);
INSERT INTO `classes` VALUES ('COMS6156', '2022-12-02', 90);

INSERT INTO `enrollments` VALUES ('COMS6156', 'hr2543');
INSERT INTO `enrollments` VALUES ('COMS4119', 'yg2233');

INSERT INTO `attendances` VALUES ('yg2233', 'COMS6156', '2022-12-02');

