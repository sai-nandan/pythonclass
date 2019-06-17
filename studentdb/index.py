import mysql.connector as mysql

mydb = mysql.connect(host="localhost",user="root",passwd="",database="college",port=3307)
mycursor = mydb.cursor()

####### Insertion process  #######
def insertStudentData(name,branch,year,phone):
    print(name,branch,year,phone)
    val = (name,branch,year,phone)
    mycursor.execute("INSERT INTO student_info (name,branch,year,phone) VALUES (%s,%s,%s,%s)",val)
    # val = [('Teja1','CSE',4,9999999999),('Teja2','ECE',4,9999999999),('Teja3','EEE',4,9999999999)]
    # mycursor.executemany("INSERT INTO student_info (name,branch,year,phone) VALUES (%s,%s,%s,%s)",val)
    mydb.commit()

####### Get data from database ######
def getAllStudentData():
    mycursor.execute("SELECT * FROM student_info")
    result = mycursor.fetchall()
    for rows in result:
        print(rows)

####### Get search data from database ######
def searchStudentData(branch):
    mycursor.execute("SELECT * FROM student_info WHERE branch=%s",branch)
    result = mycursor.fetchall()
    for rows in result:
        print(rows)

####### Update data in database ######
def updateStudentData():
    mycursor.execute("UPDATE student_info SET phone=8888888888 WHERE id=2")
    mydb.commit()

###### Delete row from database ######
def deleteStudentData():
    mycursor.execute("DELETE FROM student_info where id = 1")
    mydb.commit()

i = input("Enter Options : ")
if(i=="i"):
    name = input("Enter Name : ")
    branch = input("Enter Branch : ")
    year = input("Enter year : ")
    phone = input("Enter phone : ")
    insertStudentData(name,branch,year,phone)
elif(i=="sh"):
    getAllStudentData()
elif(i=="se"):
    branch = input("Enter Branch")
    searchStudentData(branch)
else:
    print("Select something dude!")
