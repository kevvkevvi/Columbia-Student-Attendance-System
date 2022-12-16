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

    def get_by_key(self, key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        res = self.cur.execute(sql, args=key)
        result = self.cur.fetchone()

        return result

