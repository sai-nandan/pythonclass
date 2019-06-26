from id_generation import GenerateId
from saving_data import saving_data
from database import Mydatabase
from games import selectGame

class Student_record:
    # using MYSQL to store data
    def __init__(self):
        self.activity = input('you want to add or search: ')
        if(self.activity=='add'):
            self.db = Mydatabase()
            self.sg = Selectgame()
            self.student_year()

    def student_year(self):
        branch  =   input('enter your branch: ')
        year    =   input('enter your year: ')
        name    =   str(input('enter student name: '))
        ph_no   =   int(input('enter phone number: '))
        id      =   GenerateId.id_gen(branch,year)
        sport   =   self.sg.selectGame()
        self.db.insertStudentData(id,name,branch,year,ph_no,sport)
            
sports = Student_record()
