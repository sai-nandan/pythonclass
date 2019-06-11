import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythonclass"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE pythonclass")

# dbs = mycursor.execute("SHOW DATABASES")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

mycursor.execute("SHOW TABLES")
count = 0
for x in mycursor:
  print(x[0])
  if(x[0]=="students_info"):
      count = count+1

if(count==0):
    mycursor.execute("CREATE TABLE students_info (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(30) NOT NULL, branch VARCHAR(30) NOT NULL, year TINYINT NOT NULL, PRIMARY KEY (id) )")


