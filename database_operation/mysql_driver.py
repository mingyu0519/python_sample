# coding=utf-8
import mysql.connector

conn = mysql.connector.connect(user='root',password='',database='test',use_unicode=True)

cursor = conn.cursor()

cursor.execute("insert into myclass values (9,'aimi',1,23)")

cursor.execute("select * from myclass")

values = cursor.fetchall()

for x in values:
	for i in x:
		print i,
	print ''
cursor.close()
conn.close()