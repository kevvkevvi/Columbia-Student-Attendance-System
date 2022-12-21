import pymysql
# import os

# usr = os.environ.get("DBUSER")  # DBUSER
# pw = os.environ.get("DBPW")  # DBPW
# h = os.environ.get("DBHOST")  # DBHOST


usr = "kentwhf"
pw = "Wuhuifeng1007!"
h = "awseb-e-g6gye3m3t8-stack-awsebrdsdatabase-0z9z4mepwpq3.cilqzt8nihgc.us-east-2.rds.amazonaws.com"


sma = "attend"


class DbResource:

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
            # port=3306,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
            db=self.schema
        )
        cur = conn.cursor()
        return conn, cur

    # Student Create
    def add_student(self, uni, first_name, last_name, email):

        sql = "insert into students (uni, first_name, last_name, email) \
        values (%s, %s, %s, %s)";

        res = self.cur.execute(sql, args=(uni, first_name, last_name, email))

        return res

    #Student Read
    def get_student_by_key(self,key):
        # sql = "f22_databases.columbia_students where guid=%s";
        sql = "SELECT * FROM students where uni=%s";
        res = self.cur.execute(sql, args=key)
        result = self.cur.fetchone()

        return result

    # Student Update email by uni
    def update_student_email(self,uni, email):

        sql = "update students set email = %s \
              where uni = %s";

        res = self.cur.execute(sql, args=(email, uni))

        return res

    # Student Delete by uni
    def delete_student(self, key):
        sql = "delete from students where uni=%s"
        self.cur.execute(sql, args= key)
        res = self.cur.rowcount  # number of affected rows
        return res

    # def delete_student(self, uni, call_no, date, decrease_attendance=True):
    #     sql = "delete from students where uni=%s and call_no=%s and date=%s"
    #     self.cur.execute(sql, args=(uni, call_no, date))
    #     res = self.cur.rowcount  # number of affected rows
    #     if res and decrease_attendance:
    #         sql = "update class set attendance = attendance - 1 where call_no=%s and date=%s"
    #         self.cur.execute(sql, args=(call_no, date))
    #         res = self.cur.rowcount
    #     return res

    # Section Create
    def add_section(self,call_no, course_name, enrollment_num):

        sql = "insert into sections (call_no, course_name, enrollment_num) \
        values (%s, %s, %s)";

        res = self.cur.execute(sql, args=(call_no, course_name, enrollment_num))

        return res

    # Section Read All
    def get_sections(self, dic):
        call_no = dic["call_no"] if "call_no" in dic else None
        course_name = dic["course_name"] if "course_name" in dic else None
        enrollment_number = dic["enrollment_num"] if "enrollment_num" in dic else None
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

    # Section Read by key
    def get_section_by_key(self, key):
        sql = "SELECT * FROM sections where call_no=%s"
        res = self.cur.execute(sql, args=key)
        result = self.cur.fetchone()
        return result

    # Section Read by name
    def get_section_by_name(self,name):

        sql = "SELECT * FROM sections where course_name=%s";
        res = self.cur.execute(sql, args=name)
        result = self.cur.fetchall()
        return result

    # # Section Update name by call_no
    # def update_section_name(self,call_no, course_name):
    #
    #     sql = "update sections set course_name = %s \
    #           where call_no = %s";
    #
    #     res = self.cur.execute(sql, args=(course_name, call_no))
    #
    #     return res

    # Section Update enrollment_num by call_no
    def update_section(self, course_name, call_no, enrollment_num):
        sql = "update sections set course_name = %s and enrollment_num = %s where call_no = %s"
        res = self.cur.execute(sql, args=(course_name, enrollment_num, call_no))
        return res

    # Section Delete by call_no
    def delete_section(self,call_no):

        sql = "delete from attend.sections where call_no=%s";
        self.cur.execute(sql, args=call_no)
        res = self.cur.rowcount # number of affected rows

        return res

    # Class Create
    def add_class(self, call_no, date, attendance_num):
        sql = "insert into classes (call_no, date, attendance_num) values (%s, %s, %s)"
        res = self.cur.execute(sql, args=(call_no, date, attendance_num))
        return res

    # Class Read All
    def get_classes(self, dic):
        call_no = dic["call_no"] if "call_no" in dic else None
        date = dic["date"] if "date" in dic else None
        attendance_num = dic["attendance_num"] if "attendance_num" in dic else None
        limit = dic["limit"] if "limit" in dic else None
        offset = dic["offset"] if "offset" in dic else None
        sql = "SELECT * FROM classes"
        if call_no or date or attendance_num:
            sql += "where"
            if call_no:
                sql += " call_no='{}' and".format(call_no)
            if date:
                sql += " date='{}' and".format(date)
            if attendance_num:
                sql += " attendance_num={} and".format(attendance_num)
            sql = sql[:-3]
        if limit:
            sql += " LIMIT {}".format(limit)
        if offset:
            sql += " OFFSET {}".format(offset)
        res = self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    # Class Read by section
    def get_class_by_key(self, key):
        sql = "SELECT * FROM classes where call_no=%s"
        res = self.cur.execute(sql, args=key)
        result = self.cur.fetchall()
        return result

    # Class Read by call_no and date
    def get_one_class(self, call_no, date):
        sql = "SELECT * FROM classes where call_no=%s and date=%s"
        res = self.cur.execute(sql, args=(call_no, date))
        result = self.cur.fetchone()
        return result

    # Class Update attendance_num
    def update_class_num(self, call_no, date, attendance_num):
        sql = "update classes set attendance_num = %s where call_no = %s and date = %s"
        res = self.cur.execute(sql, args=(attendance_num, call_no, date))
        return res

    # Class Delete
    def delete_class(self, call_no, date):
        sql = "delete from classes where call_no=%s and date=%s"
        self.cur.execute(sql, args=(call_no, date))
        res = self.cur.rowcount  # number of affected rows
        return res


    # Enrollment Create
    def add_enrollment(self,call_no, uni):

        sql = "insert into enrollments (call_no, uni) \
        values (%s, %s)";

        res = self.cur.execute(sql, args=(call_no, uni)) # number of affected rows
        # if insert successfully, update enrollment_number
        if res:
            sql = "update sections set enrollment_num = enrollment_num + 1 where call_no=%s"
            res = self.cur.execute(sql, args=(call_no))

        return res

    # Enrollment Read by call_no/uni
    def get_enrollments_by_no(self,no):

        sql = "SELECT * FROM enrollments where call_no=%s";

        res = self.cur.execute(sql, args=no)
        result = self.cur.fetchall()

        return result

    # Enrollment Read by call_no/uni
    def get_enrollments_by_uni(self,uni):

        sql = "SELECT * FROM enrollments where uni=%s";

        res = self.cur.execute(sql, args=uni)
        result = self.cur.fetchall()

        return result


    # Enrollment Delete
    def delete_enrollment(self,call_no, uni):

        sql = "delete from enrollments where call_no=%s and uni=%s";

        self.cur.execute(sql, args=(call_no, uni))
        res = self.cur.rowcount
        # if delete successfully, update enrollment_number
        if res:
            sql = "update sections set enrollment_num = enrollment_num - 1 where call_no=%s"
            res = self.cur.execute(sql, args=(call_no))

        return res

    # Attendance Create
    def add_attendance(self, uni, call_no, date, increase_attendance=True):
        sql = "insert into attendances (uni, call_no, date) values (%s, %s, %s)"
        res = self.cur.execute(sql, args=(uni, call_no, date))
        print(res)

        if res and increase_attendance:
            sql = "update classes set attendance_num = attendance_num + 1 where call_no=%s and date=%s"
            self.cur.execute(sql, args=(call_no, date))
            res = self.cur.rowcount

        return res


    # Attendance Read All
    def get_attendances(self, dic):
        call_no = dic["call_no"] if "call_no" in dic else None
        date = dic["date"] if "date" in dic else None
        uni = dic["uni"] if "uni" in dic else None
        limit = dic["limit"] if "limit" in dic else None
        offset = dic["offset"] if "offset" in dic else None
        sql = "SELECT * FROM attendances"
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

    # Attendance Read by class
    def get_attendances_by_class (self, call_no, date):
        sql = "SELECT * FROM attendances where call_no=%s and date=%s"
        res = self.cur.execute(sql, args=(call_no, date))
        result = self.cur.fetchone()
        return result

    # Attendance Read by class and student
    def get_one_attendance (self, call_no, date, uni):
        sql = "SELECT * FROM attendances where call_no=%s and date=%s and uni=%s"
        res = self.cur.execute(sql, args=(call_no, date, uni))
        result = self.cur.fetchone()
        return result

    # Attendance Read by section
    def get_attendance_by_section (self, call_no):
        sql = "SELECT call_no, uni, date FROM attendances NATURAL JOIN sections where call_no=%s"
        res = self.cur.execute(sql, args=(call_no))
        result = self.cur.fetchone()
        return result

    # Attendance Read by section and student
    def get_attendances_section_student (self, call_no, uni):
        sql = "SELECT call_no, uni, date FROM attendances NATURAL JOIN sections where call_no=%s and uni=%s"
        res = self.cur.execute(sql, args=(call_no, uni))
        result = self.cur.fetchone()
        return result

    # Attendance Delete
    def delete_attendance(self, uni, call_no, date, decrease_attendance=True):
        sql = "delete from attendances where uni=%s and call_no=%s and date=%s"
        self.cur.execute(sql, args=(uni, call_no, date))
        res = self.cur.rowcount  # number of affected rows
        if res and decrease_attendance:
            sql = "update classes set attendance_num = attendance_num - 1 where call_no=%s and date=%s"
            self.cur.execute(sql, args=(call_no, date))
            res = self.cur.rowcount
        return res