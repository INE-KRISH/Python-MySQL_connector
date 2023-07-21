# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:09:25 2021

@author: admin
"""

#Write a program to retrieve speceifc data from mysql table
import mysql.connector as sqlcon
con=sqlcon.connect(host='localhost',user='root',password='1234', database='empl',charset='utf8')
mycur=con.cursor()
c=input('Name of Employee to searched  : ')
str1="Select * from empl_info where ename='"+c+"'"
mycur.execute(str1)
data=mycur.fetchall()
for r in data:
    print(r)

