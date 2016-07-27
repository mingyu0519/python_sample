# coding=utf-8
import mysql.connector
# 添加数据库操作

class mysql_conn():
    def __init__(self,user,password,database):
        self.user = user
        self.password = password
        self.database = database

    def select(self,sql):
        try:
            conn = mysql.connector.connect(user=self.user,password=self.password,database=self.database,use_unicode=True)
            cursor = conn.cursor()
            cursor.execute(sql)
            values = cursor.fetchall()
        except Exception as e:
            print e
        finally:
            cursor.close()
            conn.close()
        return values
