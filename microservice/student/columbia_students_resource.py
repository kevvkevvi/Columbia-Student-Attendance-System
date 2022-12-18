import pymysql

import os


class ColumbiaStudentsResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "kentwhf"
        pw = "Wuhuifeng1007!"
        h = "awseb-e-g6gye3m3t8-stack-awsebrdsdatabase-0z9z4mepwpq3.cilqzt8nihgc.us-east-2.rds.amazonaws.com"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_student_by_key(key):
        sql = "SELECT * FROM students.students where UNI=%s";
        conn = ColumbiaStudentsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def add_student(UNI, first_name, last_name, email):

        sql = "insert into students.students (UNI, first_name, last_name, email) \
        values (%s, %s, %s, %s)";
        conn = ColumbiaStudentsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(UNI, first_name, last_name, email))

        return res