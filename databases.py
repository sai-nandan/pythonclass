employee_ids = {'emp1','emp2','emp3'}

employee_details = {
                    'emp1':{'name':'Chaitanya','lname':'Bhallamudi','age':31,'designation':'Jr.Software Engineer'},
                    'emp2':{'name':'Bhavani','lname':'Bhallamudi','age':25,'designation':'Record Assistant'},
                    'emp3':{'name':'Sree','lname':'Bhallamudi','age':2,'designation':'The Kid'}
                   }
                   # Chaitu

employee_games = {
    'Chess':{'emp1'},
    'Carroms':{'emp2','emp3'},
    'Rummy':{'emp1','emp3'}
}                   
while True:
    action  = input("Enter your choice:- 'p': print / 'i': input / 's': selected employee details / 'b' break: ")
    if action == 'p':
        for emp,detail in employee_details.items():
            print(emp+":")
            print("Employee id "+str(emp)+" details: "+str(employee_details[emp]['name'])+" "+str(employee_details[emp]['lname'])+" is of "+str(employee_details[emp]['age'])+" years and is "+str(employee_details[emp]['designation'])+" in the organization")
            print("-----------------------------------------------")
    elif action == 'i':
        emp_id = input("Enter Employee Id: ")
        emp_name = input("Enter Employee name: ")
        emp_lname = input("Enter Employee last name: ")
        emp_age = input("Enter Employee age: ")
        emp_designation = input("Enter Employee designation: ")
        emp_game = input("Select the game the employee plays: 'ch'-> Chess / 'ca'-> Carroms / 'r'-> Rummy")
        if emp_game == "ch":
            employee_games['Chess'].add(emp_id)
            emp_plays = "Chess"
        elif emp_game == "ca":    
            employee_games['Carroms'].add(emp_id)
            emp_plays = "Carroms"
        else:
            employee_games['Rummy'].add(emp_id)
            emp_plays = "Rummy"
        employee_details[emp_id] = {'name':emp_name,'lname':emp_lname,'age':emp_age,'designation':emp_designation}

        print("Employee id "+str(emp_id)+" details: "+str(employee_details[emp_id]['name'])+" "+str(employee_details[emp_id]['lname'])+" is of "+str(employee_details[emp_id]['age'])+" years and is "+str(employee_details[emp_id]['designation'])+" in the organization, who plays "+emp_plays)
    elif action == 'b':
        break
    elif action == 's':
        get_id = input("Enter the Id of an employee: \n")
        if get_id in employee_ids:
            print("Employee id "+str(get_id)+" details: "+str(employee_details[get_id]['name'])+" "+str(employee_details[get_id]['lname'])+" is of "+str(employee_details[get_id]['age'])+" years and is "+str(employee_details[get_id]['designation'])+" in the organization")
        else:
            print("No employee exists with that id")                                

