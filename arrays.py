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
        print(student_ids)
        print(student_info)
        # for k,v in student_info.items():
        #     print(v['name'])
    elif get_user_option=="i":    
        get_id = input('Enter student Id: ')
        get_name = input("Enter student Name :")
        get_branch = input("Enter branch : ")
        get_year = input("Enter year : ")
        student_ids.add(get_id)
        student_info[get_id] = {'name':get_name,'branch':get_branch,'year':get_year}
        print(student_info[get_id])
    elif get_user_option=="g":
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
    elif get_user_option == "gs":
        get_game_subscribers = input("Enter game c-cricket v-volleyball b-basketball : ")
        if get_game_subscribers == "all":
            for k,v in sports_subscribed.items():
                print(k,"subscribed students:")
                for s in v:
                    print(student_info[s]['name'])
        elif get_game_subscribers == "c":
            print("Cricket subscribed students:")
            for v in sports_subscribed['cricket']:
                print(student_info[v]['name'])
            # print(sports_subscribed)
        elif get_game_subscribers == 'cb':
            crick_basket = sports_subscribed['cricket'].intersection(sports_subscribed['basketball'])
            for s in crick_basket:
                print(student_info[s]['name'])
            print(crick_basket)
    else:
        break

# for k,v in student_info.items():
#     print(k,end=" ")
#     print(v['name'])