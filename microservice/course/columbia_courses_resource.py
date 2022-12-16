import pymysql

import os


class ColumbiaCoursesResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_section_by_key(key):

        sql = "SELECT * FROM courses.sections where call_no=%s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_section_by_name(name):

        sql = "SELECT * FROM courses.sections where course_name=%s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=name)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_enrollments_by_no(no):

        sql = "SELECT * FROM courses.enrollments where call_no=%s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=no)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_enrollments_by_uni(uni):

        sql = "SELECT * FROM courses.enrollments where uni=%s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        result = cur.fetchall()

        return result

    @staticmethod
    def add_section(call_no, course_name, enrollment_number):

        sql = "insert into courses.sections (call_no, course_name, enrollment_number) \
        values (%s, %s, %s)";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(call_no, course_name, enrollment_number))

        return res

    @staticmethod
    def update_section_name(call_no, course_name):

        sql = "update courses.sections set course_name = %s \
              where call_no = %s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(course_name, call_no))

        return res

    @staticmethod
    def delete_section(call_no):

        sql = "delete from courses.sections where call_no=%s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=call_no)
        res = cur.rowcount # number of affected rows

        return res

    @staticmethod
    def add_enrollment(call_no, uni):

        sql = "insert into courses.enrollments (call_no, uni) \
        values (%s, %s)";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(call_no, uni)) # number of affected rows
        # if insert successfully, update enrollment_number
        if res:
            sql1 = "update courses.sections set enrollment_number = enrollment_number + 1";
            res1 = cur.execute(sql1)

        return res

    @staticmethod
    def delete_enrollment(call_no, uni):

        sql = "delete from courses.enrollments where call_no=%s and uni=%s";
        conn = ColumbiaCoursesResource._get_connection()
        cur = conn.cursor()
        cur.execute(sql, args=(call_no, uni))
        res = cur.rowcount
        # if delete successfully, update enrollment_number
        if res:
            sql1 = "update courses.sections set enrollment_number = enrollment_number - 1";
            res1 = cur.execute(sql1)

        return res




