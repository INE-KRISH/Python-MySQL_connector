import numpy as np
import pandas as pd
titanicdata = pd.read_csv('D:/Coding/python/datasets/Titanic survival/train.csv', index_col=False, delimiter = ',')
df = pd.DataFrame(titanicdata)
df['Cabin'] = df['Cabin'].replace(np.nan, '-')
df['Age'] = df['Age'].replace(np.nan, '-')
df['Embarked'] = df['Embarked'].replace(np.nan, '-')





print(df)



import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', database='titanic',user='root', password='123456')#give ur username, password
    cur=conn.cursor()
    cur.execute("CREATE TABLE passenger_data(PassengerId varchar(255), Survived varchar(255), Pclass varchar(255), Name varchar(255), Sex varchar(255), Age varchar(255), SibSp varchar(255), Parch varchar(255), Ticket varchar(255), Fare varchar(255), Cabin varchar(255), Embarked varchar(255))")
    print("Table is created....")
    
   
        #loop through the data frame
    for i,row in df.iterrows():
        cur=conn.cursor()    
        #here %S means string values 
        sql = "INSERT INTO titanic.passenger_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, tuple(row))
        print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
        conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)