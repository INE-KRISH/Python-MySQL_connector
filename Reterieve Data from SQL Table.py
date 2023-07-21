# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:00:02 2021

@author: admin
"""

import mysql.connector as sqlcon
mycon=sqlcon.connect(host='localhost',user='root',password='123456',database='employee',charset='utf8')
cursor=mycon.cursor()
s='select * from empl_info'
cursor.execute(s)
data=cursor.fetchall()
for i in data:
    print(i)
cursor.close()
 