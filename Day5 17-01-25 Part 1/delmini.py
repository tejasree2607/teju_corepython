import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='coe'
)
mycursor=mydb.cursor()
sql="delete from mini WHERE name = 'akka'"
mycursor.execute(sql)
mydb.commit()



