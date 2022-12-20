################################################
#  Third MicroService
#  Attendance
#  sections(call_no, course_name, enrollment_number)
#  class(call_no, date, attendance)
#  students(UNI, call_no, date)
#  By Yipeng Geng, yg2913
################################
import pymysql
import os
usr = os.environ.get("DBUSER")
pw = os.environ.get("DBPW")
h = os.environ.get("DBHOST")
sma = "attendance"
class DBResource:
    def __init__(self, user=usr, password=pw, host=h, schema=sma):
        self.user = user
        self.password = password
        self.host = host
        self.schema = schema
        self.conn, self.cur = self.get_connection()

    def get_connection(self):
        conn = pymysql.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
            db=self.schema
        )
        cur = conn.cursor()
        return conn, cur

    def get_sections(self, dic):
        call_no = dic["call_no"] if "call_no" in dic else None
        course_name = dic["course_name"] if "course_name" in dic else None
        enrollment_number = dic["enrollment_number"] if "enrollment_number" in dic else None
        limit = dic["limit"] if "limit" in dic else None
        offset = dic["offset"] if "offset" in dic else None
        sql = "SELECT * FROM sections "
        if call_no or course_name or enrollment_number:
            sql += "where"
            if call_no:
                sql += " call_no='{}' and".format(call_no)
            if course_name:
                sql += " course_name='{}' and".format(course_name)
            if enrollment_number:
                sql += " enrollment_number={} and".format(enrollment_number)
            sql = sql[:-3]
        if limit:
            sql += " LIMIT {}".format(limit)
        if offset:
            sql += " OFFSET {}".format(offset)
        res = self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def get_classes(self, dic):
        call_no = dic["call_no"] if "call_no" in dic else None
        date = dic["date"] if "date" in dic else None
        attendance = dic["attendance"] if "attendance" in dic else None
        limit = dic["limit"] if "limit" in dic else None
        offset = dic["offset"] if "offset" in dic else None
        sql = "SELECT * FROM class"
        if call_no or date or attendance:
            sql += "where"
            if call_no:
                sql += " call_no='{}' and".format(call_no)
            if date:
                sql += " date='{}' and".format(date)
            if attendance:
                sql += " attendance={} and".format(attendance)
            sql = sql[:-3]
        if limit:
            sql += " LIMIT {}".format(limit)
        if offset:
            sql += " OFFSET {}".format(offset)
        res = self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def get_students(self, dic):
        call_no = dic["call_no"] if "call_no" in dic else None
        date = dic["date"] if "date" in dic else None
        uni = dic["uni"] if "uni" in dic else None
        limit = dic["limit"] if "limit" in dic else None
        offset = dic["offset"] if "offset" in dic else None
        sql = "SELECT * FROM students"
        if call_no or date or uni:
            sql += "where"
            if call_no:
                sql += " call_no='{}' and".format(call_no)
            if date:
                sql += " date='{}' and".format(date)
            if uni:
                sql += " uni={} and".format(uni)
            sql = sql[:-3]
        if limit:
            sql += " LIMIT {}".format(limit)
        if offset:
            sql += " OFFSET {}".format(offset)
        res = self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def get_section(self, key):
        sql = "SELECT * FROM sections where call_no=%s"
        res = self.cur.execute(sql, args=key)
        result = self.cur.fetchone()
        return result

    def get_section_attendances(self, key):
        sql = "SELECT * FROM class where call_no=%s"
        res = self.cur.execute(sql, args=key)
        result = self.cur.fetchall()
        return result
    
    def get_section_attendance(self, call_no, date):
        sql = "SELECT * FROM class where call_no=%s and date=%s"
        res = self.cur.execute(sql, args=(call_no, date))
        result = self.cur.fetchone()
        return result

    def get_section_class_students(self, call_no, date):
        sql = "SELECT * FROM students where call_no=%s and date=%s"
        res = self.cur.execute(sql, args=(call_no, date))
        result = self.cur.fetchone()
        return result

    def get_section_class_student(self, call_no, date, uni):
        sql = "SELECT * FROM students where call_no=%s and date=%s and UNI=%s"
        res = self.cur.execute(sql, args=(call_no, date, uni))
        result = self.cur.fetchone()
        return result
    
    def get_section_students(self, call_no):
        sql = "SELECT call_no, UNI, date FROM students NATURAL JOIN sections where call_no=%s"
        res = self.cur.execute(sql, args=(call_no))
        result = self.cur.fetchone()
        return result

    def get_section_student(self, call_no, uni):
        sql = "SELECT call_no, UNI, date FROM students NATURAL JOIN sections where call_no=%s and UNI=%s"
        res = self.cur.execute(sql, args=(call_no, uni))
        result = self.cur.fetchone()
        return result

    def add_section(self, call_no, course_name, enrollment_number):
        sql = "insert into sections (call_no, course_name, enrollment_number) values (%s, %s, %s)"
        res = self.cur.execute(sql, args=(call_no, course_name, enrollment_number))
        return res

    def add_class(self, call_no, date, attendance):
        sql = "insert into class (call_no, date, attendance) values (%s, %s, %s)"
        res = self.cur.execute(sql, args=(call_no, date, attendance))
        return res

    def add_student(self, uni, call_no, date, increase_attendance=True):
        sql = "insert into students (UNI, call_no, date) values (%s, %s, %s)"
        res = self.cur.execute(sql, args=(uni, call_no, date))
        print(res)
        if res and increase_attendance:
            sql = "update class set attendance = attendance + 1 where call_no=%s and date=%s"
            self.cur.execute(sql, args=(call_no, date))
            res = self.cur.rowcount
        return res

    def delete_section(self, call_no):
        sql = "delete from sections where call_no=%s"
        self.cur.execute(sql, args=(call_no))
        res = self.cur.rowcount  # number of affected rows
        return res

    def delete_class(self, call_no, date):
        sql = "delete from class where call_no=%s and date=%s"
        self.cur.execute(sql, args=(call_no, date))
        res = self.cur.rowcount  # number of affected rows
        return res

    def delete_student(self, uni, call_no, date, decrease_attendance=True):
        sql = "delete from students where UNI=%s and call_no=%s and date=%s"
        self.cur.execute(sql, args=(uni, call_no, date))
        res = self.cur.rowcount  # number of affected rows
        if res and decrease_attendance:
            sql = "update class set attendance = attendance - 1 where call_no=%s and date=%s"
            self.cur.execute(sql, args=(call_no, date))
            res = self.cur.rowcount
        return res

    def update_section_enrollment(self, call_no, enrollment):
        sql = "update sections set enrollment_number = %s where call_no = %s"
        res = self.cur.execute(sql, args=(enrollment, call_no))
        return res

    def update_section_name(self, call_no, course_name):
        sql = "update sections set course_name = %s where call_no = %s"
        res = self.cur.execute(sql, args=(course_name, call_no))
        return res

    def update_class_attendance(self, call_no, date, attendance):
        sql = "update class set attendance = %s where call_no = %s and date = %s"
        res = self.cur.execute(sql, args=(attendance, call_no, date))
        return res