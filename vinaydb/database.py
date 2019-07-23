import mysql.connector as sql

class Mydatabase:

    def __init__(self):
        self.mydb = sql.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="student_database",
                    port=3307
                )
        self.mycursor = self.mydb.cursor()

    def insertStudentData(self,id,name,branch,year,phone,sport):
        print(id,name,branch,year,phone,sport)
        val = (id,name,branch,year,phone,sport)
        print (val)
        self.mycursor.execute("INSERT INTO students_data (id,name,branch,year,phone,sport) VALUES (%s,%s,%s,%s,%s,%s)",val)
        self.mydb.commit()

    # def searchStudentData(x):
    #     search = input('enter the key to search: ')
    #     mycursor.execute("SELECT * FROM student_info WHERE branch=%s",search)