# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:18:10 2021

@author: admin
"""

#Menu Driven program
import mysql.connector as sqlcon
def usermenu(): #Method/Function declaration
    x=1
    while(x):
        print('------MENU------ ')
        print('1. Add')
        print('2. Update ')
        print('3. Delete')
        print('4. Display')
        print('5. Search')
        print('6. Exit ')
        
        ch=int(input('Enter your choice   :   '))
        
        if ch==1:
            addData() #Method/Function Call
        elif ch==2:
            updData()
        elif ch==3:
            delData()
        elif ch==4:
            showData()
        elif ch==5:
            searchData()
        elif ch==6:
            print('Program aborted by user \nThanks for Using Menu Driven Application')
            break
        else:
            print('Please enter valid choice ')


def addData():
    conn=sqlcon.connect(host='localhost',user='root',password='1234',database='xia',charset='utf8')
    cur=conn.cursor()
    eno=int(input('Enter Employee No : '))
    ena=input('Enter Name of the Employee : ')
    job=input('Enter Job : ')
    mgrid=int(input('Enter Managaer ID : '))
    jdate=input('Enter date of Joining : ')
    sal=int(input('Enter Salary : '))
    com=int(input('Enter Commission : '))
    dpt=int(input('Enter Department No : '))
    coment=input('Enter comment if any : ')
    savedata="insert into empl values("+str(eno)+",'"+str(ena)+"','"+str(job)+"',"+str(mgrid)+",'"+str(jdate)+"',"+str(sal)+","+str(com)+","+str(dpt)+",'"+str(coment)+"')"
    cur.execute(savedata)
    conn.commit()
    print('Record Saved Successfuly')
    conn.close()


def updData():
    con=sqlcon.connect(host='localhost',user='root',password='1234',database='xia',charset='utf8')
    mycur=con.cursor()
    changedvalue=input('Enter new Job to be changed : ')
    criteria=input('Enter Employee Name : ')
    upd="update empl set job='"+changedvalue+"' where ename='"+criteria+"'"
    mycur.execute(upd)
    con.commit()
    print("Record Updated successfully ..........")
    con.close()
    
def delData():
    con=sqlcon.connect(host='localhost',user='root',password='1234',database='xia',charset='utf8')
    cr=con.cursor()
    eno=int(input('Enter the Employee number to be Delated : '))
    delete="delete from empl where empno="+str(eno)+""
    cr.execute(delete)
    con.commit()
    print('Data Deleted from the table permanently............')
    con.close()

def showData():
    mycon=sqlcon.connect(host='localhost',user='root',password='1234',database='xia',charset='utf8')
    cursor=mycon.cursor()
    s='select * from EMPL'
    cursor.execute(s)
    data=cursor.fetchall()
    for i in data:
        print(i)
        cursor.close()
    
def searchData():
    con=sqlcon.connect(host='localhost',user='root',password='1234', database='xia',charset='utf8')
    mycur=con.cursor()
    c=input('Name of Employee to searched  : ')
    str1="Select * from empl where ename='"+c+"'"
    mycur.execute(str1)
    data=mycur.fetchall()
    for r in data:
        print(r)

usermenu() # User define function call
    
        
    