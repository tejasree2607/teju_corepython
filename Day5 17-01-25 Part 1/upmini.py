import mysql.connector as c
mydb=c.connect(
    host='localhost',
    user='root',
    password='root',
    database='coe'
)
mycursor=mydb.cursor()
sql="UPDATE mini SET address = 'hyd' WHERE name = 'mom'"
mycursor.execute(sql)
mydb.commit()



