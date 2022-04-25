# -*- coding = uft-8 -*-
# @File     : elements_db.py
# @Time     : 2022/4/24 10:17  
# @Author   : Samuel HONG
# @Description : insert elements to sql--learn how to use sql
# @Version  :
import os
import sqlite3

if os.path.exists('database'):
    pass
else:
    os.makedirs('database')

#     连接数据库，如果文件不存在，自动创建文件
db = sqlite3.connect('database/py-sqlite-inster-tips.db')

#   数据库创建的SQL语句：
# create_sql = '''
#     CREATE TABLE "Person" (
#         "id" INTEGER NOT NULL UNIQUE,
#         "name" TEXT NOT NULL,
#         "age" INTEGER NOT NULL DEFAULT 18,
#         PRIMARY KEY("id" AUTOINCREMENT)
# );
# '''
#
# db.execute(create_sql)

select_table_name_sql = 'SELECT name FROM sqlite_master WHERE type = "table";'

cursor = db.cursor()
cursor.execute(select_table_name_sql)
print(cursor.fetchall())

insert_sql = """INSERT INTO Person 
VALUES (1,'person1',20);"""

cursor.execute(insert_sql)

query_sql = 'SELECT * FROM Person;'
cursor.execute(query_sql)

print(cursor.fetchall())
