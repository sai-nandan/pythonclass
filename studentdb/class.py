import mysql.connector as mysql

mydb = mysql.connect(host="localhost",user="root",passwd="",database="college",port=3307)
mycursor = mydb.cursor()

class StudentData:

    def __init__(self,a):
        print("Class working")
        name = "hello"
        print(name)
        self.age = a
    
    def showVariable(self):
        def f(a):
            def F(b):
                return b + 5
            return F
        return f(3)

    ####### Insertion process  #######
    def insertStudentData(self,name,branch,year,phone,email):
        print(name,branch,year,phone,email)
        val = (name,branch,year,phone,email)
        mycursor.execute("INSERT INTO student_info (name,branch,year,phone,email) VALUES (%s,%s,%s,%s,%s)",val)
        mydb.commit()

    ####### Get data from database ######
    def getAllStudentData(self):
        mycursor.execute("SELECT * FROM student_info")
        result = mycursor.fetchall()
        for rows in result:
            print(rows)

    ####### Get search data from database ######
    def searchStudentData(self,branch):
        mycursor.execute("SELECT * FROM student_info WHERE branch=%s",branch)
        result = mycursor.fetchall()
        for rows in result:
            print(rows)

    ####### Update data in database ######
    def updateStudentData(self):
        id = input("Enter id : ")
        name = input("Enter Name : ")
        branch = input("Enter Branch : ")
        year = input("Enter year : ")
        phone = input("Enter phone : ")
        email = input("Enter Email : ")
        upInput = (name, branch, year, phone, email,id)
        mycursor.execute("UPDATE student_info SET name=%s, branch=%s, year=%s, phone=%s, email=%s WHERE id=%s",upInput)
        mydb.commit()
        print("Updated")

    ###### Delete row from database ######
    def deleteStudentData(self,id):
        mycursor.execute("DELETE FROM student_info where id = %s",(idDel,))
        mydb.commit()
        print("Deleted successfully")

sd = StudentData(2)
sd1 = StudentData(3)
# print(sd.name)
print(sd.age)
print(sd1.showVariable())
print(sd==sd1)

# i = input("Enter any of these Options 'i' or 'sh' or 'se' or 'de' or 'up' : ")
# if(i=="i"):
#     name = input("Enter Name : ")
#     branch = input("Enter Branch : ")
#     year = input("Enter year : ")
#     phone = input("Enter phone : ")
#     email = input("Enter Email : ")
#     sd.insertStudentData(name,branch,year,phone,email)
# elif(i=="sh"):
#     sd.getAllStudentData()
# elif(i=="se"):
#     branch = input("Enter Branch : ")
#     sd.searchStudentData(branch)
# elif(i=="up"):
#     sd.getAllStudentData()
#     sd.updateStudentData()
# elif(i=="de"):
#     sd.getAllStudentData()
#     idDel = input("Enter id : ")
#     sd.deleteStudentData(id)
# else:
#     print("Select something dude!")