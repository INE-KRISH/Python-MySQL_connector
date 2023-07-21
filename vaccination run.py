import mysql.connector as sqlcon
def usermenu():
    while(1):
        print('..........menu..........')
        print('1 : register yourself')
        print('2 : get appointment')
        print('3 : get your vaccination certificate')
        print('4 : show registered people')
        print('5 : people with appointment')
        print('6 : number of people vaccinated')
        print('7 : exit')
        ch=int(input('enter your interest: '))
        if ch== 1:
            reg()
        elif ch==2:
            app()
        elif ch==3:
            vacc()
        elif ch==4:
            shreg()
        elif ch==5:
            shapp()
        elif ch==6:
            shvacc()
        elif ch==7:
            print('thanks for visiting, visit again')
            break
        else:
            print('enter valid choice :)')
            
            
def reg():
     conn=sqlcon.connect(host='localhost',user='root',password='1234',database='vaccination',charset='utf8')
     cur=conn.cursor()
     aadno = input('Enter your aadhar number :')
     name = input('ENTER YOUR NAME:')
     dob = input('ENTER YOUR DATE OF BIRTH(YYYY-MM-DD):')
     local = input('ENTER YOUR AREA NAME:')
     savedata="insert into registration("+aadno+",'"+name+"','"+dob+"','"+local+"')"
     cur.execute(savedata)
     conn.commit()
     print('Record Saved Successfuly')
     conn.close()
     
def app():
     conn=sqlcon.connect(host='localhost',user='root',password='1234',database='vaccination',charset='utf8')
     cur=conn.cursor()
     aid=int(input('enter your appointment id:'))
     vaccine_name= input('ENTER VACCINE YOU WANT:')
     local=input('Enter area where you want to take vaccine:')
     savedata="insert into APPOINTMENT('"+str(aid)+"','"+vaccine_name+"','"+local+"','"++"')"      
     cur.execute(savedata)
     conn.commit()
     print('Record Saved Successfuly')
     conn.close()
    
     
     

def vacc():
     conn=sqlcon.connect(host='localhost',user='root',password='1234',database='vaccination',charset='utf8')
     cur=conn.cursor()
     
     savedata="insert into CERTIFICATE("++",'"++"','"++"','"++"')"
     cur.execute(savedata)
     conn.commit()
     print('Record Saved Successfuly')
     conn.close()
     
    


def shreg():
     conn=sqlcon.connect(host='localhost',user='root',password='1234',database='vaccination',charset='utf8')
     cursor=conn.cursor()
     s='select * from REGISTRATION'
     cursor.execute(s)
     data=cursor.fetchall()
     for i in data:
         print(i)
         cursor.close()
     
     



def shapp():
     conn=sqlcon.connect(host='localhost',user='root',password='1234',database='vaccination',charset='utf8')
     cursor=conn.cursor()
     s='select * from APPOINTMENT'
     cursor.execute(s)
     data=cursor.fetchall()
     for i in data:
         print(i)
         cursor.close()
     
 


def shvacc(): 
     conn=sqlcon.connect(host='localhost',user='root',password='1234',database='vaccination',charset='utf8')
     cursor=conn.cursor()
     s='select * from CERTIFICATE'
     cursor.execute(s)
     data=cursor.fetchall()
     for i in data:
         print(i)
         cursor.close()

usermenu()   
            
            