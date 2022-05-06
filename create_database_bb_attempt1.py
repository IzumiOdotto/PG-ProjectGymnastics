# -*- coding = uft-8 -*-
# @File     : create_database_bb_attempt1.py
# @Time     : 2022/5/6 14:30  
# @Author   : Samuel HONG
# @Description : create database py_sqlite3_bb_attempt1 and connect to it
# @Version  :


import os
import sqlite3

if os.path.exists('database'):
    pass
else:
    os.makedirs('database')

#     连接数据库，如果文件不存在，自动创建文件
db = sqlite3.connect('database/py_sqlite3_bb_attempt1.db')

create_sql = '''
#     CREATE TABLE "Elements" (
#         "id" TEXT NOT NULL,
#         "NAME" TEXT NOT NULL,
#         "GROUP" INTEGER NOT NULL DEFAULT 18,
#         PRIMARY KEY("id" AUTOINCREMENT)
# );
# '''
#
# db.execute(create_sql)

#CREATE TABLE "ELEMENTS_TABLE_BB"
# (
#     "id"                TEXT    NOT NULL,
#     "ELEMENT_NUMBER"    TEXT    NOT NULL   UNIQUE,
#     "ELEMENT_NAME"      TEXT    NOT NULL,
#     "ELEMENT_GROUP"     INTEGER    NOT NULL CHECK ( ELEMENT_GROUP >= 1 AND ELEMENT_GROUP <= 6 ),
#     "ELEMENT_DIFFICULTY"    CHAR(1)    NOT NULL CHECK ( ELEMENT_DIFFICULTY == 'A''B''C''D''E''F''G''H''I'),
#     "ELEMENT_DIFFICULTY-CALCULATION"    REAL NOT NULL CHECK ( "ELEMENT_DIFFICULTY-CALCULATION" % 0.1 == 0 AND "ELEMENT_DIFFICULTY-CALCULATION" < 1),
#     PRIMARY KEY ("id" AUTOINCREMENT)
# );