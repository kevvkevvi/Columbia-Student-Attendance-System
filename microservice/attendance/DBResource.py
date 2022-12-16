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

    def get_sections(self):
        sql = "SELECT * FROM sections"
        res = self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def get_classes(self):
        sql = "SELECT * FROM class"
        res = self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def get_students(self):
        sql = "SELECT * FROM students"
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