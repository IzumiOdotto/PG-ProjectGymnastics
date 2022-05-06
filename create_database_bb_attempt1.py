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