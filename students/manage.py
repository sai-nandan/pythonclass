from manage_student import addStudent, getStudent
# from manage_sports import add_game, getsubscribers, subscribe_to_game


# declaring student data
student_ids = {'A101','A102','A103'}
student_ids.add('A104')
student_ids.add('A105')
print(student_ids)
games = ('cricket','football','basketball','volleyball','chess')

student_info = {
    'A101':{'name':'Teja','branch':'CSE','year':4},
    'A102':{'name':'Vinay','branch':'Mech','year':4},
    'A103':{'name':'Kanthi','branch':'Civil','year':4},
    'A104':{'name':'Nandan','branch':'BSC','year':3}
    }
student_info['A105'] = {'name':'Chaitanya','branch':'BSC','year':3}
sports_subscribed = {
    'cricket':{'A101','A102','A103'},
    'basketball':{'A101','A102'},
    'volleyball':{'A103'}
}
# print(student_ids)
# print(student_info['A101']['name'])
while True:
    get_user_option = input("What do you want to do? ")
    if get_user_option=="p":
        getStudent.getStudentInfo(student_info)
    elif get_user_option=="i":    
        result = addStudent.addNewStudent(student_ids,student_info)
        student_ids = result[0]
        student_info = result[1]
        getStudent.getStudentInfo(student_info)
    # elif get_user_option=="g":
        
    # elif get_user_option == "gs":
        
    else:
        break

# for k,v in student_info.items():
#     print(k,end=" ")
#     print(v['name'])