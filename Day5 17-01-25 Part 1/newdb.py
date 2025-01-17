import mysql.connector as c

mydb = c.connect(
  host="localhost",
  user="root",
  password="root",
  database="coe"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mini (name, address) VALUES (%s, %s)"
val = [
  ('akka', 'hyd'),
  ('anna', 'aus'),
  ('bro', 'mlg'),
  ('atha', 'srpt'),
  ('mama', 'srpt'),
  ('pinni', 'nlg'),
  ('sis', 'nlg'),
  ('babai', 'nlg'),
  ('vadina', 'hyd'),
  ('bava', 'uk'),
]

mycursor.executemany(sql, val)

mydb.commit()
