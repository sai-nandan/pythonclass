emp_game = input("Enter the game c-cricket v-volleyball b-basketball : ")
student_id = input("Enter the student id : ")
if student_id in student_ids:
    if emp_game == "c":
        sports_subscribed['cricket'].add(student_id)
    elif emp_game == "v":    
        sports_subscribed['volleyball'].add(student_id)
    elif emp_game == 'b':
        sports_subscribed['basketball'].add(student_id)
    else:
        print("Student id not found!")